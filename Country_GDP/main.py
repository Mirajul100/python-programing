import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Country GDP" , layout="centered")

st.title("In search of Happiness")

option_x = st.selectbox("Select the data for the X-axis" , ("GDP" , "HAPPINESS" , "GENEROSITY"))
option_y = st.selectbox("Select the data for the Y-axis",("GDP" , "HAPPINESS" , "GENEROSITY"))

st.subheader(f"{option_x}and{option_y}")

df = pd.read_csv("Country_GDP/004 happy.csv")

match option_x:
    case"GDP":
        x = df["gdp"]
    case"HAPPINESS":
        x = df["happiness"]
    case"GENEROSITY":
        x = df["generosity"]

match option_y:
    case"GDP":
        y = df["gdp"]
    case"HAPPINESS":
        y = df["happiness"]
    case"GENEROSITY":
        y = df["generosity"]

figure = px.scatter(x=x , y=y , labels={"x": option_x , "y": option_y})
st.plotly_chart(figure)