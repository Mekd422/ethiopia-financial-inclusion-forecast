# Forecasting Financial Inclusion in Ethiopia

Build a forecasting system that tracks Ethiopia's digital financial transformation using time series methods.

## Project Overview

This project develops a forecasting system to predict Ethiopia's progress on two core dimensions of financial inclusion as defined by the World Bank's Global Findex:

- **Access** — Account Ownership Rate
- **Usage** — Digital Payment Adoption Rate

## Project Structure

```
ethiopia-fi-forecast/
├── .github/workflows/
│   └── unittests.yml
├── data/
│   ├── raw/                      # Starter dataset
│   │   ├── ethiopia_fi_unified_data.csv
│   │   └── reference_codes.csv
│   └── processed/                # Analysis-ready data
├── notebooks/
│   └── README.md
├── src/
│   ├── __init__.py
├── dashboard/
│   └── app.py
├── tests/
│   └── __init__.py
├── models/
├── reports/
│   └── figures/
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Data

Place the starter dataset files in `data/raw/`:
- `ethiopia_fi_unified_data.csv`
- `reference_codes.csv`

## Tasks

- [x] Task 1: Data Exploration and Enrichment
- [x] Task 2: Exploratory Data Analysis
- [ ] Task 3: Event Impact Modeling
- [ ] Task 4: Forecasting Access and Usage
- [ ] Task 5: Dashboard Development

## Running the Dashboard

```bash
streamlit run dashboard/app.py
```

## Key Dates

- Interim Submission: 8:00 PM UTC on Sunday, 01 Feb 2026
- Final Submission: 8:00 PM UTC on Tuesday, 03 Feb 2026
