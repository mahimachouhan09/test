class Rectangle:
	def init(self,l,w):
		self.length=l
		self.width=w
	def area(self,l,w):
		return l*w

obj=Rectangle()
print(obj.area(4,5))