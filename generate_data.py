{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNJ6kpT0gkpysiRbqrKkDcX",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Trendtek254/plp-da-a3-duka-sales-and-agent-cleanup/blob/main/generate_data.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "id": "Rc3QpNo3kqlY"
      },
      "outputs": [],
      "source": [
        "#PYTHON · DATASET GENERATOR FOR DUKA ELECTRONICS\n",
        "\n",
        "import numpy as np\n",
        "import pandas as pd\n",
        "\n",
        "rng = np.random.default_rng(2026)\n",
        "n = 1000\n",
        "products = {\"Phone\": 15000, \"Laptop\": 65000, \"Headphones\": 2500,\n",
        "            \"Tablet\": 28000, \"Charger\": 1200}\n",
        "\n",
        "sales = pd.DataFrame({\n",
        "    \"order_id\": range(1001, 1001 + n),\n",
        "    \"order_date\": pd.to_datetime(\"2026-01-01\")\n",
        "                  + pd.to_timedelta(rng.integers(0, 180, n), unit=\"D\"),\n",
        "    \"branch\": rng.choice([\"Nairobi\", \"Mombasa\", \"Kisumu\", \"Nakuru\", \"Eldoret\"], n,\n",
        "                         p=[0.4, 0.2, 0.15, 0.15, 0.1]),\n",
        "    \"product\": rng.choice(list(products), n),\n",
        "    \"quantity\": rng.integers(1, 6, n),\n",
        "    \"channel\": rng.choice([\"In-store\", \"Online\", \"Phone order\"], n,\n",
        "                          p=[0.55, 0.35, 0.10]),\n",
        "})\n",
        "\n",
        "sales[\"unit_price\"] = sales[\"product\"].map(products)\n",
        "sales.to_csv(\"duka_sales.csv\", index=False)\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#PYTHON · DATASET GENERATOR  for enegagement 2\n",
        "\n",
        "import numpy as np, pandas as pd\n",
        "\n",
        "rng = np.random.default_rng(44)\n",
        "\n",
        "n = 600\n",
        "\n",
        "agents = pd.DataFrame({\n",
        "    \"agent_id\": [f\"AG{i:03d}\" for i in range(1, 21)],\n",
        "    \"county\": rng.choice([\"Nairobi\", \"Kiambu\", \"Nakuru\", \"Mombasa\", \"Kisumu\"], 20),\n",
        "    \"onboarded\": pd.date_range(\"2024-01-01\", periods=20, freq=\"MS\").strftime(\"%Y-%m-%d\"),\n",
        "})\n",
        "\n",
        "txns = pd.DataFrame({\n",
        "    \"txn_id\": [f\"TX{i:05d}\" for i in range(1, n + 1)],\n",
        "    \"agent_id\": rng.choice(agents[\"agent_id\"], n),\n",
        "    \"txn_type\": rng.choice([\"Deposit\", \"withdrawal\", \"DEPOSIT \",\n",
        "                            \"Withdrawal\", \"deposit\"], n),\n",
        "    \"amount\": rng.lognormal(7.5, 0.8, n).round(0).astype(str),\n",
        "    \"txn_date\": (pd.to_datetime(\"2026-03-01\")\n",
        "                 + pd.to_timedelta(rng.integers(0, 60, n), unit=\"D\")).strftime(\"%Y-%m-%d\"),\n",
        "})\n",
        "\n",
        "idx = rng.choice(n, 30, replace=False)\n",
        "\n",
        "txns.loc[idx[:15], \"amount\"] = np.nan\n",
        "txns.loc[idx[15:20], \"amount\"] = \"N/A\"\n",
        "txns.loc[idx[20:25], \"amount\"] = \"250000\"\n",
        "txns.loc[idx[25:], \"txn_date\"] = txns.loc[idx[25:], \"txn_date\"].str.replace(\"-\", \"/\")\n",
        "\n",
        "txns = pd.concat([txns, txns.sample(12, random_state=1)], ignore_index=True)\n",
        "\n",
        "txns.loc[rng.choice(len(txns), 8, replace=False), \"agent_id\"] = \"AG099\"\n",
        "\n",
        "agents.to_csv(\"agents.csv\", index=False)\n",
        "txns.to_csv(\"agent_transactions.csv\", index=False)"
      ],
      "metadata": {
        "id": "SYdfUQ32uDwl"
      },
      "execution_count": 5,
      "outputs": []
    }
  ]
}