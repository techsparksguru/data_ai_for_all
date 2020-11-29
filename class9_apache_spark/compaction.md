# Compaction
- Compaction is a balance between # of files vs. size of each file relative to the storage for your dataset
- Too many files (partitions) is not good because you will end up spending time opening and closing files
- Too large size of of a partition (file) is also not good  

How do we determine a good balance ?

# Why does compaction occur

An example would be based on the rate of streaming data (from an upstream application) and the rate at which data is flushed to disk by the consuming application

# How do we find a balance

Apache spark uses it # of partitions setting to optimize its performance. How do we then determine right # of partitions setting for apache spark cluster (server side setting) ?  

- By default Apache spark will use all available cores to process partitions in parallel. So for e.g. if we have an 8 core CPU, if partitions are 4, then CPU cores are underutilized. Likewise for 8 core CPU, if we have 10k partitions, too much time is spent assigning tasks than executing tasks.  

- There are lots of benchmarking exercises done to identify CPU core to partition balance. **It is an industry guidance to have partitions approx. 1x-3x of CPU cores.** So if we have 8 core CPU, then having a partition size anywhere between 8 to 24 (16 would be good to start with and then adjust up or down)

# Gotchas

- The 1x-3x rule applies well when our apache spark cluster manages all CPU cores and controls the data layer as well
- But what about data lakes / data swamps (especially in an enterprise setting) where data is dumped and it is left to the reading processes to determine how they want to use the data
- In the case of Hadoop (hdfs), by default the block size is 128MB (how is 128mb determined. Please read hadoop documentation. There is a certain hardware on which 128mb applies). A block in HDFS is one co-located group of data. So it is faster (I/O time) to read data from one block, than multiple blocks. 
- **So the best practice is to write out data to data lake based on its block size**