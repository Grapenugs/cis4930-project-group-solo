import logging
import os

from api_client import fetch_repos
from storage import save_to_csv, add_timestamp
from datetime import datetime

# Capture base directory where the script lives by going back two layers from
# abspath. This is where /logs and /data live
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Path leading to logs directory
logs_dir = f"{BASE_DIR}/logs"

#Create log directory if it does not exist
os.makedirs(logs_dir, exist_ok=True)

#Create log file if it doesnt exist, and log all messages to it
logging.basicConfig(
    filename =f"{logs_dir}/pipeline.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)


logging.info("Starting pipeline run")

repos = fetch_repos()

print(f"Fetched {len(repos)} repositories")
logging.info(f"Fetched {len(repos)} repositories")

logging.info(f"Extracting 5 data fields from each repository")

#Extract 5 pieces of data from each record, store in records
records = []
for repo in repos:
    record = {
        "full_name": repo.get("full_name", "None"),
        "description": repo.get("description", "None"),
        "stars": repo.get("stargazers_count", 0),
        "forks": repo.get("forks_count", 0),
        "language": repo.get("language", "Unknown")
    }
    records.append(record)

logging.info(f"Extraction complete, Adding timestamp to data")

#Add a timestamp to all this data
records = add_timestamp(records)

print(f"Saving {len(records)} records to CSV")
logging.info(f"Saving {len(records)} records to CSV")
save_to_csv(records, BASE_DIR)


timestamp = datetime.now().isoformat()
print(f"Run completed at {timestamp}")
logging.info(f"Run completed at {timestamp}")


