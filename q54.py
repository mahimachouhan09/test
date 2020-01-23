class Shape():
	def init(self,l):
		self.s=s
		self.l=l
	def area(self):
		return 0

class Square(Shape):
	def init(self):
		return "0"
	def area(self,l):
		return self.l*self.l

base_obj=Shape()
derived_obj=Square()
derived_obj.area(2)