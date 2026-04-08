import requests
import logging
    
BASE_URL = "https://api.github.com/search/repositories"


def fetch_repos_page(query="python", page=1, per_page=30):
    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": per_page,
        "page": page
    }
    
    #Retry once if Timeout
    for attempt in range(2):
        try:
            response = requests.get(BASE_URL, params=params, timeout = 10)
            print(f"Status: {response.status_code}")
            logging.info(f"Status: {response.status_code}")
            response.raise_for_status() #Raises any exceptions for me

            data = response.json()  #Get the data as json object
            return data.get('items', [])    #safely try to access data, default []
        
        except requests.exceptions.Timeout:
            print(f"Request timed out on page: {page}.")
            logging.error(f"Request timed out on page {page}.")
            if attempt < 1:
                print("Retrying...")
                logging.error("Retrying...")

        except requests.exceptions.RequestException as e:
            print(f"Request error on page: {page}, Error:", e)
            logging.error(f"Request error on page: {page}, Error:", e)
            return []
    
    return []


#fetch pages from 1 to max_pages.
def fetch_repos(query="python", max_pages=3):
    repos = []

    for page in range(1, max_pages+1):
        print(f"Fetching page {page}")
        logging.info(f"Fetching page {page}")
        
        items = fetch_repos_page(query=query, page=page)
        if not items:
            break

        print(f"Page {page} fetched, {len(items)} records")
        logging.info(f"Page {page} fetched, {len(items)} records")


        repos.extend(items)
    return repos

