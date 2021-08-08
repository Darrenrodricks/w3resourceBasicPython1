# Write a Python program to calculate body mass index.
height = float(input("please enter your height in feet: "))
w = float(input("Please enter your weight in kgs: "))
ms = height * 0.3048
final = round(w / (height ** 2), 2)
print("Your Body Mass Index is {}".format(final))
