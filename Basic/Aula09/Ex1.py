def mult(x,y=6):
    return  x * y

print(mult(5))


def greeting( name, greeting="Hello ", excl="!"):
    return greeting + name + excl

print(greeting("Bob"))
print(greeting(""))
print(greeting("Bob", excl="!!!"))



def sum(intx ,intz=5):
    return intz + intx


def test(required_integer, optional_boolean=True, dict1={2: 3, 4: 5, 6: 8}):
    if optional_boolean:
        if required_integer in dict1:
            return dict1[required_integer]
    else:
        return False


