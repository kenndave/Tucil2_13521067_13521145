import math
import random

from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

euclid_count = 0

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

def dist(p1, p2):
    global euclid_count
    euclid_count += 1
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2 + (p1.z - p2.z)**2)

def bruteForce(P, n):
    min_dist = float("inf")
    for i in range(n):
        for j in range(i+1, n):
            if dist(P[i], P[j]) < min_dist:
                min_dist = dist(P[i], P[j])
                closest_pair = (P[i], P[j])
    return closest_pair

def min(x, y):
    return x if x < y else y

def stripClosest(strip, size, d, closest_pair):
    min_dist = d
    strip = sorted(strip, key=lambda point: point.z)

    for i in range(size):
        for j in range(i+1, size):
            if (strip[j].z - strip[i].z) >= min_dist:
                break
            if dist(strip[i], strip[j]) < min_dist:
                min_dist = dist(strip[i], strip[j])
                closest_pair = (strip[i], strip[j])
    return closest_pair

def closestUtil(P, n):
    if n <= 3:
        return bruteForce(P, n)
    mid = n//2
    midPoint = P[mid]
    dl_pair = closestUtil(P[:mid], mid)
    dr_pair = closestUtil(P[mid:], n - mid)
    dl = dist(*dl_pair)
    dr = dist(*dr_pair)
    d = min(dl, dr)
    closest_pair = dl_pair if dl < dr else dr_pair
    strip = []
    for i in range(n):
        if abs(P[i].x - midPoint.x) < d:
            strip.append(P[i])
    closest_pair_in_strip = stripClosest(strip, len(strip), d, closest_pair)
    closest_pair = closest_pair if dist(*closest_pair) < dist(*closest_pair_in_strip) else closest_pair_in_strip
    return closest_pair

def closest(P, n):
    P = sorted(P, key=lambda point: point.x)
    return closestUtil(P, n)

def createRandomPoints(n):
    points = []
    for i in range(n):
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        z = random.randint(1, 100)
        p = Point(x, y, z)
        points.append(p)
    return points

def printPoints(points):
    print("The randomize points are,")
    for point in points:
        print(f"({point.x}, {point.y}, {point.z})")

def printPointPair(pair):
    p1, p2 = pair
    print("Point 1: ({0}, {1}, {2})".format(p1.x, p1.y, p1.z))
    print("Point 2: ({0}, {1}, {2})".format(p2.x, p2.y, p2.z))

def visualizePoints(points, closest_pair=None):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
 
    x = [point.x for point in points]
    y = [point.y for point in points]
    z = [point.z for point in points]
 
    if closest_pair:
        p1, p2 = closest_pair
 
        ax.scatter(p1.x, p1.y, p1.z, color='r', s=100)
        ax.scatter(p2.x, p2.y, p2.z, color='r', s=100)
 
    ax.scatter(x, y, z)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
 
    plt.show()

if __name__ == "__main__":
    import time

    print()
    print("Closest Pair of Points in 3D Using DIVIDE AND CONQUER Algorithm")
    print()

    number_of_points = int(input("Input the number of points: "))
    P = createRandomPoints(number_of_points)
    # printPoints(P)
    print()

    start_time = time.time()
    closest_pair = closest(P, number_of_points)
    end_time = time.time()
    
    print()
    print("The closest pair of points are,")
    printPointPair(closest_pair)
    print()

    print("The distance is", dist(*closest_pair))
    print("The number of Euclidian formula operation is", euclid_count)
    print("The time taken is", end_time - start_time, "seconds")
    print()

    visualizePoints(P, closest_pair)