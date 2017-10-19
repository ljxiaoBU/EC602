# Copyright 2017 Lijun Xiao ljxiao@bu.edu
import sys
l=len(sys.argv)
if l<=5:
	for i in range(1,l):
		print(sys.argv[i])
else:
	for i in range(1,5):
		print(sys.argv[i])
	for i in range(5,l):
		print(sys.argv[i],file=sys.stderr)