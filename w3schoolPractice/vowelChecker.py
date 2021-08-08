# Write a Python program to test whether a passed letter is a vowel or not.

def is_vowel(char):
    all_vowels = 'aeiou'
    print(char in all_vowels)

is_vowel("c")


def vowel_checker(char):
    if char == "a":
        print("True")
    elif char == "e":
        print("True")
    elif char == "i":
        print("True")
    elif char == "o":
        print("True")
    elif char == "u":
        print("True")
    else:
        print("False")

vowel_checker('a')
vowel_checker('b')
vowel_checker('e')
vowel_checker('i')
