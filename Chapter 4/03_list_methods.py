l1 = [1, 8, 7, 2, 21, 15]
print(l1)
l1.sort() # sorts the list
print("Sorted: ", l1)
l1.reverse() #reverses the list
print("Reversed: ",l1)
l1.reverse() 
print("Reversed 2: ",l1)

l1.append(45) # adds to the end of the list
print ("Append", l1)

l2 = [1,5, 4, 10]
l1.append(l2) # l2 (list) will be added
print("Append 2", l1)

l1.insert(0, 100) # Inserts 100 at 0-(position)
print("Inserted", l1)

l1.pop(2)  # removes item from position 2
print("Popped", l1)

l1.remove(7)  # removes 7 from the list
print("Removed", l1)
