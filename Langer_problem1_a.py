# -*- coding: utf-8 -*-
"""
Numerically solves the equation of a planar pendulum
for a 10 cm arm, with an initial condition of theta=178 deg.
Uses the fourth-order Runge-Kutta method. 
"""
from math import sin,cos,pi
from numpy import array,arange
#from pylab import plot,xlabel,ylabel,show
from visual import sphere,rate,cylinder,display

g=9.81
l=0.1

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

s=sphere(pos=[0.1*cos(89.0*pi/90.0),0.1*sin(89.0*pi/90.0),0])
c=cylinder(pos=[0.1*cos(89.0*pi/90.0),0.1*sin(89.0*pi/90.0),0],axis=[0,0,0],radius=0.1)

r=array([89.0*pi/90.0,0.0],float)
for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    k1=h*f(r,t)
    k2=h*f(r+0.5*k1,t+0.5*h)
    k3=h*f(r+0.5*k2,t+0.5*h)
    k4=h*f(r+k3,t+h)
    r+=(k1+2.0*k2+2*k3+k4)/6.0
    rate(30)
    s.pos=[0.1*cos(r[0]),0.1*sin(r[0]),0]
    c.pos=[0.1*cos(r[0]),0.1*sin(r[0]),0]
#plot(tpoints,xpoints)
# plot(tpoints,ypoints)
#xlabel("t (s)")
#ylabel("theta (rad)")
#show()
