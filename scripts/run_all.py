import subprocess
import os
from scripts.emailer import send_email

def run_script(label, path):
    print(f"\n🚀 {label}...")
    try:
        subprocess.run(["python", path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed during: {label}")
        print(f"Error: {e}")
        exit(1)

def main():
    run_script("Running score computation", "scripts/compute_scores.py")
    run_script("Running alert detection", "scripts/alert_generator.py")

    # Check if alert output exists
    alert_file = "alerts/alerts_summary.txt"
    if os.path.isfile(alert_file):
        with open(alert_file, "r", encoding="utf-8") as f:
            content = f.read().strip()
        if content:
            send_email(
                subject="🚨 Financial Distress Alert – EWSD System",
                body=content,
                attachment_path=alert_file
            )
        else:
            print("\n📭 No alert files found. Email not sent.")
    else:
        print("\n📭 No alert files found. Email not sent.")

    print("\n✅ Workflow complete.")

if __name__ == "__main__":
    main()
