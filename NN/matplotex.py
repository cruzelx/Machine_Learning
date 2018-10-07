import matplotlib
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0,4.0,0.01)
s = np.sin(2*np.pi*t)*np.tanh(2*np.pi*t)*np.tan(2*np.pi*t)

fig,ax = plt.subplots()
ax.plot(t,s)
ax.set(xlabel='test1',ylabel='test2',title='title')
ax.grid()
fig.savefig('test.png')
plt.show()
