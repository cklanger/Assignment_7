# -*- coding: utf-8 -*-
"""
Numerically solves the equations of a planar pendulum
with 15cm arm, and an initial condition theta=89 deg
from the vertical. Uses the Leapfrog method.
"""
from math import sin,pi
from numpy import array,arange
from pylab import plot,xlabel,ylabel,show

g=9.81
l=0.15

def f(r,t):
    theta=r[0]
    omega=r[1]
    ftheta=omega
    fomega=-(g/l)*sin(theta)
    return array([ftheta,fomega],float)

a=0.0
b=10.0
N=1000
h=(b-a)/N
tpoints=arange(a,b,h)
xpoints=[]
ypoints=[]
r_half=array([],float)
r_3half=array([],float)

r=array([1.553,0.0],float)
for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    r_half=r+0.5*h*f(r,t)
    r+=h*f(r_half,t+0.5*h)
    r_3half=r_half+h*f(r,t+h)
plot(tpoints,xpoints)
# plot(tpoints,ypoints)
xlabel("t (s)")
ylabel("theta (rad)")
show()