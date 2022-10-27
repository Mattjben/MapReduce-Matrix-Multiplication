# MapReduce-Matrix-Multiplication

Contained is a MapReduce program with python that is used to implement **X-MN** , where X , M and N are all matrices. 

INPUTS: (examples can be seen in matrices folder)
-  For each matrix, it should be represented in a txt file, where the 1st column specifies the matrix #, 2nd 
column specifies the row #, then the row of the matrix. 
- Each matrix file should be stored in a folder called matrices in the same directory as the mapper and reducer
- The size of each inputed matrix should also be added to the run file paramters 
 

Files:
hadoop-streaming-3.1.4.jar: hadoop streaming file 
report.pdf : Analysis of mapreduce performance on different number of reducers 
run.sh: run file needed to implement the code and specify inputs and outputs 
mapper.py: mapper code
reducer.py: reducer code

# HOW TO RUN: 

Source Code: 
 
    mapper.py
    reducer.py 
    run.sh
    
1. Remeber to delete or rename any /outputA3  file in the masternode working directory 

2. open the run.sh file and make sure Msize,Nsize,Xsize arguments correspond to (# of rows,# of columns) for each of the respective matrices used as inputs

2. for each task after uploading the code and data to the cluster master node with the correct hadoop-streaming-3.1.4.jar file, make sure 
each run rile is runnable (chmod +x run.sh) and execute each run file in the cluster master node (./run.sh).
