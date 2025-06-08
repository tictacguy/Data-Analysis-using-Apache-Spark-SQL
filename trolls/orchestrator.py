import os
import subprocess

RAW_DATA_PATH = "data/raw/troll_tweets.csv"
SCRIPTS_PATH = "scripts"

def run_script(script_name):
    print(f"\n🚀 Running {script_name} ...\n")
    result = subprocess.run(["python", os.path.join(SCRIPTS_PATH, script_name)], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(f"⚠️ Error in {script_name}:\n{result.stderr}")

if os.path.exists(RAW_DATA_PATH):
    print(f"✅ Dataset already exists: {RAW_DATA_PATH} — skipping download.")
else:
    print(f"❌ Dataset not found — running download_dataset.py")
    run_script("download_dataset.py")

run_script("spark_analysis.py")

run_script("community_detection.py")

run_script("plot_trends.py")

print("\n✅ All steps completed! Project ready 🚀\n")
