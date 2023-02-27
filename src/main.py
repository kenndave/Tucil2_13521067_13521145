import math
import random
import time

from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

euclid_count = 0

def quickSort(list, key):
    if len(list) <= 1:
        return list
    else:
        pivot = list.pop()

    greaterPivot = []
    lesserPivot = []
    for titik in list:
        if titik[key] > pivot[key]:
            greaterPivot.append(titik)
        else:
            lesserPivot.append(titik)
    # if (key == 0):
    #     for titik in list:
    #         if titik.x > pivot.x:
    #             greaterPivot.append(titik)
    #         else:
    #             lesserPivot.append(titik)
    # elif (key == 1):
    #     for titik in list:
    #         if titik.y > pivot.y:
    #             greaterPivot.append(titik)
    #         else:
    #             lesserPivot.append(titik)
    # elif (key == 2):
    #     for titik in list:
    #         if titik.z > pivot.z:
    #             greaterPivot.append(titik)
    #         else:
    #             lesserPivot.append(titik)
    
    return quickSort(lesserPivot, key) + [pivot] + quickSort(greaterPivot, key)

def dist(p1, p2):
    global euclid_count
    euclid_count += 1
    distance = 0
    for i in range(len(p1)):
        distance += (p1[i] - p2[i])**2
    return math.sqrt(distance)

def bruteForce(P, n):
    min_dist = 999999
    for i in range(n):
        for j in range(i+1, n):
            if dist(P[i], P[j]) < min_dist:
                min_dist = dist(P[i], P[j])
                closest_pair = (P[i], P[j])
    return closest_pair

def min(x, y):
    if x < y:
        return x
    else:
        return y

def stripClosest(strip, size, d, closest_pair):
    min_dist = d
    #printPoints(strip)
    for i in range(size):
        for j in range(i+1, size):
            if (strip[j][0] - strip[i][0]) >= min_dist:
                break
            if dist(strip[i], strip[j]) < min_dist:
                min_dist = dist(strip[i], strip[j])
                closest_pair = (strip[i], strip[j])
    return closest_pair

def closestDots(P, n):
    if n <= 3:
        return bruteForce(P, n)
    mid = n//2
    midPoint = P[mid]
    left_pair = closestDots(P[:mid], mid)
    right_pair = closestDots(P[mid:], n - mid)
    left_closest = dist(*left_pair)
    right_closest = dist(*right_pair)
    d = min(left_closest, right_closest)
    if left_closest < right_closest:
        closest_pair = left_pair
    else:
        closest_pair = right_pair
    strip = []
    for i in range(n):
        if abs(P[i][0] - midPoint[0]) < d:
            strip.append(P[i])
    if len(strip) != 0:
        closest_pair_in_strip = stripClosest(strip, len(strip), d, closest_pair)
        if dist(*closest_pair) < dist(*closest_pair_in_strip):
            return closest_pair
        else:
            return closest_pair_in_strip
        
    else:
        return closest_pair

def DivAndConq(P, n):
    P = quickSort(P, 0)
    return closestDots(P, n)

def createRandomPoints(n, dimension):
    points = []
    for i in range(n):
        p = []
        for j in range(dimension):
            p.append(round(random.uniform(1, 100), 2))
        points.append(p)
    #print(points)
    return points

def printPoints(points):
    print("The randomize points are,")
    for point in points:
        print("(", end='')
        for i in range(len(points[0])):
            print(point[i], end= '')
            if i < len(points[0])-1:
                print(", ")
        print(")")

def printPointPair(pair):
    p1, p2 = pair
    print("Point 1: (", end='')
    for j in range(len(p1)):
        print (p1[j], end= '')
        if (j < len(p1)-1):
            print (', ', end ='')
    print(")")

    print("Point 2: (", end= '')
    for j in range(len(p2)):
        print (p2[j], end='')
        if (j < len(p2)-1):
            print (', ', end= '')
    print(")")


def visualizePoints(points, closest_pair=None):
    fig = plt.figure()
    if len(points[0]) == 3:
        ax = fig.add_subplot(111, projection='3d')
    elif len(points[0]) == 2:
        ax = fig.add_subplot(111)
    else:
        ax = fig.add_subplot(111)
    x = []
    for i in range(len(points[0])):
        x.append([point[i] for point in points])
    if closest_pair:
        p1, p2 = closest_pair
        if (len(p1) == 3):
            ax.scatter(p1[0], p1[1], p1[2], color='r', s=100)
            ax.scatter(p2[0], p2[1], p2[2], color='r', s=100)
        elif (len(p1) == 2):
            ax.scatter(p1[0], p1[1], color='r', s=100)
            ax.scatter(p2[0], p2[1], color='r', s=100)
        else:
            ax.plot(p1[0], 0.0, color='r')
            ax.plot(p2[0], 0.0, color='r')

    if (len(p1) == 3):
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], color = 'r', linewidth = 5)
        ax.scatter(x[0], x[1], x[2])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

    elif (len(p1) == 2):
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color = 'r', linewidth = 5)
        ax.scatter(x[0], x[1])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')

    else:
        y = [0 for i in range(len(x[0]))]
        ax.plot([p1[0], p2[0]], [0, 0], color = 'r', linewidth = 5)
        ax.scatter(x[0], y)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
 
    plt.show()

# if __name__ == "__main__":
# Main
print()
print("Mencari Pasangan Titik Terdekat 3D dengan Algoritma Divide and Conquer")
print()

n_titik = int(input("Jumlah titik: "))
while n_titik <= 1:
    print("Jumlah titik untuk diuji tidak valid. Silahkan input ulang dengan jumlah titik lebih dari 1!")
    n_titik = int(input("Jumlah titik: "))
dimens = int(input("Dimensi: "))
while dimens <= 0:
    print("Dimensi tersebut tidak valid. Silahkan input ulang dimensi dengan nilai 1 atau ke atas.")
    dimens = int(input("Dimensi: "))
P = []
P = createRandomPoints(n_titik, dimens)
P2 = P.copy()
# printPoints(P)
print()


# BruteForce
start_bf = time.time()
closest_pair2 = bruteForce(P2, n_titik)
end_bf = time.time()
# Divide & Conquer
euclid_count_bf = euclid_count

start_time = time.time()
closest_pair = DivAndConq(P, n_titik)
end_time = time.time()
# printPoints(P2)


print()
print("Pasangan titik terdekat dengan algoritma Divide & Conquer:")
printPointPair(closest_pair)
print()
print("Pasangan titik terdekat dengan algoritma BruteForce:")
printPointPair(closest_pair2)
print()

print("Jarak pasangan titik terdekat Divide & Conquer: ", dist(*closest_pair)) #round(dist(*closest_pair), 2))
print()
print("Jarak pasangan titik terdekat Brute Force: ", dist(*closest_pair2))
print()
print("Jumlah operasi euclidean algoritma Divide & Conquer: ", euclid_count-euclid_count_bf)
print("Jumlah operasi euclidean algoritma Brute Force: ", euclid_count_bf)
print("Waktu Eksekusi Divide & Conquer ", 1000*(end_time - start_time), "miliseconds")
print("Waktu Eksekusi Brute Force ", 1000*(end_bf - start_bf), " miliseconds")
print()
if dimens <= 3 & dimens > 0:
        visualize = input("Apakah ingin ditampilkan visualisasinya? (Y / N)")
        while visualize not in {'Y', 'N', 'y', 'n'}:
            print("Input tidak valid. Silahkan input ulang!")
            visualize = input("Apakah ingin ditampilkan visualisasinya?(Y/N) ")
        if (visualize in {'Y', 'y'}):
            visualizePoints(P, closest_pair)
else:
    print("Maaf, tidak dapat divisualisasikan pada dimensi,", dimens)
    # if dimens <= 3 & dimens > 0:
    #     visualize = (input("Apakah ingin ditampilkan visualisasinya?(Y/N) "))
    #     while not (visualize == 'Y' or visualize == 'y' or visualize == 'N' or visualize == 'n'):
    #         print(visualize)
    #         print("Input tidak valid. Silahkan input ulang!")
    #         visualize = input("Apakah ingin ditampilkan visualisasinya?(Y/N) ")
    #     visualizePoints(P, closest_pair)
    # else:
    #     print("Maaf tidak dapat divisualisasikan untuk dimensi ", dimens, ".")