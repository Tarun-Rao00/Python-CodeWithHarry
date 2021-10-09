# creating  an empty set
b = set()
print(type(b))

# Adding values to an empty set
b.add(4)
b.add(5)
b.add(5)
b.add(5)  # adding a value repeatedly does not change the set
# b.add([4, 5, 6])  We can't add a list in a set as it is unhashable( Changeable)
b.add((4, 5, 6))  # we can add tupple in a set as it is unchangeable
# b.add({4:5}) We can't add a dictionary in a set as it is unhashable( Changeable)

print(b)

# LENGTH OF THE SET

print(len(b))  # Prints the length of set

# REMOVAL

b.remove(5)  # Removes 5 from set
# b.remove(15)  throws an error as 15 is not present in the set
print(b)

# POPS OUT A RANDOM ITEM

print(b.pop())
print(b)

# UNION

print(b.union({2,3,4,7,8}))


# INTERSECTION

print(b.intersection({2,3,4,5,8}))
