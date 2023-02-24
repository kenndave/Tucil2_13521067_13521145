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

def bruteForce(P, n): # p list of point, n jumlah point
    min = float("inf")
    for i in range(n):
        for j in range(i+1, n):
            if jarak(P[i], P[j]) < min:
                min = jarak(P[i], P[j])
                p1 = P[i]
                p2 = P[j]
    return min, p1, p2;

# def min(x, y):
#     return x if x < y else y
 
# stripClosest masih kureng
# def stripClosest(strip, size, d):
#     min_jarak = d
#     strip = sorted(strip, key=lambda point: point.y)
 
#     for i in range(size):
#         for j in range(i+1, size):
#             if (strip[j].y - strip[i].y) >= min_jarak:
#                 break
#             if jarak(strip[i], strip[j]) < min_jarak:
#                 min_jarak = jarak(strip[i], strip[j])
#     return min_jarak

# closestUtil masih kureng
# def closestUtil(P, n):
#     if n <= 3:
#         return bruteForce(P, n)
#     mid = n//2
#     midPoint = P[mid]
#     dl = closestUtil(P, mid)
#     dr = closestUtil(P[mid:], n - mid)
#     d = min(dl, dr)
#     strip = []
#     for i in range(n):
#         if abs(P[i].x - midPoint.x) < d:
#             strip.append(P[i])
#     return min(d, stripClosest(strip, len(strip), d))
 
 
# def closest(P, n):
#     P = sorted(P, key=lambda point: point.x)
#     return closestUtil(P, n)

print("helllo worldddd")
P = [Point(x=2, y=3, z = 4), Point(x=12, y=30, z = 15),
         Point(x=40, y=50, z = 60), Point(x=5, y=1, z = 6), Point(x=12, y=10, z = 17), Point(x=3, y=4, z = 5)]
n = len(P)
