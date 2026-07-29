import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,2*np.pi,1000)
y=np.cos(x)
plt.plot(x, y, color='blue', label='y = cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Cosine Function y = cos(x)')
plt.legend()
plt.show()
x=np.linspace(0,500,500)
y=x**2 + 2*x - 3
plt.plot(x, y, color='blue', label='y = x**2+2*x-3')
plt.xlabel('x')
plt.ylabel('y')
plt.show()