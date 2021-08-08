# Write a Python program to create a histogram from a given list of integers.
def histogram_generator(items):
    for i in items:
        output =''
        times = i
        while (times > 0):
            output += "*"
            times = times - 1
        print(output)

histogram_generator([1,2,3,4,5,6])

