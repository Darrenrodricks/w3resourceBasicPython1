# Write a Python program to accept a filename from the user and print the extension of that.
#
# Sample filename: abc.java

a = input("PLease enter your file name: ")
b = a.split('.')
print("Your file type is {}".format(b[1]))