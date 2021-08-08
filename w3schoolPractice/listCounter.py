# Write a Python program to count the number 4 in a given list.

def list_counter(nums):
    count = 0
    for num in nums:
        if num == 4:
            count += 1
    print(count)

list_counter([1,2,3,4,5,6,4,5,6,4,5,6,4])
list_counter([4,4,4,4,4,4,4,4,4,4,4,4,4,6])