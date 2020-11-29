# Compaction
- Compaction is a balance between # of files vs. size of each file relative to the storage for your dataset
- Too many files (partitions) is not good because you will end up spending time opening and closing files
- Too large size of of a partition (file) is also not good  

How do we determine a good balance ?

# Why does compaction occur

An example would be based on the rate of streaming data (from an upstream application) and the rate at which data is flushed to disk by the consuming application. If the rate of data received into an application is sub-optimal compared with how frequently the application writes out to storage. It can also be the result of incremental updates into a table partition

# How do we find a balance

Apache spark uses it # of partitions setting to optimize its performance. How do we then determine right # of partitions setting for apache spark cluster (server side setting) ?  

- By default Apache spark will use all available cores to process partitions in parallel. So for e.g. if we have an 8 core CPU, if partitions are 4, then CPU cores are underutilized. Likewise for 8 core CPU, if we have 10k partitions, too much time is spent assigning tasks than executing tasks.  

- There are lots of benchmarking exercises done to identify CPU core to partition balance. **It is an industry guidance to have partitions approx. 1x-3x of CPU cores.** So if we have 8 core CPU, then having a partition size anywhere between 8 to 24 (16 would be good to start with and then adjust up or down)

- It is also helpful to not overly partition your data. Shallow and wide is a better strategy for storage of compacted files rather than deep and narrow.

# Gotchas

- The 1x-3x rule applies well when our apache spark cluster manages all CPU cores and controls the data layer as well
- But what about data lakes / data swamps (especially in an enterprise setting) where data is dumped and it is left to the reading processes to determine how they want to use the data
- In the case of Hadoop (hdfs), by default the block size is 128MB (how is 128mb determined. Please read hadoop documentation. There is a certain hardware on which 128mb applies). A block in HDFS is one co-located group of data. So it is faster (I/O time) to read data from one block, than multiple blocks. 
- **So the best practice is to write out data to data lake based on its block size**

## Optimal file size for HDFS
- In the case of HDFS, the ideal file size is that which is as close to the configured blocksize value as possible (dfs.blocksize), often set as default to 128MB.
- Avoid file sizes that are smaller than the configured block size. An average size below the recommended size adds more burden to the NameNode, cause heap/GC issues in addition to cause storage and processing to be inefficient.
Larger files than the blocksize are potentially wasteful. e.g. Creating files of 130MB would mean that file extend over 2 blocks, which carries additional I/O time.

## Optimal file size for S3
- For S3, there is a configuration parameter we can refer to — fs.s3a.block.size — however this is not the full story. File listing performance from S3 is slow, therefore an opinion exists to optimise for a larger file size. 1GB is a widely used default, although you can feasibly go up to the 4GB file maximum before splitting.
- The penalty for handling larger files is that processes such as Spark will partition based on files — if you have more cores available than partitions, they will be idle. 2x1GB files in a partition can only be operated on by 2 cores simultaneously, whereas 16 files of 128MB could be processed by 16 cores in parallel.

## An Example Solution
- Get the size of directory (with large # of files)
- Get the block size (For hadoop it is 128MB default)
- Get repartition factor (size of directory / block size)
- Read all files into a dataframe
- Apply repartition with repartition factor and write out the files back to disk 

``` python
def get_repartition_factor(dir_size):
    block_size = sc._jsc.hadoopConfiguration().get(“dfs.blocksize”)
    return math.ceil(dir_size/block_size) # returns 2
df=spark.read.parquet(“/path/to/source”)
df.repartition(get_repartition_factor(217894092)) 
.write
.parquet("/path/to/output")
```  

# Conclusion
- For maintaining optimal read performance and reducing metadata management overheads, compaction boosts performance by leaps
- With a minor development effort, a crawler process could be created to incrementally walk through all tables and their partitions in a datalake — pulling total size of each directory and calculating the ideal number of files in comparison to the storage block size — taking action if the composition is not optimal

# References
[Compaction/Merge of parquet files](https://medium.com/@chrisfinlayson_83750/compaction-merge-of-small-parquet-files-bef60847e60b)
[Spark+Data Compaction](https://medium.com/@fqaiser94/spark-data-compaction-ec9dee8712f9)