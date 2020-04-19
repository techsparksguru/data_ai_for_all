# Why is Pandas taking so much RAM
The recommended RAM size for pandas is generally 5 to 10 times the size of the dataset. That said, pandas engine is not the best compared to Arrow, Spark and others that are built keeping distributed systems in mind. Factors that could affect memory needs are data types, all possible statistical aggregations on the data types, lack of distributed system design and so on. Also pandas prefers immutability when performing operations on input data i.e. input data is not modified after the operation.
However , since Pandas gets someone quickly started with analyzing data, without the overhead of setting up a server, following all bells and whistles and cuts straight to the need, it is still preferred by many especially because developers have access to higher horse power machines on the client side

# Pandas vs. Spark vs. Koalas
Pandas is great for data analysis, quick and no hassle to get started
Apache Spark is the defacto (along with hadoop) for big data processing
Koalas helps write Pandas aligned code, but runs on Apache Spark server (trying to get the best of both worlds, though still in early stages)

# Various links

- [Pandas To Apache Spark DataFrame](https://ogirardot.wordpress.com/2015/07/31/from-pandas-to-apache-sparks-dataframe/)
- [Pandarize your Spark DataFrame](https://lab.getbase.com/pandarize-spark-dataframes/)