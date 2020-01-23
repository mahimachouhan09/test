class Myclass:
	def init(self):
		return self.s
	def getString(self):
		self.string=input("Enter String:")
	def printString(self):
	 	print(self.string.upper())

myobject=Myclass()
myobject.getString()
myobject.printString()