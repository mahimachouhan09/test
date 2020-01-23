class Person:
	
	def getGender():
		return 0
class Male(Person):
	def getGender():
		return male
class Female(Person):
	def getGender():
		return female

maleobj=Male()
femaleobj=Female()
print(maleobj.getGender())
print(femaleobj.getGender())