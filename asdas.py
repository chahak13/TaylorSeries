import numpy as np
import scipy.misc as sp
import matplotlib.pyplot as plt
import math

def f(x):
    # return (1/np.sqrt(2*np.pi))*(np.e**(-(x**2)/2))
    # return -np.sqrt(3)*x**5 + x**4 + x**3 + 4*np.sqrt(5)*x**2 + x + 1 + (2**x)
    return np.tanh(x)*np.cosh(x**2)

points = np.linspace(start=-2,stop=2,num=2000)

taylor = [f(0)]*len(points)
for degree in range(1,6):
    for i in range(len(points)):
            taylor[i] += (sp.derivative(f,0.0,dx=1e-3,n=degree, order=9)*(points[i])**degree)/math.factorial(degree)

            # taylor[i] += (points[i]**degree)/math.factorial(degree)
    # plt.plot(points, f(points))
# plt.plot(points,taylor,label='taylor')
plt.plot(points,f(points),label='real')
plt.legend()
plt.title('n='+str(degree))
# plt.ylim(-1.5,1.5)
# plt.grid(True)
plt.show()
# plt.savefig('order'+str(n-1)+'.png')
# plt.close()
