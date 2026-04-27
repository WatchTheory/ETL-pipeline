# ETL Pipeline

**A lightweight, modular ETL pipeline for processing resume data**

---

## Overview

This project is a **basic ETL (Extract, Transform, Load) pipeline** designed 
to automate the ingestion, cleaning and storage or resume data. It was built to get a functional pipeline up in quickly


## Architecture
```python
resume-pipeline/
├── requirements.txt      # Python dependencies
├── main.py               # <--- This is the only file you run
├── config.py             # All paths, URLs, settings in one place
├── extract.py            # Pull raw data (API, files, DB, etc)
├── transform.py          # Cleaning, enrichement resume
├── load.py               # Writes to database or file
└── logs/                 # Pipeline run logs
```



### Installation 
1. Clone the Repository
```python
# Clone the repository
git clone 
cd ETL_pipeline

# Install uv if you haven't already
# macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows 
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
2. Create a virtual environment
```python
uv venv

# macOS and Linux
source venv/bin/activate
```
3. Run the pipeline
```python
uv run main.py
```


## Next Steps
1. Add logging and error handling for errors.
2. Write to csv files.
3. Parse PDF. 
4. Scale up the pipeline for the cloud.