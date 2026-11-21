
import pandas as pd
import numpy as np


def clean_agent_data(txns, agents):

    # Make copies so the original datasets remain unchanged
    txns = txns.copy()
    agents = agents.copy()

    cleaning_log = []

    # 1. Remove exact duplicate transactions
    before = len(txns)
    txns = txns.drop_duplicates().copy()
    removed = before - len(txns)

    cleaning_log.append({
        "Step": "Duplicate removal",
        "Action": "Removed exact duplicate rows",
        "Rows affected": removed
    })

    # 2. Standardise transaction types
    txns["txn_type"] = (
        txns["txn_type"]
        .astype("string")
        .str.strip()
        .str.lower()
        .str.capitalize()
    )

    cleaning_log.append({
        "Step": "Transaction types",
        "Action": "Standardised transaction type formatting",
        "Rows affected": len(txns)
    })

    # 3. Clean transaction amounts
    original_amount = txns["amount"].copy()

    txns["amount"] = pd.to_numeric(
        txns["amount"], errors="coerce"
    )

    txns["amount_flag"] = np.select(
        [
            original_amount.isna(),
            original_amount.notna() & txns["amount"].isna(),
            txns["amount"].eq(250000)
        ],
        [
            "Missing",
            "Invalid",
            "Review"
        ],
        default="Valid"
    )

    # 4. Standardise and convert transaction dates
    txns["txn_date"] = (
        txns["txn_date"]
        .astype("string")
        .str.strip()
        .str.replace("/", "-", regex=False)
    )

    txns["txn_date"] = pd.to_datetime(
        txns["txn_date"], errors="coerce"
    )

    txns["date_flag"] = np.where(
        txns["txn_date"].isna(),
        "Invalid",
        "Valid"
    )

    # 5. Flag potential outliers using IQR
    valid_amounts = txns["amount"].dropna()

    if len(valid_amounts) > 0:
        q1 = valid_amounts.quantile(0.25)
        q3 = valid_amounts.quantile(0.75)
        iqr = q3 - q1

        lower_limit = q1 - 1.5 * iqr
        upper_limit = q3 + 1.5 * iqr

        txns["iqr_flag"] = np.where(
            txns["amount"].isna(),
            "Not assessed",
            np.where(
                (txns["amount"] < lower_limit) |
                (txns["amount"] > upper_limit),
                "Potential outlier",
                "Normal"
            )
        )
    else:
        txns["iqr_flag"] = "Not assessed"

    # 6. Merge transactions with agent information
    clean_txns = txns.merge(
        agents,
        on="agent_id",
        how="left",
        indicator=True
    )

    clean_txns["agent_flag"] = np.where(
        clean_txns["_merge"] == "both",
        "Matched",
        "Unknown agent"
    )

    clean_txns.drop(columns=["_merge"], inplace=True)

    cleaning_log.append({
        "Step": "Agent matching",
        "Action": "Matched transactions with agent records",
        "Rows affected": int(
            (clean_txns["agent_flag"] == "Unknown agent").sum()
        )
    })

    # 7. Create cleaning log
    cleaning_log = pd.DataFrame(cleaning_log)

    return clean_txns, cleaning_log
