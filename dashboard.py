import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Trader Sentiment Dashboard", layout="wide")

st.title("Trader Performance vs Market Sentiment")

df = pd.read_csv('outputs/daily_metrics_processed.csv')

st.sidebar.header("Filters")
sentiments = st.sidebar.multiselect(
    "Select Sentiment(s)",
    options=df['Classification'].unique(),
    default=list(df['Classification'].unique())
)
accounts = st.sidebar.multiselect(
    "Select Account(s) (optional)",
    options=df['Account'].unique(),
    default=[]
)

filtered = df[df['Classification'].isin(sentiments)]
if accounts:
    filtered = filtered[filtered['Account'].isin(accounts)]

col1, col2, col3, col4 = st.columns(4)
col1.metric("Avg Daily PnL", f"{filtered['daily_pnl'].mean():,.2f}")
col2.metric("Avg Win Rate", f"{filtered['win_rate'].mean():.2%}")
col3.metric("Avg Trades/Day", f"{filtered['num_trades'].mean():.1f}")
col4.metric("Avg Long Ratio", f"{filtered['long_ratio'].mean():.2%}")

st.divider()

st.subheader("Daily PnL by Sentiment")
fig1, ax1 = plt.subplots()
filtered.boxplot(column='daily_pnl', by='Classification', ax=ax1)
plt.title('')
plt.suptitle('')
st.pyplot(fig1)


st.subheader("Win Rate by Sentiment")
fig2, ax2 = plt.subplots()
filtered.boxplot(column='win_rate', by='Classification', ax=ax2)
plt.title('')
plt.suptitle('')
st.pyplot(fig2)

st.subheader("Long Position Ratio by Sentiment")
fig3, ax3 = plt.subplots()
filtered.boxplot(column='long_ratio', by='Classification', ax=ax3)
plt.title('')
plt.suptitle('')
st.pyplot(fig3)

st.subheader("Underlying Data")
st.dataframe(filtered)