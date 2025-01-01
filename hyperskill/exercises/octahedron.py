import math
a = int(input())

#Calculate octahedron area
area = round(2 * math.sqrt(3) * a**2, 2)

#Calculate octahedron volume
volume = round(1 / 3 * math.sqrt(2) * a**3, 2)

print(area, volume, sep=' ')