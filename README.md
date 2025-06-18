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

## 📁 Project Structure

```
early-warning-financial-distress/
├── scripts/                    # All functional scripts
│   ├── compute_scores.py       # Core model logic (Z″ + F-Score)
│   ├── generate_plots.py       # Z″ visualizations with thresholds
│   ├── alert_generator.py      # Detects and logs downgrades
│   ├── emailer.py              # Sends alerts via email securely
│   └── run_all.py              # Full end-to-end execution pipeline
├── charts/                     # Generated Z-trend plots (auto-saved)
├── data/                       # Output CSVs and Excel reports
├── .env.example                # Sample env file (no real credentials)
├── .gitignore                  # Ignores sensitive and bulky files
├── requirements.txt            # Python package dependencies
├── README.md                   # This project documentation
```


## 📊 Sample Output

**Summary Table**

| Sector              | Model              | Safe | Distress | Weak |
|---------------------|--------------------|------|----------|------|
| Industrials         | Altman Z″          | ✅ 39 | ❌  0     | -    |
| Technology          | Piotroski F‑Score  | -    | -        | ❗ 5  |
| Basic Materials     | Altman Z″          | ✅ 20 | ❌  0     | -    |

**Visual Output**

All `charts/*.png` display historical Z″ scores with clear risk thresholds.

---


## 📧 Email Configuration (.env)

Before running the alert pipeline, create a `.env` file using the template below:

```ini
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your.email@gmail.com
EMAIL_PASS=your_app_password
EMAIL_TO=recipient@example.com
```

Use an [App Password](https://support.google.com/accounts/answer/185833) if you're using Gmail with 2FA.

---

## 🔁 Pipeline Execution Guide

### 1️⃣ Clone the Repository and Setup the Environment

```bash
git clone https://github.com/Swaliher/early-warning-financial-distress.git
cd early-warning-financial-distress
python -m venv .venv
source .venv/bin/activate  # On Windows: .\.venv\Scripts\activate
pip install -r requirements.txt
```

### 2️⃣ Configure Environment Variables

```bash
cp .env.example .env
```

Then, open `.env` and update it with your email credentials.

### 3️⃣ Run the Full Pipeline

```bash
python scripts/run_all.py
```

This runs the complete financial distress detection workflow.

---

## 🧠 Core Pipeline Modules

| Script                 | Functionality Description |
|------------------------|---------------------------|
| `data_fetcher.py`      | Fetches financial statements from Yahoo Finance |
| `compute_zscore.py`    | Calculates Altman Z-score for each company |
| `generate_report.py`   | Generates Excel reports with Z-score outputs |
| `send_email.py`        | Sends Z-score alert report via email |
| `run_all.py`           | Orchestrates full pipeline execution |
| `.env`                 | Stores secure credentials (email/SMTP) |

---

## 📊 Technologies & Libraries Used

- **Python 3.11+**
- `yfinance`, `requests`: Market data scraping
- `pandas`, `numpy`: Financial metrics and calculations
- `matplotlib`: Z-score trend charts
- `openpyxl`: Report formatting in Excel
- `smtplib`, `dotenv`: Secure email notifications

---

## 🔥 Why This Stands Out

- ✅ Fully automated detection and delivery pipeline
- 📈 Uses **Altman Z-scores** for financial stress identification
- 📬 Real-time alerts via email — ideal for analysts or risk teams
- 💡 Transparent, reproducible, and modular implementation

---

## 🏁 Future Enhancements

- 🗣 Add earnings call transcript sentiment
- 📊 Streamlit-based interactive dashboard
- ⚙️ REST API deployment for fintech integration

---

## 🤝 About Me

I'm an aspiring financial analyst with a strong interest in risk modeling and automation in finance.

📧 swaliher3@gmail.com  
🌐 GitHub: [Swaliher](https://github.com/Swaliher)  
📄 Resume: Available on request

---

## 📜 License

This project is intended for educational and demonstration purposes. If used in research or coursework, please attribute the author.

> Built with 📊 Finance, 💻 Python, and ❤️ a passion for risk intelligence.
