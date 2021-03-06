#!/bin/python3
#Class Polygon with attributes numsides and area.
class Polygon:
	#__init__() constructor.
	def __init__(self,numSides,area):
		#The class attributes "numSides" and "area".
		self.numSides = numSides
		self.area = area

	#For the string representation of our object.
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

try:
	#Creating a polygon object with respective number of sides and area.
	p1 = Polygon(1,23)
	#Printing the object.
	print(p1)
	#Printing the exception type and respective message. 
except Exception as e: 
    print(type(e)) 
    print(e) 