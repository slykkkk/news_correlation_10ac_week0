import os

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# Load data
rating_df = pd.read_csv("./data/rating.csv")
domain_locations_df = pd.read_csv("./data/domains_location.csv")
traffic_data_df = pd.read_csv("./data/traffic.csv")

# Title with custom color and font size
st.title("🌎 Global News Analytics Dashboard")
st.markdown("---")

# Sidebar with custom color and font size
st.sidebar.title("🚀 Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "🔍 EDA", "😊 Sentiment Analysis", "📰 Topic Modeling"])

# Page Content
if page == "🏠 Home":
    # Colorful introduction
    st.header("Welcome to the Global News Analytics Dashboard")
    st.write("Explore insights and trends in global news data.")
    st.markdown("---")
    st.write("This dashboard provides a comprehensive analysis of global news data, including article counts by source, website traffic distribution, sentiment analysis, and more. Use the navigation on the left to explore different sections.")
    st.write("Get started by selecting a section from the sidebar on the left.")
    st.markdown("---")
    
elif page == "🔍 EDA":
    # Exploratory Data Analysis
    st.header("🔍 Exploratory Data Analysis")
    st.subheader("Top 10 Websites")
    top_10_websites = rating_df['source_name'].value_counts().head(10)
    st.bar_chart(top_10_websites, use_container_width=True)

    st.subheader("Article Counts by Source")
    article_counts_by_source = rating_df['source_name'].value_counts()
    st.bar_chart(article_counts_by_source.head(10), use_container_width=True)

    st.subheader("Website Traffic Distribution")
    st.write("This histogram displays the distribution of website traffic ranks.")
    plt.hist(traffic_data_df['GlobalRank'], bins=30)
    st.pyplot()

elif page == "😊 Sentiment Analysis":
    # Sentiment Analysis
    st.header("😊 Sentiment Analysis")
    sentiment_counts = rating_df['title_sentiment'].value_counts()
    st.bar_chart(sentiment_counts, use_container_width=True)
    st.write("This bar chart illustrates the distribution of sentiment categories.")

elif page == "📰 Topic Modeling":
    # Topic Modeling
    st.header("📰 Topic Modeling")
    st.write("Include your topic modeling visualizations here")
