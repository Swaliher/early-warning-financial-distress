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

## 📬 Email Notifications

Set your environment variables in a `.env` file:

```env
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your.email@gmail.com
EMAIL_PASS=your_app_password
EMAIL_TO=recipient@example.com

## 🔁 How to Run

### 1️⃣ Clone Repo and Setup

```bash
git clone https://github.com/Swaliher/early-warning-financial-distress.git
cd early-warning-financial-distress
python -m venv .venv
source .venv/bin/activate  # On Windows: .\.venv\Scripts\activate
pip install -r requirements.txt
2️⃣ Create .env from Template
bash
Copy
Edit
cp .env.example .env
Then update it with your credentials.

3️⃣ Run Full Pipeline
bash
Copy
Edit
python scripts/run_all.py
📈 Technologies Used
Python 3.11+

yfinance for data ingestion

pandas, numpy for data wrangling

matplotlib for Z-trend charts

openpyxl for Excel styling

smtplib + dotenv for secure email delivery

🔥 Why This Project Stands Out
✅ End-to-end automation (score → visualization → alert → email)

📊 Real data from NSE-listed firms

⚠️ Detects distress before earnings collapse

📬 Notifies instantly — ideal for analysts or fund managers

💼 Built by hand: No black-box APIs or pre-trained tools

🧪 Production-grade structure and modularity

🤝 Hire Me
I'm an aspiring financial analyst, deeply passionate about quantitative finance and risk modeling. If this project caught your eye, feel free to connect or reach out!

📧 Email: swalihfinance@gmail.com

🌐 GitHub: Swaliher

📄 Resume: Available on request

🏁 Future Enhancements
 Integrate earnings call transcript sentiment

 Web dashboard with Dash or Streamlit

 Sector-specific alert thresholds

 REST API deployment for live dashboards

💬 License
This project is for academic and demonstrative use. Please credit the author if reused in research or coursework.

Built with 📊 Finance, 💻 Python, and ❤️ passion for risk intelligence.
