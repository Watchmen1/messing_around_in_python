#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 20:18:22 2020

@author: watchmen1
"""
import math
#set up the charge centres and expression for electric potential
def f2d(x,y):
    q1=np.array([30.5,30.5])
    q2=np.array([35.5,30.5])
    q3=np.array([30.5,40.5])
    return (-1/(math.sqrt((x-q1[0])**2 + (y-q1[1])**2))+\
            (-1/(math.sqrt((x-q2[0])**2 + (y-q2[1])**2))))+\
            (-1/(math.sqrt((x-q3[0])**2 + (y-q3[1])**2)))

#set up empty array for potential
arraf2d = np.zeros(shape=(70,70))

#fill in values
for i in np.arange(0,70):
        for j in np.arange(0,70):
             arraf2d[i,j]=f2d(i,j)

#print(arraf2d)

import numpy as np
from numpy import gradient as ng
from matplotlib.pyplot import quiver as qu
import matplotlib.pyplot as plt
x=np.arange(0,70,1)
y=np.arange(0,70,1)
Y,X = np.meshgrid(y,x)
#z = X*np.exp(-X**2 -Y**2)
#z=(X-3)**2 + (Y-3)**2 
dx, dy = ng(arraf2d, edge_order=2)
#dx, dy = ng(z, edge_order=2)

#for i in range(0,70):
#        for j in range(0,70):
#             modgrad=np.sqrt(dx**2+dy**2)
#print(modgrad[45,45])
                
fig, ax = plt.subplots(figsize=(70,70))
ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])
ax.set_aspect('equal')
plt.contour(X, Y, np.sqrt(dx**2+dy**2), 10, colors='black')
plt.contourf(X, Y, np.sqrt(dx**2+dy**2), 20, cmap='plasma')
ax.quiver(X,Y,dx,dy, scale=3)
plt.colorbar()
plt.savefig('three_particle_electric_field.jpg')
plt.show()