def checkingIfIn(x,direction = True, d ={'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if x in d:
            return True
        else:
            return False
    else:
        if x not in d:
            return True
        else:
            return False

