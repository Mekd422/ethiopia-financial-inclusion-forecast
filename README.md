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
- [x] Task 3: Event Impact Modeling
- [x] Task 4: Forecasting Access and Usage
- [x] Task 5: Dashboard Development

## Running the Dashboard

The interactive dashboard provides comprehensive visualization and analysis of Ethiopia's financial inclusion data.

### Prerequisites

1. Ensure data files are in `data/raw/`:
   - `ethiopia_fi_unified_data.csv`
   - `reference_codes.csv`

2. Install dependencies (if not already done):
   ```bash
   pip install -r requirements.txt
   ```

### Starting the Dashboard

From the project root directory, run:

```bash
streamlit run dashboard/app.py
```

The dashboard will open in your default web browser at `http://localhost:8501`

### Dashboard Features

The dashboard includes four main pages:

1. **Overview Page**
   - Key metrics summary cards (current values, trends)
   - P2P/ATM Crossover Ratio indicator
   - Growth rate highlights

2. **Trends Page**
   - Interactive time series plots
   - Date range selector
   - Channel comparison view (Account Ownership vs Mobile Money)

3. **Forecasts Page**
   - Forecast visualizations with confidence intervals
   - Model selection (Baseline Trend, Event-Augmented, Scenario Analysis)
   - Key projected milestones
   - Forecast tables

4. **Inclusion Projections Page**
   - Financial inclusion rate projections
   - Progress toward 60% target visualization
   - Scenario selector (Optimistic/Base/Pessimistic)
   - Answers to consortium's key questions
   - Data download functionality

### Interactive Features

- **At least 4 interactive visualizations** using Plotly
- **Clear labels and explanations** for all metrics
- **Data download functionality** for forecast tables
- **Scenario analysis** with optimistic, base, and pessimistic projections

## Key Dates

- Interim Submission: 8:00 PM UTC on Sunday, 01 Feb 2026
- Final Submission: 8:00 PM UTC on Tuesday, 03 Feb 2026
