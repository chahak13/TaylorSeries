import numpy as np
import scipy.misc as sp
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

def f(x):
    # return np.e**x
    # return (1/np.sqrt(2*np.pi))*(np.e**(-(x**2)/2))
    return np.tanh(x)*np.cosh(x**2)

# points = np.linspace(start=-2,stop=2,num=2000)
points = np.linspace(start=-2,stop=2,num=2000)

for n in range(2,9):
    taylor = [f(0)]*len(points)
    for degree in range(1,n):
        for i in range(len(points)):
                taylor[i] += (sp.derivative(f,0.0,dx=1e-3,n=degree, order=9)*(points[i])**degree)/math.factorial(degree)

            # taylor[i] += (points[i]**degree)/math.factorial(degree)
    # plt.plot(points, f(points))
    plt.plot(points,taylor,label='taylor')
    plt.plot(points,f(points),label='real')
    plt.legend()
    plt.title('n='+str(degree))
    plt.ylim(-20,20)
    # plt.grid(True)
    plt.savefig('arc'+str(n-1)+'.png')
    plt.close()
    # plt.show()
