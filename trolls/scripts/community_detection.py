import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from tqdm import tqdm

import logging
logging.getLogger("py4j").setLevel(logging.ERROR)

print("🚀 Starting Community Detection - Russian Troll Tweets")

print("✅ Creating Spark session...")
spark = SparkSession.builder.appName("Community Detection - Russian Troll Tweets").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

print("✅ Loading Parquet file...")
df = spark.read.parquet("data/parquet/tweets.parquet")

print("✅ Converting to Pandas DataFrame...")
df_pd = df.select("author", "content").toPandas()

print("✅ Building mention graph...")
G = nx.DiGraph()

for row in tqdm(df_pd.itertuples(), total=len(df_pd), desc="Building Graph"):
    author = row.author
    content = row.content

    mentions = []
    if content:
        mentions = [word[1:] for word in content.split() if word.startswith("@")]

    for mention in mentions:
        if mention.strip():
            G.add_edge(author, mention)

print(f"📊 Number of nodes: {G.number_of_nodes()}")
print(f"📊 Number of edges: {G.number_of_edges()}")

print("✅ Converting graph to undirected...")
G_undirected = G.to_undirected()

print("✅ Running label propagation community detection...")
communities = list(nx.community.label_propagation_communities(G_undirected))
print(f"📊 Number of communities found: {len(communities)}")

print("📊 Community sizes:")
for i, community in enumerate(communities):
    print(f" - Community {i}: {len(community)} users")

print("✅ Saving communities to CSV...")
community_list = []
for i, community in enumerate(communities):
    for user in tqdm(community, desc=f"Saving Community {i}", leave=False):
        community_list.append((user, i))

df_communities = pd.DataFrame(community_list, columns=["user", "community_id"])
df_communities.to_csv("data/communities/user_communities.csv", index=False)
print("✅ Communities saved to data/communities/user_communities.csv")

df_summary = df_communities["community_id"].value_counts().reset_index()
df_summary.columns = ["community_id", "num_users"]
df_summary = df_summary.sort_values("community_id")
df_summary.to_csv("data/communities/community_summary.csv", index=False)
print("✅ Community summary saved to data/communities/community_summary.csv")

print("✅ Plotting mention graph colored by community...")

community_dict = dict(zip(df_communities["user"], df_communities["community_id"]))
node_colors = [community_dict.get(node, -1) for node in G_undirected.nodes()]

plt.figure(figsize=(12, 10))
nx.draw_spring(G_undirected, node_size=30, node_color=node_colors, cmap='tab20', edge_color='gray', alpha=0.6)
plt.title("Mention Graph - Communities Colored")
plt.savefig("data/communities/mention_graph_colored.png")
print("✅ Graph saved to data/communities/mention_graph_colored.png")

print("🏁 Community Detection completed! Shutting down Spark...")
spark.stop()