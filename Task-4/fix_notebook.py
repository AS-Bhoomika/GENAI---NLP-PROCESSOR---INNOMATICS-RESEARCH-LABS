import json

file_path = "Task-4/Twitter_Sentiment_Analysis.ipynb"

with open(file_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

if "metadata" in nb and "widgets" in nb["metadata"]:
    del nb["metadata"]["widgets"]

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(nb, f)

print("Notebook fixed successfully!")