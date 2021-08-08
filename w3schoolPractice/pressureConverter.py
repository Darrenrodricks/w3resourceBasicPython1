# Write a Python program to convert pressure in kilopascals to pounds per square
# inch,a millimeter of mercury (mmHg) and atmosphere pressure.
kpa = float(input("Input pressure in in kilopascals "))
psi = kpa / 6.89475729
mmhg = kpa * 760 / 101.325
atm = kpa / 101.325
print("The pressure in pounds per square inch: {}".format(psi))
print("The pressure in millimeter of mercury: {}".format(mmhg))
print("Atmosphere pressure: {}".format(atm))
