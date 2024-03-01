ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_id = sorted(ids, key=lambda x: str(x)[-4:])
print(sorted_id)

# Given list of ID numbers

# Given list
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']

# Sorting the list by the second letter using lambda function
lambda_sort = sorted(ex_lst, key=lambda x: x[1])

# Displaying the sorted list
print(lambda_sort)
