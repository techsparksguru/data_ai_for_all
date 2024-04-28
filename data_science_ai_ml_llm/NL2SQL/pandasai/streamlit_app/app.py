from dotenv import load_dotenv
import streamlit as st
import pandas as pd
from langchain_anthropic import ChatAnthropic
from pandasai import SmartDataframe

load_dotenv()

st.title("Data visualization with PandasAI and ChatAnthropic API")

data = pd.read_parquet("../Real_Estate_Sales_2001-2017.parquet")
st.write(data.head(5))

model = ChatAnthropic(model="claude-3-haiku-20240307")
sdf = SmartDataframe(data, config={"llm": model})

prompt = st.text_area("Enter your prompt:", value="Examples: 1. How many homes are there in each town?\n2.How many homes are in Andover town whose sale price is greater than the average sales price of all homes?\n3.Plot a vertical bar graph of top 25 towns in decreasing order of total sale prices,using different colors for each bar.")

if st.button("Generate:"):
    if prompt:
        with st.spinner("Generating response..."):
            response = sdf.chat(prompt)
            if "png" in response:
                st.write(st.image(response))
            else:
                st.write(response)