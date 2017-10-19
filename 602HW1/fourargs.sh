#!/bin/sh
# Copyright 2017 Lijun Xiao ljxiao@bu.edu

g++ fourargs.cpp -o fourargs
fourargs one two 3 four five six 
fourargs one two 3 
python fourargs.py one two 3 four five six 
python fourargs.py one two 3 
