myDict = {
    "fast" : "in a quick manner",
    "harry" : "a coder",
    "marks" : [1, 2, 5],
    "anotherdict" : {'run' : 'walk fast'},
    1: 2
}

#************************** DICTONARY METHODS *****************************

print(myDict.keys())    # Prints all keys
print(type(myDict.keys()))  # Prints the type (dict_keys)
print(list(myDict.keys()))   # Can be converted into list
print(myDict.values())   # Will print the values of all keys
print(myDict.items())   # Will print the values, keys for all content of dictionary
print(myDict)

updateDict = {
    "Lovish": "Friend",
    "harry" : "a dancer"
}
myDict.update(updateDict)
print(myDict)

print(myDict.get('harry'))  # Print the value associated with the key 'harry'
print(myDict['harry']) # print the value associated with the key 'harry'


print(myDict.get("harry2"))  #gives 'None' as 'harry2' is not present in the list
#print(myDict["harry2"])  #throws an error as 'harry2' is not present in list