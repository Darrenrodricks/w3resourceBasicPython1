# Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.

def difference(a):
    if a > 17:
        print((a - 17) * 2)
    elif a < 17:
        print(abs(a - 17))


difference(22)
difference(14)