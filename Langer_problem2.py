# -*- coding: utf-8 -*-
"""
Solves the Lotka-Volterra equations for
alpha=1,beta=gamma=0.5,delta=2,
with the initial condition x=y=2. Uses
a fourth order Runge Kutta
"""
from pylab import plot,xlabel,show,legend
from numpy import array,arange

def f(r,t):
    x=r[0]
    y=r[1]
    fx=A*x-B*x*y
    fy=C*x*y-D*y
    return array([fx,fy],float)

A,B,C,D=1.0,0.5,0.5,2.0
a=0.0
b=10.0
N=1000
h=(b-a)/N
tpoints=arange(a,b,h)
xpoints=[]
ypoints=[]

r=array([2.0,2.0],float)
for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    k1=h*f(r,t)
    k2=h*f(r+0.5*k1,t+0.5*h)
    k3=h*f(r+0.5*k2,t+0.5*h)
    k4=h*f(r+k3,t+h)
    r+=(k1+2.0*k2+2*k3+k4)/6.0
plot(tpoints,xpoints,label="x(t)")
plot(tpoints,ypoints,label="y(t)")
xlabel("t")
legend()
show()
