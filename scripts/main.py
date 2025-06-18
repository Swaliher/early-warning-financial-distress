# scripts/main.py

import compute_scores
import generate_plots
import alert_generator

if __name__ == "__main__":
    print("🚀 Starting full pipeline...\n")

    compute_scores.main()
    generate_plots.main()
    alert_generator.main()

    print("\n✅ Pipeline completed successfully.")
