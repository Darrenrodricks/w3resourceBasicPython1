# Write a Python program to calculate midpoints of a line.
x1 = float(input("Please enter your first endpoint for x: "))
y1 = float(input("Please enter your first endpoint for y: "))
x2 = float(input("Please enter your second endpoint for x: "))
y2 = float(input("Please enter your second endpoint for y: "))

x = (x1 + x2) / 2
y = (y1 + y2) / 2

print("Your midpoints are, ({},{}).".format(x, y))
