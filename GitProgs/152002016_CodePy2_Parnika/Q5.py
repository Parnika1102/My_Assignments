import matplotlib.pyplot as plt 
import matplotlib.animation as ani
import numpy as np 

#Same as Q4, with extra interact() function.
class Sines():
	t = 0
	phi = 0
	deg = 0
	sr = 0
	sl =0
	def __init__(self):
		self.phi = 0
		self.t = 0
		self.deg = 0
		self.sr = 0
		self.sl = 0

	def addSine(self,phi):
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
		plt.axhline(y=1, color='g', label= "Maximum Value", linestyle='-')
		plt.axhline(y=-1, color='r', label= "Minimum Value",linestyle='-')
		plt.grid(True)
		plt.title("Interactive sinusoidal functions")
		plt.ylabel("sin"+"("+chr(952)+"+"+chr(966)+")")
		plt.xlabel(chr(952))
		plt.legend()
		plt.show()

	def shiftRight(self,sr):
		self.sr = sr * (np.pi/180)
		self.t = np.arange(0,2*np.pi,0.025*np.pi)
		plt.plot(self.t,np.sin(self.t-self.sr),label=chr(966)+"="+"0"+chr(176))
		#plt.plot(x,np.sin(x),marker='^',label="sin")
		if self.phi != 0:
			plt.plot(self.t,np.sin(self.t+self.deg-self.sr),label=chr(966)+"="+str(self.phi)+chr(176))
		#plt.plot(x,np.cos(x),marker='+',label="cos")
		#plt.plot(self.t,np.sin(self.t+self.deg),label=chr(966)+"="+"90"+chr(176))
		#plt.xticks(t)
		plt.axhline(y=1, color='g', label= "Maximum Value", linestyle='-')
		plt.axhline(y=-1, color='r', label= "Minimum Value",linestyle='-')
		plt.grid(True)
		plt.title("Interactive sinusoidal functions")
		plt.ylabel("sin"+"("+chr(952)+"+"+chr(966)+")")
		plt.xlabel(chr(952))
		plt.legend()
		plt.show()

	def shiftLeft(self,sl):
		self.sl = sl * (np.pi/180)
		self.t = np.arange(0,2*np.pi,0.025*np.pi)
		plt.plot(self.t,np.sin(self.t+self.sl),label=chr(966)+"="+"0"+chr(176))
		#plt.plot(x,np.sin(x),marker='^',label="sin")
		if self.phi != 0:
			plt.plot(self.t,np.sin(self.t+self.deg+self.sl),label=chr(966)+"="+str(self.phi)+chr(176))
		#plt.plot(x,np.cos(x),marker='+',label="cos")
		#plt.plot(self.t,np.sin(self.t+self.deg),label=chr(966)+"="+"90"+chr(176))
		#plt.xticks(t)
		plt.axhline(y=1, color='g', label= "Maximum Value", linestyle='-')
		plt.axhline(y=-1, color='r', label= "Minimum Value",linestyle='-')
		plt.grid(True)
		plt.title("Interactive sinusoidal functions")
		plt.ylabel("sin"+"("+chr(952)+"+"+chr(966)+")")
		plt.xlabel(chr(952))
		plt.legend()
		plt.show()
#To interact with the animation of sine curve.
	def interact(self):
	    fig, ax = plt.subplots()
	    #NumPy is a Python library used for working with arrays.
	    #arange() is an inbuilt numpy function that returns an ndarray object containing evenly spaced values within a defined interval.
	    x = np.arange(0, 2*np.pi, 0.01)
	    line, = ax.plot(x, np.sin(x))
	#To be able to modify the values of running and direction, I assigned them to anim. 
	#For the manual update, I'm accessing anim's generator object that FuncAnimation uses to update the plot. 
	#This ensures that when I resume the animation, it starts from the active frame rather than from where it was originally paused.
	    def update_time():
	        t = 0
	        t_max = 10
	        while t<t_max:
	            t = t + anim.direction 
	            yield t

	    def animate(i):
	        line.set_ydata(np.sin(x - i/10.0))  
	        return line,
		#To simulate animation of sine curve when pressed certain keys as required in the question.
	    def on_press(event):
	        if event.key.isspace():
	            if anim.running:
	                anim.event_source.stop()
	            else:
	                anim.event_source.start()
	            anim.running ^= True
	        elif event.key == 'a':
	            anim.direction = -1
	        elif event.key == 'd':
	            anim.direction = +1

	        # Manually update the plot
	        if event.key in ['a','d']:
	            t = anim.frame_seq.next()
	            animate(t)
	            plt.draw()
	    #To receive events, we need to write a callback function and then connect our function to the event manager, which is part of the FigureCanvasBase.
	    #The FigureCanvas method mpl_connect() is used for event handling and picking.
	    fig.canvas.mpl_connect('key_press_event', on_press)
	    anim = ani.FuncAnimation(fig, animate, frames=update_time,
	                             interval=100, repeat=True)
	    anim.running = True
	    anim.direction = -1
	    plt.show()

s = Sines()
s.interact()