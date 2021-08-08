# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

name = input("Please enter your name: ")
split = name.split(' ')
new_name = reversed(split)
final = ' '.join(new_name)
print(new_name)

