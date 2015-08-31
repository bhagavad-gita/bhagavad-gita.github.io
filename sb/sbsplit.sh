#!/bin/sh
# for c in 01 02 03 04 05 06 07 08 09 10
for c in 05
do
	# CMD="./sbsplit.py raw/SB-Canto-$c-Raw.txt"
	CMD="./sbsplit.py $c"
	echo $CMD
	$CMD
done
