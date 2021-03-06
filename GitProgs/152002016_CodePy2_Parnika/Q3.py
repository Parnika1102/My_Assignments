#!/bin/python3
import matplotlib.animation as animation
import numpy as npy 
import matplotlib.pyplot as plot 
   

mean = 0 
std = 0.1

fig, ax = plot.subplots(1, 1, figsize = (8, 8)) #pyplot.subplots creates a figure and a grid of subplots with a single call,
												# while providing reasonable control over how the individual plots are created.

#To start the animation using 'matplotlib.animation' to plot the graph how often animate(i) is being called.
def animate(i):
	array = npy.random.normal(0, 0.1, 1000*i) 
	count, bins, ignored = plot.hist(array, 30, normed=True) 
	plot.plot(bins, 1/(std * npy.sqrt(2 * npy.pi)) *
	          npy.exp( - (bins - mean)**2 / (2 * std**2) ), 
	          linewidth=2, color='r') 

#Makes an animation by repeatedly calling a function func. 
#The figure object that is used to get draw, resize, and any other needed events. The function to call at each frame
ani = animation.FuncAnimation(fig, animate, frames = 11, interval = 200)
plot.show() 
  
#Credits: https://docs.scipy.org/doc/numpy-1.13.0/reference/ 
	# generated/numpy-random-normal-1.py
