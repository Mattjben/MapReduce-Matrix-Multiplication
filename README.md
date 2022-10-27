# MapReduce-Matrix-Multiplication
# HOW TO RUN: 

Source Code: 
 
    mapper.py
    reducer.py 
    run.sh
    
1. Remeber to delete or rename any /outputA3  file in the masternode working directory 

2. open the run.sh file and make sure Msize,Nsize,Xsize arguments correspond to (# of rows,# of columns) for each of the respective matrices used as inputs

2. for each task after uploading the code and data to the cluster master node with the correct hadoop-streaming-3.1.4.jar file, make sure 
each run rile is runnable (chmod +x run.sh) and execute each run file in the cluster master node (./run.sh).
