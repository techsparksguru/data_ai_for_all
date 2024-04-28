# SmartDataframe

The SmartDataframe class is the main class of pandasai. It is used to interact with a single dataframe

```
import os
import pandas as pd
from pandasai import SmartDataframe

# Sample DataFrame
sales_by_country = pd.DataFrame({
    "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
    "sales": [5000, 3200, 2900, 4100, 2300, 2100, 2500, 2600, 4500, 7000]
})

# By default, unless you choose a different LLM, it will use BambooLLM.
# You can get your free API key signing up at https://pandabi.ai (you can also configure it in your .env file)
os.environ["PANDASAI_API_KEY"] = "YOUR_API_KEY"

df = SmartDataframe(sales_by_country)
df.chat('Which are the top 5 countries by sales?')
# Output: China, United States, Japan, Germany, Australia
```  

## Passing name and description for a dataframe

Sometimes, in order to help the LLM to work better, you might want to pass a name and a description of the dataframe. You can do this as follows: 
`df = SmartDataframe(df, name="My DataFrame", description="Brief description of what the dataframe contains")
`

# SmartDatalake

PandasAI also supports queries with multiple dataframes. To perform such queries, you can use a SmartDatalake instead of a SmartDataframe

```
import os
import pandas as pd
from pandasai import SmartDatalake

employees_data = {
    'EmployeeID': [1, 2, 3, 4, 5],
    'Name': ['John', 'Emma', 'Liam', 'Olivia', 'William'],
    'Department': ['HR', 'Sales', 'IT', 'Marketing', 'Finance']
}

salaries_data = {
    'EmployeeID': [1, 2, 3, 4, 5],
    'Salary': [5000, 6000, 4500, 7000, 5500]
}

employees_df = pd.DataFrame(employees_data)
salaries_df = pd.DataFrame(salaries_data)

# By default, unless you choose a different LLM, it will use BambooLLM.
# You can get your free API key signing up at https://pandabi.ai (you can also configure it in your .env file)
os.environ["PANDASAI_API_KEY"] = "YOUR_API_KEY"

lake = SmartDatalake([employees_df, salaries_df])
lake.chat("Who gets paid the most?")
# Output: Olivia gets paid the most
```

# Agent

While a SmartDataframe or a SmartDatalake can be used to answer a single query and are meant to be used in a single session and for exploratory data analysis, an agent can be used for multi-turn conversations.
```
import os
from pandasai import Agent
import pandas as pd

# Sample DataFrames
sales_by_country = pd.DataFrame({
    "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
    "sales": [5000, 3200, 2900, 4100, 2300, 2100, 2500, 2600, 4500, 7000],
    "deals_opened": [142, 80, 70, 90, 60, 50, 40, 30, 110, 120],
    "deals_closed": [120, 70, 60, 80, 50, 40, 30, 20, 100, 110]
})


# By default, unless you choose a different LLM, it will use BambooLLM.
# You can get your free API key signing up at https://pandabi.ai (you can also configure it in your .env file)
os.environ["PANDASAI_API_KEY"] = "YOUR_API_KEY"

agent = Agent(sales_by_country)
agent.chat('Which are the top 5 countries by sales?')
# Output: China, United States, Japan, Germany, Australia
```

Contrary to a SmartDataframe or a SmartDatalake, an agent will keep track of the state of the conversation and will be able to answer multi-turn conversations

```
agent.chat('And which one has the most deals?')
# Output: United States has the most deals
```

## Clarification questions

An agent will also be able to ask clarification questions if it does not have enough information to answer the query

```
agent.clarification_question('What is the GDP of the United States?')
```
this will return up to 3 clarification questions that the agent can ask the user to get more information to answer the query.

## Explanation

An agent will also be able to explain the answer given to the user. For example:

```
response = agent.chat('What is the GDP of the United States?')
explanation = agent.explain()

print("The answer is", response)
print("The explanation is", explanation)
```

## Rephrase Question

Rephrase question to get accurate and comprehensive response from the model. For example:

```
rephrased_query = agent.rephrase_query('What is the GDP of the United States?')

print("The rephrased query is", rephrased_query)
```

# Config

To customize PandasAI's SmartDataframe, you can either pass a config object with specific settings upon instantiation or modify the pandasai.json file in your project's root. The latter serves as the default configuration but can be overridden by directly specifying settings in the config object at creation. This approach ensures flexibility and precision in how PandasAI handles your data.

## Settings:

- llm: the LLM to use. You can pass an instance of an LLM or the name of an LLM. You can use one of the LLMs supported. You can find more information about LLMs here.
- llm_options: the options to use for the LLM (for example the api token, etc). You can find more information about the settings here.
- save_logs: whether to save the logs of the LLM. Defaults to True. You will find the logs in the pandasai.log file in the root of your project.
- verbose: whether to print the logs in the console as PandasAI is executed. Defaults to False.
- enforce_privacy: whether to enforce privacy. Defaults to False. If set to True, PandasAI will not send any data to the LLM, but only the metadata. By default, PandasAI will send 5 samples that are anonymized to improve the accuracy of the results.
- save_charts: whether to save the charts generated by PandasAI. Defaults to False. You will find the charts in the root of your project or in the path specified by save_charts_path.
- save_charts_path: the path where to save the charts. Defaults to exports/charts/. You can use this setting to override the default path.
- open_charts: whether to open the chart during parsing of the response from the LLM. Defaults to True. You can completely disable displaying of charts by setting this option to False.
- enable_cache: whether to enable caching. Defaults to True. If set to True, PandasAI will cache the results of the LLM to improve the response time. If set to False, PandasAI will always call the LLM.
- use_error_correction_framework: whether to use the error correction framework. Defaults to True. If set to True, PandasAI will try to correct the errors in the code generated by the LLM with further calls to the LLM. If set to False, PandasAI will not try to correct the errors in the code generated by the LLM.
- max_retries: the maximum number of retries to use when using the error correction framework. Defaults to 3. You can use this setting to override the default number of retries.
- custom_whitelisted_dependencies: the custom whitelisted dependencies to use. Defaults to {}. You can use this setting to override the default custom whitelisted dependencies. You can find more information about custom whitelisted dependencies here.

# Connectors
PandasAI provides a number of connectors that allow you to connect to different data sources. These connectors are designed to be easy to use, even if you are not familiar with the data source or with PandasAI.

To use a connector, you first need to install the required dependencies. You can do this by running the following command:

```
# Using poetry (recommended)
poetry add pandasai[connectors]
# Using pip
pip install pandasai[connectors]
```
### SQL connectors

PandasAI provides connectors for the following SQL databases:

- PostgreSQL
- MySQL
- Generic SQL
- Snowflake
- DataBricks
- GoogleBigQuery
- Yahoo Finance
- Airtable

Additionally, PandasAI provides a generic SQL connector that can be used to connect to any SQL database.

### PostgreSQL connector

The PostgreSQL connector allows you to connect to a PostgreSQL database. It is designed to be easy to use, even if you are not familiar with PostgreSQL or with PandasAI.

To use the PostgreSQL connector, you only need to import it into your Python code and pass it to a SmartDataframe or SmartDatalake object:

```
from pandasai import SmartDataframe
from pandasai.connectors import PostgreSQLConnector

postgres_connector = PostgreSQLConnector(
    config={
        "host": "localhost",
        "port": 5432,
        "database": "mydb",
        "username": "root",
        "password": "root",
        "table": "payments",
        "where": [
            # this is optional and filters the data to
            # reduce the size of the dataframe
            ["payment_status", "=", "PAIDOFF"],
        ],
    }
)

df = SmartDataframe(postgres_connector)
df.chat('What is the total amount of payments in the last year?')
```

# Large language models (LLMs)

PandasAI supports several large language models (LLMs). LLMs are used to generate code from natural language queries. The generated code is then executed to produce the result.

You can either choose a LLM by instantiating one and passing it to the SmartDataFrame or SmartDatalake constructor, or you can specify one in the pandasai.json file.

If the model expects one or more parameters, you can pass them to the constructor or specify them in the pandasai.json file, in the llm_options param, as it follows:

```
{
  "llm": "BambooLLM",
  "llm_options": {
    "api_key": "API_KEY_GOES_HERE"
  }
}
```

## OpenAI models
from pandasai import SmartDataframe
from pandasai.llm import OpenAI

```
llm = OpenAI()  # no need to pass the API key, it will be read from the environment variable
pandas_ai = SmartDataframe("data.csv", config={"llm": llm})
```

### Count tokens

You can count the number of tokens used by a prompt as follows:

```
"""Example of using PandasAI with a pandas dataframe"""

from pandasai import SmartDataframe
from pandasai.llm import OpenAI
from pandasai.helpers.openai_info import get_openai_callback
import pandas as pd

llm = OpenAI()

# conversational=False is supposed to display lower usage and cost
df = SmartDataframe("data.csv", config={"llm": llm, "conversational": False})

with get_openai_callback() as cb:
    response = df.chat("Calculate the sum of the gdp of north american countries")

    print(response)
    print(cb)
#  The sum of the GDP of North American countries is 19,294,482,071,552.
#  Tokens Used: 375
#   Prompt Tokens: 210
#   Completion Tokens: 165
# Total Cost (USD): $ 0.000750
```

# [ADVANCED] Pipelines

Pipelines provide a way to chain together multiple processing steps (called Building Blocks) for different tasks. They allow you to customize and reuse logic by composing reusable steps.

PandasAI provides some core building blocks for creating pipelines as well as some predefined pipelines for common tasks. Pipelines can also be fully customized by injecting custom logic at each step.

### Core Pipeline Building Blocks

PandasAI provides the following core pipeline logic units that can be composed to build custom pipelines:

    Pipeline - The base pipeline class that allows chaining multiple logic units.
    BaseLogicUnit - The base class that all pipeline logic units inherit from. Each unit performs a specific task.

### Predefined Pipelines

PandasAI provides the following predefined pipelines that combine logic units:
GenerateChatPipeline

The GenerateChatPipeline generates new data in a Agent. It chains together logic units for:

- CacheLookup - Checking if data is cached
- PromptGeneration - Generating prompt
- CodeGenerator - Generating code from prompt
- CachePopulation - Caching generated data
- CodeExecution - Executing code
- ResultValidation - Validating execution result
- ResultParsing - Parsing result into data

Read more [here](https://docs.pandas-ai.com/en/stable/pipelines/pipelines/)

# MORE ADVANCED
## Cache

PandasAI uses a cache to store the results of previous queries. This is useful for two reasons:

- It allows the user to quickly retrieve the results of a query without having to wait for the model to generate a response.
- It cuts down on the number of API calls made to the model, reducing the cost of using the model.

The cache is stored in a file called cache.db in the /cache directory of the project. The cache is a SQLite database, and can be viewed using any SQLite client. The file will be created automatically when the first query is made.

- Disabling the cache
- Clearing the cache

Read more [here](https://docs.pandas-ai.com/en/stable/cache/)


## Use custom head

In some cases, you might want to share a custom sample head to the LLM. For example, you might not be willing to share potential sensitive information with the LLM. Or you might just want to provide better examples to the LLM to improve the quality of the answers. You can do so by passing a custom head to the LLM as follows:

```
from pandasai import SmartDataframe
import pandas as pd

# head df
head_df = pd.DataFrame({
    "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
    "gdp": [19294482071552, 2891615567872, 2411255037952, 3435817336832, 1745433788416, 1181205135360, 1607402389504, 1490967855104, 4380756541440, 14631844184064],
    "happiness_index": [6.94, 7.16, 6.66, 7.07, 6.38, 6.4, 7.23, 7.22, 5.87, 5.12]
})

df = SmartDataframe("data/country_gdp.csv", config={
    "custom_head": head_df
})
```

**Doing so will make the LLM use the head_df as the custom head instead of the first 5 rows of the dataframe.**

## Use custom field descriptions

The field_descriptions is a dictionary attribute of the BaseConnector class. It is used to provide additional information or descriptions about each individual field in the data source. This can be useful for providing context or explanations for the data in each field, especially when the field names themselves are not self-explanatory.

Read more [here](https://docs.pandas-ai.com/en/stable/fields-description/)

## Train with your own settings

You can train PandasAI to understand your data better and to improve its performance. Training is as easy as calling the train method on the SmartDataframe, SmartDatalake or Agent.

There are two kinds of training:

- instructions training
- q/a training


Read more [here](https://docs.pandas-ai.com/en/stable/train/).
**Heavily reliese on https://pandabi.ai and bamboovectorstore etc. For enterprise they let you use local chromadb / qdrant etc**

## Custom Response

For e.g. return StreamlitResponse

Read more [here](https://docs.pandas-ai.com/en/stable/custom-response/)

## Skills
For e.g. add streamlit skill. You can add customs functions for the agent to use, allowing the agent to expand its capabilities. These custom functions can be seamlessly integrated with the agent's skills, enabling a wide range of user-defined operations. Read more [here](https://docs.pandas-ai.com/en/stable/skills/)

# Determinism
## Introduction

In the realm of Language Model (LM) applications, determinism plays a crucial role, especially when consistent and predictable outcomes are desired. Our library, which integrates multiple LLMs including OpenAI's models, offers users the ability to control this aspect of model behavior through specific parameters like temperature and seed. This document aims to elucidate the importance of these parameters, their usage, and current limitations with different LLM instances such as AzureOpenAI.
## Why Determinism Matters

Determinism in language models refers to the ability to produce the same output consistently given the same input under identical conditions. This characteristic is vital for:

- Reproducibility: Ensuring the same results can be obtained across different runs, which is crucial for debugging and iterative development.
- Consistency: Maintaining uniformity in responses, particularly important in scenarios like automated customer support, where varied responses to the same query might be undesirable.
- Testing: Facilitating the evaluation and comparison of models or algorithms by providing a stable ground for testing.

## The Role of temperature=0

The temperature parameter in language models controls the randomness of the output. A higher temperature increases diversity and creativity in responses, while a lower temperature makes the model more predictable and conservative. Setting temperature=0 essentially turns off randomness, leading the model to choose the most likely next word at each step. This is critical for achieving determinism as it minimizes variance in the model's output.
Implications of temperature=0

- Predictable Responses: The model will consistently choose the most probable path, leading to high predictability in outputs.
- Creativity: The trade-off for predictability is reduced creativity and variation in responses, as the model won't explore less likely options.

## Utilizing seed for Enhanced Control

The seed parameter is another tool to enhance determinism. It sets the initial state for the random number generator used in the model, ensuring that the same sequence of "random" numbers is used for each run. This parameter, when combined with temperature=0, offers an even higher degree of predictability.

Read more [here](https://docs.pandas-ai.com/en/stable/determinism/)










