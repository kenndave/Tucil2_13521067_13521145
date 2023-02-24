from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
from algo import Point
from algo import bruteForce

# Creating dataset
# z = np.random.randint(100, size =(50))
# x = np.random.randint(80, size =(50))
# y = np.random.randint(60, size =(50))
# p = Point(x, y, z)
 
# # Creating figure
# fig = plt.figure(figsize = (10, 7))
# ax = plt.axes(projection ="3d")
 
# # Creating plot
# ax.scatter3D(p.x, p.y, p.z, color = "blue")
# plt.title("simple 3D scatter plot")
 
# # show plot
# plt.show()
def randrange(n, vmin, vmax):
    """
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    """
    return np.random.randint(vmax-vmin, size=(100))

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

n = 100
datax = randrange(n, 0, 100)
datay = randrange(n, 0, 100)
dataz = randrange(n, 0, 100)
# For each set of style and range settings, plot n random points in the box
# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
p = []
closest = []
for i in range(n):
    p.append(Point(datax[i], datay[i], dataz[i]))
ax.scatter(datax, datay, dataz, color = "yellow")


min, p1, p2 = bruteForce(p, n)
closest.append([p1.x, p2.x])
closest.append([p1.y, p2.y])
closest.append([p1.z, p2.z])

ax.plot(closest[0], closest[1], closest[2], color="black")
ax.scatter(p1.x, p1.y, p1.z, color = "black")
ax.scatter(p2.x, p2.y, p2.z, color = "black")
print(closest)
print("First point: ", p1.x, p1.y, p1.z)
print("Second point: ", p2.x, p2.y, p2.z, p2)
print("The smallest distance is", min)

plt.title ("3D scatter plot")
plt.show()