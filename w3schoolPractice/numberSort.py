# Write a Python program to sort three integers without using conditional statements and loops.
a = int(input("Pick a number: "))
b = int(input("Pick another number: "))
c = int(input("Pick another number: "))

mini = min(a, b, c)
maxi = max(a, b, c)

z = (a + b + c) - mini - maxi
print("Numbers in sorted order: ", mini, maxi, z)