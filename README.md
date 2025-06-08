# Analyzing Russian Troll Tweets using Apache Spark SQL

## 📚 Project Overview

This project performs a comprehensive analysis of a dataset of tweets attributed to Russian troll accounts.  
The analysis explores temporal trends, user activity, language usage, hashtag patterns, and social network structures through efficient data processing and visualization techniques.

The goal is to better understand the behavior of these accounts and their coordinated activities on social media.

---

## 🗂 Project Structure

russian_trolls/
│
├── scripts/ # Python scripts for each analysis step
│ ├── download_dataset.py
│ ├── spark_analysis.py
│ ├── plot_trends.py
│ ├── community_detection.py
│
├── data/ # Data folder
│ ├── raw/ # Raw downloaded data (CSV)
│ ├── parquet/ # Processed data (Parquet)
│ ├── trends/ # Trend analysis outputs (CSV + plots)
│ ├── communities/ # Community detection outputs (CSV + graph)
│
└── README.md # Project documentation (this file)

---

## 🔍 Dataset

- **Source:** [FiveThirtyEight Russian Troll Tweets GitHub Repository](https://github.com/fivethirtyeight/russian-troll-tweets)
- **Format:** CSV
- **Fields:** `author`, `content`, `publish_date`, `language`, `hashtags`, `mentions`, ...

*Note:* For this project, one CSV file was used from the dataset.

---

## 🚀 Project Workflow

1️⃣ **Downloading the dataset**  
`download_dataset.py` downloads the CSV and saves it in `/data/raw/`.

2️⃣ **Processing with Spark**  
`spark_analysis.py` converts the CSV to Parquet and runs Spark SQL queries to extract:
- Temporal tweet trends
- Top authors
- Language distribution
- Top hashtags

3️⃣ **Trend analysis visualization**  
`plot_trends.py` creates visual plots of tweet activity over time.

4️⃣ **Social network & community detection**  
`community_detection.py` builds a mention graph and detects communities using Label Propagation.

---

## 📊 Outputs

✅ **Raw and processed data**
- `troll_tweets.csv` (raw)
- `tweets.parquet` (optimized for queries)

✅ **Trend analysis results** (in `/data/trends/`)
- CSVs: tweet trends, top authors, language distribution, top hashtags
- PNG: temporal trends plot

✅ **Community analysis results** (in `/data/communities/`)
- CSV: user-community mapping, community size summary
- PNG: mention graph with community coloring

---

## 💪 Project Highlights

- **Modular design** → Each analysis step in its own script
- **Efficient data processing** → Uses Apache Spark and Parquet
- **Comprehensive analysis** → Combines statistical trends and social network analysis
- **Clear data organization** → Easy to navigate and reproduce

---

## 🔗 Repository

GitHub Repository: [https://github.com/tomokazukomiya/Data_Analysis_Using_Apache_SQL](https://github.com/tomokazukomiya/Data_Analysis_Using_Apache_SQL)

---

## 🚧 Possible Future Improvements

- Add sentiment analysis on tweet content
- Implement time-based evolution of communities
- Explore more advanced graph algorithms

---

## 📝 License

This project is for educational and research purposes.
Original dataset provided by [FiveThirtyEight](https://github.com/fivethirtyeight/russian-troll-tweets).