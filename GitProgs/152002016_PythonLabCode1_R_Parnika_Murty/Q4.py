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
		#To display details about the polygon if number of sides of polygon is equals to 3.
		elif self.numSides == 3:
			return "Triangle with area % s" % (self.area)
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

class Paper:
	#__init__() constructor.
	def __init__(self,area):
		#The class attribute "area".
		#Additional attributes have been used for all the functions.
		self.area = area
		self.remArea = area
		self.tDict = {}
		self.listt = []
	#Here the + operator is being overloaded and an exception thrown when remaining area is not sufficient for the polygon to be added.
	#The details of the polygon being added, like area and numSides, are being added into a list of lists as [numSides, area].
	#We are also calculating the remaining area and printing the polygon details.
	def __add__(self,o):
		if self.remArea < o.area :
			raise Exception("Paper does not have sufficient free area to fit the polygon")	
		self.key = o.numSides
		self.value = o.area
		self.listt.append([self.key,self.value])
		self.remArea = self.remArea - o.area
		print(o)
		#print(self.listt)
		return self
	#Here me are merging the polygons with same number of sides(numSides) by adding their areas. We have used a dictionary for this.
	#We loop over the list of lists for this purpose. The "pair[0]" has the numSides and "pair[1]" has the area. So if the numSides 
	#are equal we will add the areas else create a new {key:value} pair for dictionary "tDict".
	def merge(self):
		for pair in self.listt:
			if pair[0] in self.tDict:
				self.tDict[pair[0]] = self.tDict[pair[0]] + pair[1]
			else:
				self.tDict[pair[0]] = pair[1]
		for x in self.tDict:
			if x == 3:
				print("Triangle with area "+str(self.tDict[x])+".")
			else:
				print("Polygon with "+str(x)+" sides and area "+str(self.tDict[x])+".")
		#print(self.tDict)
		#return self

	#We are returning the remaining area and original area here.
	#If the original area of the Paper is itself negative then we throw an exception and handle it.
	def __str__(self):
		if self.area < 0:
			raise Exception("Paper should have a positive area")
		else:
			return "Paper has free area {0} out of {1}, and contains:\n".format(self.remArea,self.area)

	#We are erasing the shapes from the paper here and as a result the paper is blank at the end.
	#We are also erasing "listt" and "tDict" to reflect that the shapes have been erased and now 
	#new shapes can be added from the beginning with the initial area of paper again being the original area.
	def erase(self):
		self.remArea = self.area
		self.listt.clear()
		self.tDict.clear()
try:
	pap = Paper(200)
	pap = pap + Polygon(10, 100)
	pap = pap + Polygon(20, 50)
	pap = pap + Triangle(3, 4, 5)
	print(pap)
	pap.erase()
	print(pap)
	'''pap = Paper(2000)
	pap = Paper(-1)
	print(pap)
	pap = Paper(200)
	p = Polygon(10, 100)
	pap = pap + p
	pap = pap + Polygon(5, 45)
	print(type(pap).__name__)
	pap = Paper(200)
	p1 = Polygon(10, 100)
	p2 = Polygon(20, 150)
	pap = (pap + p1) + p2
	pap = Paper(200)
	pap = pap + Polygon(10, 100)
	pap = pap + Polygon(20, 50)
	pap = pap + Triangle(3, 4, 5)
	print(pap)
	pap = Paper(200)
	pap = pap + Polygon(3, 100)
	print(pap)
	pap = Paper(2000)
	pap = pap + Polygon(10, 100)
	pap = pap + Polygon(20, 50)
	pap = pap + Polygon(10, 200)
	pap = pap + Polygon(3,24)
	pap = pap + Triangle(3, 4, 5)
	print(pap)
	pap.merge()
	print(pap)
	pap = pap + Polygon(10, 123)
	print(pap)'''
	#Printing the exception type and respective message. 
except Exception as e: 
    print(type(e)) 
    print(e)   