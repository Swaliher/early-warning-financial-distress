import pandas as pd
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import matplotlib.pyplot as plt
import os

# Aligned with root project directory
ALERT_CSV_PATH = "output/alert_logs.csv"
DATA_CSV_PATH = "output/indian_smart_z_fscore.csv"
CHART_PATH = "output/alert_dashboard.png"

DOWNGRADE_TARGETS = ["distress", "weak", "grey"]
VALID_PRIOR_STATUSES = ["safe", "strong", "neutral"]

# Configure SMTP
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = "your.email@gmail.com"        # 🔁 Replace with your Gmail
SMTP_PASS = "your-app-password"           # 🔁 Replace with Gmail App Password
EMAIL_FROM = SMTP_USER
EMAIL_TO = ["recipient@example.com"]      # 🔁 List of recipients

def load_and_prepare_data():
    df = pd.read_csv(DATA_CSV_PATH)
    df = df[df["Status"].notna()]
    df = df[~df["Status"].str.lower().isin(["finance sector", "skipped"])]
    df.sort_values(by=["Ticker", "Year"], inplace=True)
    return df

def detect_transitions(df):
    alerts = []
    for ticker, group in df.groupby("Ticker"):
        group = group.reset_index(drop=True)
        for i in range(1, len(group)):
            prev = group.loc[i-1, "Status"].lower()
            curr = group.loc[i, "Status"].lower()
            year = int(group.loc[i, "Year"])
            if prev in VALID_PRIOR_STATUSES and curr in DOWNGRADE_TARGETS:
                alerts.append({
                    "Ticker": ticker,
                    "Year": year,
                    "From": prev.title(),
                    "To": curr.title(),
                    "Model": group.loc[i, "Model"]
                })
    return alerts

def save_alerts(alerts):
    df_alerts = pd.DataFrame(alerts)
    df_alerts["Alert Generated On"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    os.makedirs("output", exist_ok=True)
    df_alerts.to_csv(ALERT_CSV_PATH, index=False)
    print(f"🚨 {len(alerts)} alert(s) saved to {ALERT_CSV_PATH}")
    return df_alerts

def send_email(df_alerts):
    body = df_alerts.to_html(index=False)
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "🚨 Company Downgrade Alerts"
    msg["From"] = EMAIL_FROM
    msg["To"] = ", ".join(EMAIL_TO)
    msg.attach(MIMEText(body, "html"))

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    print("📤 Alert email sent.")

def generate_dashboard(df_alerts):
    counts = df_alerts["Ticker"].value_counts()
    plt.figure(figsize=(10, 6))
    counts.plot(kind="barh", color="crimson")
    plt.title("📉 Downgrade Alert Counts by Ticker")
    plt.xlabel("Number of Downgrades")
    plt.tight_layout()
    plt.savefig(CHART_PATH)
    plt.close()
    print(f"🖼 Dashboard chart saved to {CHART_PATH}")

def main():
    if not os.path.exists(DATA_CSV_PATH):
        print(f"❌ Missing source file: {DATA_CSV_PATH}")
        return

    df = load_and_prepare_data()
    alerts = detect_transitions(df)

    if not alerts:
        print("✅ No downgrades detected.")
        return

    df_alerts = save_alerts(alerts)
    send_email(df_alerts)
    generate_dashboard(df_alerts)

if __name__ == "__main__":
    main()
