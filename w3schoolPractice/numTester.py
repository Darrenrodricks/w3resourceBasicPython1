# Write a Python program to test whether a number is within 100 of 1000 or 2000

def numberTester(n):
    if 900 <= n <= 1100:
        print("Your value is within 100 of 1,000")
    elif 1900 <= n <= 2100:
        print("Your value is within 100 of 2,000")
    else:
        print("Your value is not within 100 of 1,000 or 2,000")



numberTester(20)
numberTester(890)
numberTester(900)
numberTester(901)
numberTester(1000)
numberTester(1030)
numberTester(1900)
numberTester(1950)
numberTester(2000)
numberTester(2050)