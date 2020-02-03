import math


class Line:

	def __init__(self,coor1,coor2):
		self.coor1 = coor1
		self.coor2 = coor2
	
	def distance(self):
		distance = math.sqrt(((self.coor1[0]-self.coor2[0])**2)+((self.coor1[1]-self.coor2[1])**2))
		return distance
		
	def slope(self):
		return (self.coor2[1] - self.coor1[1])/(self.coor2[0]-self.coor1[0])
		
#x = Line([0,0],[0,0])
#hey = x.distance()
#print(hey)
#hey2 = x.slope()
#print(hey2)


class Sphere:


	def __init__(self, radius):
		self.radius = radius
		
	def volume(self):
		return (4/3)*math.pi*(self.radius**3)
		
	def surface_area(self):
		return 4*math.pi*(self.radius**2)
		

	
class Cylinder:

	def __init__(self, radius, height):
		self.radius = radius
		self.height = height
		
	def volume(self):
		return math.pi*(self.radius**2)*self.height
		
	def surface_area(self):
		return (2*math.pi*self.radius*self.height)+(2*math.pi*(self.radius**2))
		
		
class Cone:

	def __init__(self, radius, height):
		self.radius = radius
		self.height = height
		
	def volume(self):
		return math.pi*(self.radius**2)*(self.height/3)
		
	def surface_area():
		return math.pi*self.radius*(self.radius+math.sqrt(self.height**2+self.radius**2))
		

		
		
class Ewok:

	def __init__(self, firstname, tribe, age=1):
		self.tribe = tribe
		self.age = age
		self.firstname = firstname

		if firstname[-1] == "i":
			self.tribe = "Booyi"
		elif firstname[-1] == "a":
			self.tribe = "Humyaka"
		else:
			self.tribe = "Maikumba"

	def str(self):
		return self.firstname, self.tribe, self.age
	
	def set_age(self, newage):
		self.age = newage
		
		
		
class Player:
