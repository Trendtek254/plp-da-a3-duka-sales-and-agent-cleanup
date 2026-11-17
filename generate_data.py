{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOWl0rKOleGvSnJS4VPNqoz",
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
        "sales.to_csv(\"duka_sales.csv\", index=False)"
      ]
    }
  ]
}