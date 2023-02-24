# Import libraries
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
import math
 
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

def jarak(p1, p2):
    return math.sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2 + (p1.z-p2.z)**2)

def BruteForce(P, n): # p list of point, n jumlah point
    min = float("inf")
    for i in range(n):
        for j in range(i+1, n):
            if jarak(P[i], P[j]) < min:
                min = jarak(P[i], P[j])
    return min;


# Creating dataset
z = np.random.randint(100, size =(50))
x = np.random.randint(80, size =(50))
y = np.random.randint(60, size =(50))
p = Point(x, y, z)
 
# Creating figure
fig = plt.figure(figsize = (10, 7))
ax = plt.axes(projection ="3d")
 
# Creating plot
ax.scatter3D(p.x, p.y, p.z, color = "blue")
plt.title("simple 3D scatter plot")
 
# show plot
plt.show()