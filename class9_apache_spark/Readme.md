# Apache Spark Features

![Spark Features](./images/apache_spark_features.png)

# General Knowledge

- Spark is written in Scala and executed on JVM
- Spark interactive consoles can be launched via `./bin/pyspark` (and then type `spark` for SparkSession) OR `./bin/spark-shell` for scala OR `./bin/spark-sql` for SQL console

# Spark Application
Spark Applications consist of a driver process and a set of executor processes. There is a one-to-one correspondence between a SparkSession and a Spark Application  

![Spark Application](./images/spark_application.png)

### Driver Process
The driver process runs your main() function, sits on a node in the cluster, and is responsible for three things: maintaining information about the Spark Application; responding to a user’s program or input; and analyzing, distributing, and scheduling work across the executors.

### Executor Process
The executors are responsible for actually carrying out the work that the driver assigns them. This means that each executor is responsible for only two things: executing code assigned to it by the driver, and reporting the state of the computation on that executor back to the driver node

### Local Mode
Spark, in addition to its cluster mode, also has a local mode. The driver and executors are simply processes, which means that they can live on the same machine or different machines. In local mode, the driver and executurs run (as threads) on your individual computer instead of a cluster.

### Interative vs. Standalone
When you start Spark in this interactive mode, you implicitly create a SparkSession that manages the Spark Application. When you start it through a standalone application (spark-submit), you must create the SparkSession object yourself in your application code.


# Spark Partitions
- To allow every executor to perform work in parallel, Spark breaks up the data into chunks called partitions. A partition is a collection of rows that sit on one physical machine in your cluster. A DataFrame’s partitions represent how the data is physically distributed across the cluster of machines during execution. 
- If you have one partition, Spark will have a parallelism of only one, even if you have thousands of executors. 
- If you have many partitions but only one executor, Spark will still have a parallelism of only one because there is only one computation resource
- An important thing to note is that with DataFrames you do not (for the most part) manipulate partitions manually or individually

# Spark UI
- Generally available on port 4040 of driver node