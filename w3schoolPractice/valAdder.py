# Write a Python program to calculate the sum of three given numbers, if the values are equal then
# return three times of their sum.

def valAdder(x, y, z):
    if x == y == z:
        print((x + y + z) * 3)
    else:
        print(x + y + z)

valAdder(1, 2, 3)
valAdder(3, 3, 3)
