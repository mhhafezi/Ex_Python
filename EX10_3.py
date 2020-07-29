import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,10,200)
f=np.exp(-x/10)*np.sin(np.pi*x)
g=x* np.exp(-x/3)
plt.plot(x,f,x,g)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend(['f(x)','g(x)'])
plt.show()
t=np.linspace(0,2*np.pi,100)
r=0.8+np.cos(t)
z=r*np.cos(t)
y=r*np.sin(t)
plt.plot(z,y)

r=1.0+np.cos(t)
z=r*np.cos(t)
y=r*np.sin(t)
plt.plot(z,y)

r=1.2+np.cos(t)
z=r*np.cos(t)
y=r*np.sin(t)
plt.plot(z,y)

plt.legend(['r=0.8','r=1.0','r=1.2'])
plt.show()
