#!/bin/bash


Msize=2,3
Nsize=3,2
Xsize=2,2



hadoop jar ./hadoop-streaming-3.1.4.jar \
-D stream.map.output.field.separator="\t" \
-D stream.num.map.output.key.fields=2 \
-D mapred.text.key.partitioner.options=-k1,2 \
-D mapred.reduce.tasks=3 \
-file ./mapper.py \
-mapper "./mapper.py $Msize $Nsize $Xsize" \
-file ./reducer.py \
-reducer ./reducer.py \
-input /matrices \
-output /outputA3 \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

