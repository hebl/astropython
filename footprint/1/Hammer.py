'''
Created on 2012-2-22

@author: hebl
'''

import numpy as np
#import azurium as az
import math
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,5))
ax = fig.add_axes([0.1,0.1,0.8,0.8], projection="hammer")
ax.grid(True)

ra = []
dec = []

filename = 'demo.dat'
file = open(filename)
for line in file:
    g = line.split()
    ra.append((float(g[0]) -180)/ 180 * math.pi)
    dec.append(float(g[1]) / 180 * math.pi)    
file.close()

ax.plot(ra,dec,'ko')

#ax.set_yticklabels([],[])
x = range(-150,151,30)
#print x
#for a in x:
#    i = (a+180)/15
#    xx.append(r'$%d^\mathrm{h}$' % i)
#print xx
xx = [r'$2^\mathrm{h}$', '$4^\mathrm{h}$', '$6^\mathrm{h}$', '$8^\mathrm{h}$', '$10^\mathrm{h}$', '$12^\mathrm{h}$', '$14^\mathrm{h}$', '$16^\mathrm{h}$', '$18^\mathrm{h}$', '$20^\mathrm{h}$', '$22^\mathrm{h}$']
ax.set_xticklabels(xx)
plt.title('20120520')

#plt.show()
plt.savefig("demo.png")
#subplot(111, )
#title("LAMOST PLAN STATUS")
#grid(False)

#show()
