#Copyright 2017 Lijun Xiao ljxiao@bu.edu
earthmass=5.972*(10**24)*1000
atomspermole=6.022*(10**23)
	
electronsperatom=14

gramspermole=28.08

electronsnumber=earthmass/gramspermole*atomspermole*electronsperatom

estimate=electronsnumber/(2**43)

lower=estimate*0.9

upper=estimate*1.1

print(estimate)

print(lower)

print(upper)