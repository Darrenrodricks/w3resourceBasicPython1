# Write a Python program to calculate the sum of the digits in an integer.

def getSum(n):
    sum = 0
    for num in str(n):
        sum += int(num)
    print(sum)

getSum(12345)



