#Copyright 2017 Lijun Xiao ljxiao@bu.edu
Table="{:<6} {:<22} {:<22} {:<22}"
print(Table.format('Bytes','Largest Unsigned Int','Minimum Signed Int','Maximum Signed Int'))
i=1
while i<=8:
	print(Table.format(i, 2**(i*8)-1, -2**(i*8-1), 2**(i*8-1)-1))
	i=i+1