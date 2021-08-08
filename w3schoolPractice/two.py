# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the
# user. Hint: how does an even / odd number react differently when divided by 2?

int = int(input("Please enter a number."))

new_int = int % 2

if new_int > 0:
    print("you picked an odd number")
else:
    print("you picked an even number")