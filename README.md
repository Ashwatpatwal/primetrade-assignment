# Trader Performance vs Market Sentiment

Analysis of how Bitcoin market sentiment (Fear/Greed) relates to trader 
behavior and performance on Hyperliquid.

## Setup

1. Clone this repo
2. Install dependencies:
    pip install -r requirements.txt
3. Data files should be in `data/` (already included):
   - `fear_greed_index.csv`
   - `historical_data.csv`

## How to run

**Notebook (main analysis):**
Open `notebooks/analysis.ipynb` in VS Code or Jupyter and run all cells 
top to bottom. This performs data cleaning, date alignment, metric 
building, Fear/Greed comparison, segmentation, and the bonus predictive 
model.

**Dashboard:**
    streamlit run dashboard.py
    This opens an interactive dashboard at `localhost:8501` to explore 
    results by sentiment and account.

## Project structure
├── data/                # raw input CSVs
│   ├── fear_greed_index.csv
│   └── historical_data.csv
├── notebooks/
│   └── analysis.ipynb   # main analysis notebook
├── outputs/              # saved charts and processed data
├── dashboard.py          # Streamlit dashboard
├── requirements.txt
├── README.md             # this file
└── WRITEUP.md            # methodology, insights, strategy recommendations

## Summary

Two datasets were joined on date: Hyperliquid trade-level data and 
Bitcoin Fear/Greed sentiment classification. Trades were aggregated to 
daily per-account metrics (PnL, win rate, trade frequency, position 
size, long/short ratio), compared across sentiment categories, and 
broken into behavioral segments. A simple predictive model and 
interactive dashboard were built as bonus extensions.

See **[WRITEUP.md](./WRITEUP.md)** for full findings, insights, and 
strategy recommendations.

Also create requirements.txt at root with:
pandas
matplotlib
scikit-learn
scipy
streamlit
numpy