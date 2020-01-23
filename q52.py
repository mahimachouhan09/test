class Circle:
	def init(self,r):
		self.r=r
	def area(self,r):
		a=3.14 * r**2
		return a
myobject=Circle()
print(myobject.area(1))
