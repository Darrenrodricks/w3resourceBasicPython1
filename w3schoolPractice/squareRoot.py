# Write a Python program to calculate the hypotenuse of a right angled triangle.
from math import sqrt
print("Give the values of the shorter sides of the triangles")
a = int(input("side 1: "))
b = int(input("side 2: "))
c = sqrt((a **2) + (b **2))
print("Your hypotenuse is {}".format(c))
