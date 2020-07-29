import numpy as np
import matplotlib.pyplot as plt
x=5
x2=pow(x,2)
x3=pow(x,3)
print(x,'^2 :',x2,x,'^3 :',x3)
theta=30
s=np.sin(theta)
c=np.cos(theta)
print('theta: ',theta,' sin:',s,theta,' cos:',c)
print('These are radians.')


meshPoints=np.linspace(-1,1,500)
print('meshPoints[53] =' , meshPoints[53])
plt.plot(meshPoints,np.sin(2*np.pi*meshPoints))
plt.show()
