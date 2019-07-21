class People: 
	def __init__(this,name,age):
		this.name=name
		this.age = age
		this.friends=[]
		print("-doesn't run")
	def doSth(this):
		print(this.name,this.age,"is eatting")

class Engineer(People):
	pass
class SoftEngineer(People):
	def __init__(this,name,age):
		People.__init__(this,name,age)
		this.skill = 'Python'

rod = Engineer("Rod",34)
rod.doSth()
zzt = SoftEngineer("Rod",34)
zzt.doSth()

