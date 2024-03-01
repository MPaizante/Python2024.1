groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}
most_needed = sorted(groceries.keys(),key= lambda x : groceries[x],reverse=True)
print(most_needed)


# Function to get the last four digits of an ID number
def last_four(id_number):
    # Convert the ID number to a string and return the last four digits
    return str(id_number)[-4:]

# Given list of ID numbers
ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]

# Sorting the list by the last four digits using the last_four function
sorted_ids = sorted(ids, key=last_four)

# Displaying the sorted list
print(sorted_ids)



