# Automated GitHub Repository Data Pipeline

## Author
Jack Norton
Student ID: jwn20


---

## Project Description
This project implements an automated data pipeline that fetches repository data from GitHub on a
regular basis. The pipeline collects multiple pages of results, extracts meaningful fields (like 
repository name, stars, forks, and language), and stores them in a structured CSV file. This 
allows for ongoing tracking of repository trends over time, which could be used for analysis of
popular Python education projects.

---

## API Documentation
- [GitHub REST API – Search Repositories](https://docs.github.com/en/rest/search?apiVersion=2022-11-28#search-repositories)

---

## Data Pipeline Goals
1. Fetch multiple pages of GitHub repository data based on the query `"python"`.  
2. Extract key fields from each repository:  `full_name`, `description`, `stars`, `forks`, `language`.  
3. Add a timestamp for each pipeline run to track when data was collected.  
4. Accumulate results into a CSV file, appending new rows for each run without overwriting existing data.  
5. Handle errors and exceptions gracefully, including HTTP failures and timeouts, and log issues for later review.

