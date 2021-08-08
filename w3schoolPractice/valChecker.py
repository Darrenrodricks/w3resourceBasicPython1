def value_checker(data_set, n):
    if n in data_set:
        print("True, this value is in the dataset")
    else:
        print("False, this value is not in the dataset")


value_checker([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7)
value_checker([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4)
