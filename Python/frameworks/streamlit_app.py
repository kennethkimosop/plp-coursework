# If you get import errors, run these commands in your terminal:
# pip install streamlit pandas matplotlib seaborn

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("CORD-19 Data Explorer")
st.write("Exploring metadata of COVID-19 research papers")

@st.cache_data
def load_data():
    df = pd.read_csv("metadata.csv", nrows=5000)   # just first 5000 rows
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    return df

df = load_data()

# Year filter
years = st.slider("Select year range:", int(df['year'].min()), int(df['year'].max()), (2020, 2021))
filtered = df[(df['year'] >= years[0]) & (df['year'] <= years[1])]

st.write(f"Showing {len(filtered)} papers")

# Visualization
year_counts = filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
sns.barplot(x=year_counts.index, y=year_counts.values, ax=ax)
st.pyplot(fig)

# Show top journals
st.write("Top 10 Journals:")
st.write(filtered['journal'].value_counts().head(10))
