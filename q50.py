class American:
	@staticmethod
	def printnationality():
		print("static method print: America")
myobject=American()
#myobject.printnationality()
American.printnationality()