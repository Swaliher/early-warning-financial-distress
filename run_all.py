import subprocess
import os
import sys

print("\n🚀 Running score computation...")
try:
    subprocess.run([sys.executable, "scripts/compute_scores.py"], check=True)
except subprocess.CalledProcessError as e:
    print("\n❌ Failed during: Running score computation")
    print("Error:", e)
    exit(1)

print("\n🔍 Running alert detection...")
try:
    subprocess.run([sys.executable, "scripts/alert_generator.py"], check=True)
except subprocess.CalledProcessError as e:
    print("\n❌ Failed during: Alert generation")
    print("Error:", e)
    exit(1)

# 🔍 Alert files check
alert_files = [
    "output/z_outliers.csv",
    "output/ratios_warning.csv",
    "output/alert_logs.csv",
    "output/alert_dashboard.png"
]
attachments = [f for f in alert_files if os.path.exists(f) and os.path.getsize(f) > 0]

if attachments:
    print("\n📧 Alerts found. Sending email...")
    try:
        subprocess.run([sys.executable, "scripts/emailer.py"], check=True)
    except subprocess.CalledProcessError as e:
        print("\n❌ Failed during: Email sending")
        print("Error:", e)
else:
    print("\n📭 No alert files found. Email not sent.")

print("\n✅ Workflow complete.")
