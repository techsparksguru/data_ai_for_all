# PandasAI
- PandasAI is a Python library that makes it easy to ask questions to your data (CSV, XLSX, PostgreSQL, MySQL, BigQuery, Databrick, Snowflake, etc.) in natural language. xIt helps you to explore, clean, and analyze your data using generative AI.
- Beyond querying, PandasAI offers functionalities to visualize data through graphs, cleanse datasets by addressing missing values, and enhance data quality through feature generation, making it a comprehensive tool for data scientists and analysts.

# Features

- Natural language querying: Ask questions to your data in natural language.
- Data visualization: Generate graphs and charts to visualize your data.
- Data cleansing: Cleanse datasets by addressing missing values.
- Feature generation: Enhance data quality through feature generation.
- Data connectors: Connect to various data sources like CSV, XLSX, PostgreSQL, MySQL, BigQuery, Databrick, Snowflake, etc.

# How does PandasAI work?
PandasAI uses a generative AI model to understand and interpret natural language queries and translate them into python code and SQL queries. It then uses the code to interact with the data and return the results to the user.

# Installation

```
# Using poetry (recommended)
poetry add pandasai

# Using pip
pip install pandasai
```

## Optional dependencies

In order to keep the installation size small, pandasai does not include all the dependencies that it supports by default. You can install the extra dependencies by running the following command:

pip install pandasai[extra-dependency-name]

You can replace extra-dependency-name with any of the following:

- google-ai: this extra dependency is required if you want to use Google PaLM as a language model.
- google-sheet: this extra dependency is required if you want to use Google Sheets as a data source.
- excel: this extra dependency is required if you want to use Excel files as a data source.
- modin: this extra dependency is required if you want to use Modin dataframes as a data source.
- polars: this extra dependency is required if you want to use Polars dataframes as a data source.
- langchain: this extra dependency is required if you want to support the LangChain LLMs.
- numpy: this extra dependency is required if you want to support numpy.
- ggplot: this extra dependency is required if you want to support ggplot for plotting.
- seaborn: this extra dependency is required if you want to support seaborn for plotting.
- plotly: this extra dependency is required if you want to support plotly for plotting.
- statsmodels: this extra dependency is required if you want to support statsmodels.
- scikit-learn: this extra dependency is required if you want to support scikit-learn.
- streamlit: this extra dependency is required if you want to support streamlit.
- ibm-watsonx-ai: this extra dependency is required if you want to use IBM watsonx.ai as a language model


# Concepts

CONTINUE [HERE][./CONCEPTS.md]
