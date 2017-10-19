#Copyright 2017 Lijun Xiao ljxiao@bu.edu
class Polynomial():
	def __init__(self, coeff1=[]):
		self.poly = {}
		for i in range(len(coeff1)):
			self.poly[i] = coeff1[len(coeff1)-i-1]
	def __add__(self, other):
		add = self.poly.copy()
		for i in other.poly.keys():
			if (add.get(i)==None):
				add[i] = other.poly[i]
			else:
				add[i] += other.poly[i]
		a=Polynomial()
		a.poly=add
		return a

	def __sub__(self,other):
		sub = {x:self.poly.get(x,0) - other.poly.get(x,0) for x in set(self.poly).union(other.poly)}
		a = {}
		for i in range(len(sub)):
			a[i] = sub[len(sub)-i-1]
		return Polynomial(a)
	def __mul__(self, other):
		mul={}
		for i in self.poly.keys():
			for j in other.poly.keys():
				mul[i+j] = 0
		for i in self.poly.keys():
			for j in other.poly.keys():
				mul[i+j] += self.poly[i]*other.poly[j]
		a = Polynomial()
		a.poly = mul
		return a

	def __eq__(self,other):
		if len(self.poly) != len(other.poly):
			return False
		else:
			for i in self.poly:
				while self.poly[i] != other.poly[i]:
					return False
			return True

	def __getitem__(self,key):
		if key in self.poly:
			return self.poly[key]
		else:
			return 0

	def __setitem__(self,key,value):
		return self.poly.__setitem__(key,value)

	def eval(self,x):
		result = 0
		for power, coeff in self.poly.items():
			result += coeff*(x**power)
		return result

	def deriv(self):
		a = Polynomial()
		for key in self.poly.keys():
			if (key==0):
				pass
			else:
				a.poly[key-1] = (self.poly[key])*key
		return a

	def __str__(self):
		return self.poly.__str__()

	def __repr__(self):
		return str(self)