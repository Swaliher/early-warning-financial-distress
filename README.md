# 🛑 Early Warning System for Financial Distress

A full-fledged, automated Z-Score and Piotroski F‑Score based framework designed to detect early signs of financial distress in Indian publicly listed companies using real-time data from Yahoo Finance. This project bridges academic financial theory and practical implementation with clear visualization, alerting, and email notifications.

---

## 📈 Objective

This project aims to **identify distressed or weakening companies** by computing:

- 📉 **Altman Z″-Scores**: For non-financial companies
- 📊 **Piotroski F‑Scores**: For tech-sector companies
- 🧠 **Trend Analysis and Alert Generation**: Based on year-over-year transitions

---

## 🧠 Core Features

| Module              | Description |
|---------------------|-------------|
| 🧮 `compute_scores.py` | Computes Altman Z″ or Piotroski F‑Scores based on sector |
| 📉 `generate_plots.py` | Visualizes Z″ trends over years (grey & distress thresholds shown) |
| 📬 `alert_generator.py` | Flags downgrade transitions and generates alert CSVs |
| ✉️ `emailer.py`         | Sends email alerts securely using `.env` credentials |
| 🔄 `run_all.py`         | Unified runner script to automate the full pipeline |
| 🧪 Unit-tested and modular structure for future extensibility and deployment |

---

## 💼 Methodology

### 🔹 Altman Z″ Score
Adapted for emerging markets. Applied to all non-financial, non-tech sectors. Calculated using:
- Working Capital / Total Assets
- Retained Earnings / Total Assets
- EBIT / Total Assets
- Book Equity / Total Liabilities

📌 Winsorized at Z = 8 to control outlier skewing.

### 🔹 Piotroski F‑Score
Applied to:
- Technology
- Software
- IT Services

Metrics include:
- ROA, CFO, Accruals
- Leverage, Liquidity, Equity Dilution
- Gross Margin & Asset Turnover

📌 Out of 9 — scores ≥6 = Strong, ≤3 = Weak

---

## 📦 Folder Structure

