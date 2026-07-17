# Write-up: Trader Performance vs Market Sentiment

## Methodology

Two datasets were joined at the daily level: Hyperliquid trade-level 
data (`historical_data.csv`) and Bitcoin Fear/Greed sentiment 
classification (`fear_greed_index.csv`). Trade timestamps were parsed 
and reduced to a `date` field, then left-joined against sentiment on 
that date — sentiment data (2018–2025) fully covered the trades date 
range (2023–2025), so the join was clean with no meaningful match loss.

Trades were aggregated into daily per-account metrics: daily PnL, win 
rate, number of trades, average trade size (USD), and long/short 
position ratio. A drawdown proxy was built as cumulative PnL minus its 
running maximum, per account.

Three behavioral segments were built by splitting accounts at the 
median: trade frequency (Frequent/Infrequent), win consistency 
(Consistent Winner/Inconsistent), and position size (Large/Small) — the 
last used in place of a leverage-based segment, since leverage data was 
not available in this dataset.

## Insights

1. **Tail risk is worst during Greed, not Fear.** The largest single-day 
   loss in the dataset (~-350,000) and the deepest drawdowns 
   (~-360,000) both occurred during Greed. Extreme Fear and Fear showed 
   comparatively contained downside (worst outliers around -100,000), 
   contradicting the assumption that fear-driven markets carry more risk.

2. **Long/short bias inverts sharply across the sentiment spectrum.** 
   Median long ratio falls from ~1.0 in Extreme Fear to ~0.33 in Greed 
   — traders go long during fear and short during greed, the clearest 
   behavioral signal in the data.

3. **Position size is the strongest performance differentiator.** 
   Large-size traders outperformed small-size traders in every 
   sentiment category, with the widest gap during Fear (8,383 vs 2,993 
   average daily PnL) and Greed (5,415 vs 1,383). The gap nearly closed 
   only during Extreme Fear.

## Strategy Recommendations

1. **Reduce position size and trade frequency during Greed, especially 
   for frequent traders.** Greed shows the deepest drawdowns and worst 
   PnL outliers, and Infrequent traders significantly outperformed 
   Frequent traders during Greed specifically (6,663 vs 2,293 average 
   daily PnL). Greed periods appear to reward selectivity over activity.

2. **Maintain or increase position size during Fear, particularly for 
   larger-size traders.** Large-size traders showed their biggest edge 
   over small-size traders during Fear, and Fear/Extreme Fear showed 
   the most contained downside risk of any sentiment category — running 
   counter to the instinct to de-risk during fear.

## Bonus: Predictive Model

A logistic regression predicted whether an account would be profitable 
the next day, using trade frequency, average trade size, win rate, long 
ratio, and sentiment classification as features.

- **Baseline (always predict "profitable")**: 67.6% accuracy
- **Model accuracy**: 66.2% — essentially matching baseline
- **Class-level performance**: the model correctly identified 84% of 
  profitable days but only 29% of unprofitable days — weakest exactly 
  where prediction would be most useful (flagging risk in advance)

**Interpretation**: The selected features do not carry strong signal 
for next-day profitability beyond the base rate. With only 32 accounts 
and daily-level aggregation, this is a reasonable outcome given the 
limited sample size — a larger dataset or richer features (multi-day 
rolling history, account-level trends) would likely be needed for a 
genuinely predictive model. This is reported as an honest, inconclusive 
finding rather than overstated.

## Bonus: Interactive Dashboard

A lightweight Streamlit dashboard (`dashboard.py`) was built to explore 
results interactively — filterable by sentiment and account, showing 
PnL, win rate, and long ratio distributions alongside the underlying 
data table. Run via `streamlit run dashboard.py`.

## Limitations

- **Leverage** was not available in the dataset. `Crossed` margin mode 
  (53.1% Cross / 46.9% Isolated) and position size (Size USD) were used 
  as partial proxies where relevant.
- **Sample size** is small (32 accounts), so segment-level findings — 
  particularly "Consistent Winners" (n=3) — should be interpreted 
  directionally rather than as statistically robust conclusions.