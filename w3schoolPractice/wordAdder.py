# Write a Python program to get a string which is n (non-negative integer) copies of a given string.

def wordAdder(str, i):
    final = " "
    for i in range(i):
        final = str + final
    print(final)

wordAdder("monkey", 7)