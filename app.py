import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#data = pd.read_csv(r'data/github_dataset.csv')

data = pd.read_csv('data/github_dataset.csv')


data = data.rename(columns={
    'stars_count': 'Stars Count',
    'forks_count': 'Forks Count',
    'issues_count': 'Issues Count',
    'pull_requests': 'Pull Requests',
    'contributors': 'Contributors',
    'language': 'Language',
    'repositories': 'Repositories'})

st.header("Top 5 Rows of the GitHub Dataset")
st.dataframe(data.head().reset_index(drop=True))

st.header("Repositories by Programming Language")
st.bar_chart(data['Language'].value_counts())

st.header("Relationship Between Stars and Forks of GitHub Repositories")
fig, ax = plt.subplots()
ax.scatter(data['Stars Count'], data['Forks Count'])
ax.set_xlabel('Stars Count')
ax.set_ylabel('Forks Count')
ax.set_title('Stars vs Forks')
st.pyplot(fig)

st.subheader("Filter Repositories by Programming Language")
languages = data['Language'].dropna().unique()
if 'Python' in languages:
    default_index = list(languages).index('Python')
else:
    default_index = 0
language = st.selectbox('Select Language', languages, index=default_index)
filtered_data = data[data['Language'] == language]
st.write(f"Showing repositories for: {language}")
st.dataframe(filtered_data.reset_index(drop=True))