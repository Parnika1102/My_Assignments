#!/bin/python3
# Import libraries 
import pandas as pd
from matplotlib import pyplot as plt 
import numpy as np 

#to create a class PieChart
class PieChart:
	listkey=[]
	listval=[]
	listt=[]
	dict1={}
	#For the constructor part.
	def __init__(self,Dictt):
		self.dicts = Dictt
		for key in self.dicts:
			#setattr(self, key, Dictt[key])
			self.k = key
			self.v = self.dicts[key]
			#using lists to store values and labels to be able to display in piechart.
			self.listt.append([self.k,self.v])
			self.listkey.append(key)
			self.listval.append(self.dicts[key])
			#Exceptions as required.
			if type(self.k) != str :
				raise Exception("Label should be string")
			elif type(self.v) != int or self.v < 0 :
				raise Exception("Value should be a postive numeric")
	#Overloading add function.
	def __add__(self,other):
		self.other = other
		if type(other) == tuple:
			self.listt.append([self.other[0],self.other[1]])
			if len(self.other) != 2 :
				raise Exception("Tuple should be of length 2")
			elif type(self.other[0]) != str :
				raise Exception("Label should be string")
			elif type(self.other[1]) != int or self.other[1] < 0 :
				raise Exception("Value should be a postive numeric")

		for pair in self.listt:
			if pair[0] not in self.dict1 :
				self.dict1[pair[0]] = pair[1]
			else:
				self.dict1[pair[0]] = self.dict1[pair[0]] + pair[1]
		self.listkey.clear()
		self.listval.clear()
		self.dicts = self.dict1
		for key in self.dict1:
			self.listkey.append(key)
			self.listval.append(self.dict1[key])
		#print(self.listkey)
		#print(self.listval)
		return self

	#Overloading subtract function.
	def __sub__(self,str1):
		if str1 in self.dicts:
			self.dicts.pop(str1)
		self.listkey.clear()
		self.listval.clear()
		for key in self.dicts:
			self.listkey.append(key)
			self.listval.append(self.dicts[key])
		for pair in self.listt:
			if pair[0] == str1:
				self.listt.remove(pair)
		return self

try:
	#p = PieChart({"Frogs":10,"Dog":20, "Cat":30})
	p = PieChart({"Frogs":10,"Dog":25})
	#p = p + ("Cat",25)
	p = p + PieChart({"Frogs":20,"Cat":10})
	#p = PieChart({"Frogs":10,"Dog":20})
	p = p - 'Frogs'
	#p = p + PieChart({"Frogs": 20, "Cat": 10})
	p = p - 'Lions'
	fig = plt.figure(figsize =(10, 7)) 
	plt.pie(p.listval, labels = p.listkey,autopct='%1.1f%%')
	plt.show()
except Exception as e: 
    print(type(e)) 
    print(e)
