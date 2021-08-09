#! /bin/bash

read input

echo "Processing application : $input"

echo "Counting Misses for L2 and L3 Caches"

for policy in 1 2 3
do
	python3 simulator.py $input $policy
done
