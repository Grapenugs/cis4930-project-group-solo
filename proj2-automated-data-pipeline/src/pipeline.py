import logging
import os

from api_client import fetch_repos

#Create log directory if it does not exist
os.makedirs("../logs", exist_ok=True)

#Create log file if it doesnt exist, and log all messages to it
logging.basicConfig(
    filename = "../logs/pipeline.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)


logging.info("Starting pipeline run")

repos = fetch_repos()

logging.info(f"Fetched {len(repos)} repositories")

print(len(repos))

