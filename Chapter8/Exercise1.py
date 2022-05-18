# Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None.
# Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

t = [1, 2, 3, 4, 5, 6]

def chop(listToChop):
    del listToChop[0]
    del listToChop[-1]
    return listToChop


def middle(middleOfList):
    middleOfList[1:-1]
    return middleOfList
