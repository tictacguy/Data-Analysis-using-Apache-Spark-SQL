import pandas as pd
import matplotlib.pyplot as plt
import glob
csv_files = glob.glob("data/trends/tweet_trends.csv/part-*.csv")

if not csv_files:
    print("❌ No CSV files found in tweet_trends.csv directory!")
    exit(1)

print(f"✅ Found CSV file: {csv_files[0]}")

df = pd.read_csv(csv_files[0])

df['tweet_date'] = pd.to_datetime(df['tweet_date'])
df = df.sort_values('tweet_date')

plt.figure(figsize=(12, 6))
plt.plot(df['tweet_date'], df['tweet_count'], marker='o', linestyle='-')

plt.title("Number of Tweets Over Time")
plt.xlabel("Date")
plt.ylabel("Tweet Count")
plt.grid(True)
plt.tight_layout()

plt.show()

plt.savefig("data/trends/tweet_trends_plot.png")
print("✅ Plot saved to data/trends/tweet_trends_plot.png")
