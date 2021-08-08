# Write a Python program to convert the distance (in feet) to inches, yards, and miles.
feet = int(input("Please enter the distance in feet: "))
inches = (feet * 12)
yards = (feet / 3)
miles = (feet / 5280)

print("{} feet equates to\n{} inches\n{} yards\n{} miles".format(feet, inches, yards, miles))
