import matplotlib.pyplot as plt 
import numpy as np 


#To create class Sines.
class Sines:
	t = 0
	phi = 0
	deg = 0
	sr = 0
	sl =0
	def __init__(self):	#Adding constructor
		self.phi = 0
		self.t = 0
		self.deg = 0
		self.sr = 0
		self.sl = 0

	def addSine(self,phi): #To add the offset and then calculating the radian of the degree.
		self.phi = phi
		self.deg = self.phi * (np.pi/180)
		#t = [0,30,45,60,90]
		#t = np.linspace(0,2*np.pi)
		#self.t = np.arange(0,2*np.pi,0.025*np.pi)
		#x = [i*(np.pi/180) for i in t]

	def show(self):
		self.t = np.arange(0,2*np.pi,0.025*np.pi)
		plt.plot(self.t,np.sin(self.t),label=chr(966)+"="+"0"+chr(176))
		#plt.plot(x,np.sin(x),marker='^',label="sin")
		if self.phi != 0:
			plt.plot(self.t,np.sin(self.t+self.deg),label=chr(966)+"="+str(self.phi)+chr(176))
		#plt.plot(x,np.cos(x),marker='+',label="cos")
		#plt.plot(self.t,np.sin(self.t+self.deg),label=chr(966)+"="+"90"+chr(176))
		#plt.xticks(t)
		plt.axhline(y=1, color='g', linestyle='-')
		plt.text(5,1,"Maximum Value")
		plt.axhline(y=-1, color='r', linestyle='-')
		plt.text(3,-1,"Minimum Value")
		plt.grid(True)
		plt.title("Interactive sinusoidal functions")
		plt.ylabel("sin"+"("+chr(952)+"+"+chr(966)+")")
		plt.xlabel(chr(952))
		plt.legend()
		plt.show()

	def shiftRight(self,sr):		#To shift graph right by the amount of offset mentioned while calling the method.
		self.sr = sr * (np.pi/180)
		self.t = np.arange(0,2*np.pi,0.025*np.pi)
		plt.plot(self.t,np.sin(self.t-self.sr),label=chr(966)+"="+"0"+chr(176))
		#plt.plot(x,np.sin(x),marker='^',label="sin")
		if self.phi != 0:
			plt.plot(self.t,np.sin(self.t+self.deg-self.sr),label=chr(966)+"="+str(self.phi)+chr(176))
		#plt.plot(x,np.cos(x),marker='+',label="cos")
		#plt.plot(self.t,np.sin(self.t+self.deg),label=chr(966)+"="+"90"+chr(176))
		#plt.xticks(t)
		plt.axhline(y=1, color='g', linestyle='-')
		plt.text(5,1,"Maximum Value")
		plt.axhline(y=-1, color='r', linestyle='-')
		plt.text(3,-1,"Minimum Value")
		plt.grid(True)
		plt.title("Interactive sinusoidal functions")
		plt.ylabel("sin"+"("+chr(952)+"+"+chr(966)+")")
		plt.xlabel(chr(952))
		plt.legend()
		plt.show()

	def shiftLeft(self,sl):		#To shift graph left by the amount of offset mentioned while calling the method.
		self.sl = sl * (np.pi/180)
		self.t = np.arange(0,2*np.pi,0.025*np.pi)
		plt.plot(self.t,np.sin(self.t+self.sl),label=chr(966)+"="+"0"+chr(176))
		#plt.plot(x,np.sin(x),marker='^',label="sin")
		if self.phi != 0:
			plt.plot(self.t,np.sin(self.t+self.deg+self.sl),label=chr(966)+"="+str(self.phi)+chr(176))
		#plt.plot(x,np.cos(x),marker='+',label="cos")
		#plt.plot(self.t,np.sin(self.t+self.deg),label=chr(966)+"="+"90"+chr(176))
		#plt.xticks(t)
		plt.axhline(y=1, color='g', linestyle='-')	#To mark the maximum level
		plt.text(5,1,"Maximum Value")
		plt.axhline(y=-1, color='r', linestyle='-')	#To mark the minimum level
		plt.text(3,-1,"Minimum Value")
		plt.grid(True)
		plt.title("Interactive sinusoidal functions")
		plt.ylabel("sin"+"("+chr(952)+"+"+chr(966)+")")
		plt.xlabel(chr(952))
		plt.legend()
		plt.show()

s = Sines()
s.addSine(0)
s.addSine(90)
#s.shiftRight(45)
s.shiftLeft(45)
#s.show()