import math
import random

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
    disst = 0
    for i in range(len(p1)):
        disst += (p1[i] - p2[i])**2
    return math.sqrt(disst)

def bruteForce(P, n):
    min_dist = float("inf")
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
    if len(strip[0]) < 2:
        #print(len(strip))
        sumbu = 0
        strip = quickSort(strip, sumbu)
    else:
        sumbu = 1
        strip = quickSort(strip, sumbu)
    #printPoints(strip)
    for i in range(size):
        for j in range(i+1, size):
            if (strip[j][sumbu] - strip[i][sumbu]) >= min_dist:
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
    if dl < dr:
        closest_pair = dl_pair
    else:
        closest_pair = dr_pair
    #closest_pair = dl_pair if dl < dr else dr_pair
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

def closest(P, n):
    P = quickSort(P, 0)
    return closestUtil(P, n)

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

if __name__ == "__main__":
    import time

    print()
    print("Closest Pair of Points in 3D Using DIVIDE AND CONQUER Algorithm")
    print()

    number_of_points = int(input("Input the number of points: "))
    dimens = int(input("Dimensi: "))
    while dimens <= 0:
        print("Dimensi tersebut tidak valid. Silahkan input ulang dimensi dengan nilai 1 atau ke atas.")
        dimens = int(input("Dimensi: "))
    P = []
    P = createRandomPoints(number_of_points, dimens)
    P2 = P.copy()
    # printPoints(P)
    print()


    # BruteForce
    start_bf = time.time()
    closest_pair2 = bruteForce(P2, number_of_points)
    end_bf = time.time()
    # Divide & Conquer
    euclid_count_bf = euclid_count

    start_time = time.time()
    closest_pair = closest(P, number_of_points)
    end_time = time.time()
    # printPoints(P2)

    
    print()
    print("The closest pair of points are, (Divide & Conquer)")
    printPointPair(closest_pair)
    print()
    print("The closest pair of points are, (bruteForce)")
    printPointPair(closest_pair2)
    print()

    print("The distance is for Divide & Conquer", dist(*closest_pair)) #round(dist(*closest_pair), 2))
    print()
    print("The distance for Brute Force is", dist(*closest_pair2))
    print()
    print("The number of Euclidian formula operation (Divide & Conquer) is", euclid_count-euclid_count_bf)
    print("The number of Euclidian formula operation (Brute Force) is", euclid_count_bf)
    print("Time taken by Divide & Conquer ", 1000*(end_time - start_time), "miliseconds")
    print("Time taken by Brute Force ", 1000*(end_bf - start_bf), " miliseconds")
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