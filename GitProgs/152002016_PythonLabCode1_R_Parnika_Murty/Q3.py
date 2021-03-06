#!/bin/python3
#Class Polygon with attributes numsides and area.
class Polygon:
	#__init__() constructor.
	def __init__(self,numSides,area):
		#The class attributes "numSides" and "area".
		self.numSides = numSides
		self.area = area

	#For the string representation of our polygon object.
	def __str__(self):
		#To display error message if number of sides is less than 3.
		if self.numSides<3 :
			raise Exception("Number of sides should be atleast 3")
		#To display error message if polygon has negative area.
		elif self.area<0 :
			raise Exception("Polygon should have postive area")
		#To display details about the polygon.
		else:
			return "Polygon with % s  sides and area % s" % (self.numSides, self.area)

class Triangle(Polygon):
	area = 0
	numSides = 0
	def __init__(self, a, b, c):
		area = (((a + b + c)/2)*(((a + b + c)/2)-a)*(((a + b + c)/2)-b)*(((a + b + c)/2)-c)) ** (1/2)
		numSides = 3
		Polygon.__init__(self, numSides, area)
		if (a < 0) or (b < 0) or (c < 0) :
			#If any of the sides is negative.
			raise Exception("Triangle should have postive side-lengths")
		elif (c >= (a + b)) or (b >= (a + c)) or (a >= (c + b)) :
			#If sides don't form a triangle.
			raise Exception("Side-lengths do not form a triangle")
		elif area < 0 :
			#If area of triangle is negative.
			raise Exception("Triangle should have positive area")

	def __str__(self):
		#To display area of triangle.
		return "Triangle with area % s" % (self.area)

try:
	#Creating an triangle object with respective 3 sides.
	p1 = Triangle(3,2,1)
	#Printing the object.
	print(p1)
	#Printing the exception type and respective message. 
except Exception as e: 
    print(type(e)) 
    print(e)   