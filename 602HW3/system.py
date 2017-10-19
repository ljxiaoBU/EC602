#Copyright 2017 Lijun Xiao ljxiao@bu.edu
import numpy as np

x=input()
h=input()

x=np.fromstring(x, dtype=float, sep=" ")
h=np.fromstring(h, dtype=float, sep=" ")


y=np.convolve(x,h)
print(" ".join(str(i) for i in y))



