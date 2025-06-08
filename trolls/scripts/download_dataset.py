import os
import requests

csv_url = "https://raw.githubusercontent.com/fivethirtyeight/russian-troll-tweets/master/IRAhandle_tweets_1.csv"
output_dir = "data/raw"
os.makedirs(output_dir, exist_ok=True)

filename = "troll_tweets.csv"
output_path = os.path.join(output_dir, filename)

print(f"Downloading {csv_url} to {output_path}...")
response = requests.get(csv_url, stream=True)
response.raise_for_status()

with open(output_path, "wb") as f:
    for chunk in response.iter_content(chunk_size=8192):
        f.write(chunk)

print(f"Download complete: {output_path}")