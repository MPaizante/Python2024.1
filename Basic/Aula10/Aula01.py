a = ["Matheu","Paizante","de","Araujo"]
x = sorted(a)
print(x)
b = [3,4,2,7,9,6,8,1,5]

print(sorted(a, reverse= True))
print(sorted(b,reverse=False))
print(sorted(b,reverse=True))
b.sort()
print(b)

lst = [3, 5, 1, 6, 7, 2, 9, -2, 5]
lst_sorted = sorted(lst, reverse= True)

l1 =[1,7,4,-2,3]
print('-'*20 )
def ab(x):
    if x >=0:
        return x
    else:
        return  -x

l2 = sorted(l1,key=ab)
print(l2)
print(sorted(l1,reverse= True, key= ab))

print('-----------------------------------------')



# Function to get the second letter of a string
def second_let(s):
    if len(s) >= 2:
        return s[1]
    else:
        return ''


# Function to get the last character of a string
def last_char(s):
    return s[-1]

# Given list of strings
nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

# Sorting the list by the last digit using the last_char function
nums_sorted = sorted(nums, key=last_char, reverse=True)

# Displaying the sorted list
print(nums_sorted)

