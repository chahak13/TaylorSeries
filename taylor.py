import numpy as np
import scipy.misc as sp
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

def f(x):
    # return np.e**x
    # return (1/np.sqrt(2*np.pi))*(np.e**(-(x**2)/2))
    return np.tanh(x)*np.cosh(x**2)
    # return np.cos(x)
    # return np.sin(x)

points = np.linspace(start=-2,stop=2,num=2000)

for n in range(2,10):
    taylor = [f(0)]*len(points)
    for degree in range(1,n):
        for i in range(len(points)):
                taylor[i] += (sp.derivative(f,0.0,dx=1e-1,n=degree, order=11)*(points[i])**degree)/math.factorial(degree)

            # taylor[i] += (points[i]**degree)/math.factorial(degree)
    # plt.plot(points, f(points))
    plt.plot(points,taylor,label='taylor')
    plt.plot(points,f(points),label='real')
    plt.legend()
    plt.title('n='+str(degree))
    # plt.ylim(0,0.75)
    # plt.grid(True)
    # plt.savefig('exponential/exponential'+str(n-1)+'.png')
    # plt.savefig('gaussian/gaussian'+str(n-1)+'.png')
    plt.savefig('arc/arc'+str(n-1)+'.png')
    # plt.savefig('cos/cosine'+str(n-1)+'.png')
    # plt.savefig('sin/sin'+str(n-1)+'.png')
    plt.close()
    # plt.show()
