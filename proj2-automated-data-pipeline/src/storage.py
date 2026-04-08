import pandas as pd
import os
from datetime import datetime


#Save data to csv file
def save_to_csv(records, BASE_DIR):
    df = pd.DataFrame(records)  #make datafram with json data
    
    #Path leading to where we want to store our data
    file_path = f"{BASE_DIR}/data/processed/github_repos.csv"
    
    #Make surre directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    #Append data without header if file already exists
    if os.path.exists(file_path):
        df.to_csv(file_path, mode='a', header=False, index=False)
    else:
        df.to_csv(file_path, index=False)


#Add a timestamp column to data for accumulating data over time
def add_timestamp(records):
    timestamp = datetime.now().isoformat()
    
    #Add the timestamp for all records obtained in this run
    for r in records:
        r['collected_at'] = timestamp

    return records

    
