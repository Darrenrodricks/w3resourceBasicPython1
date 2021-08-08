# Write a Python program to prove that two string variables of same value point same memory location.
a = 100
b = 100

print("memory 1:", hex(id(a)))
print("memory 2:", hex(id(b)))
print()