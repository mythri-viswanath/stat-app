import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📊 Stat Graph + Interpretation App")

file = st.file_uploader("Upload your data (CSV)", type=["csv"])

if file is not None:
    data = pd.read_csv(file)

    st.write(data.head())

    col1 = st.selectbox("Select X", data.columns)
    col2 = st.selectbox("Select Y", data.columns)

    fig, ax = plt.subplots()
    sns.scatterplot(x=data[col1], y=data[col2], ax=ax)
    st.pyplot(fig)

    corr = data[col1].corr(data[col2])

    if corr > 0.7:
        st.write("Strong positive relationship")
    elif corr > 0.3:
        st.write("Moderate positive relationship")
    elif corr > 0:
        st.write("Weak positive relationship")
    elif corr < -0.7:
        st.write("Strong negative relationship")
    elif corr < -0.3:
        st.write("Moderate negative relationship")
    elif corr < 0:
        st.write("Weak negative relationship")
    else:
        st.write("No relationship")

    st.write("Correlation:", round(corr, 2))