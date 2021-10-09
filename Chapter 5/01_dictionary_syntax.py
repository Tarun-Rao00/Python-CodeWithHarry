myDict = {
    "Fast" : "In a Quick Manner",
    "Harry" : "A Coder",
    "Marks" : [1, 2, 5],
    "anotherdict" : {'Run' : 'Walk Fast'}
}

print(myDict['Fast'])
print(myDict['Harry'])
print(myDict['Marks'])
myDict['Marks'] = [45, 4, 7]   # Dictionary is mutable
print(myDict["Marks"])
print(myDict["anotherdict"])
print(myDict["anotherdict"]['Run'])