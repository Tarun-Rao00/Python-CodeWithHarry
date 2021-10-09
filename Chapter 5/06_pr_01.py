myDict = {
    "Pankha" : "Fan",
    "Darwaja" : "Door",
    "Hawa" : "Air",
    "Badal": "Clouds",
    "Aasmaan" : "Sky"

}

print("options are ", myDict.keys())
a = input("Enter the hindi word\n")

# Below line will not throw an error if the key is not present the Dictionary
print("The meaning of your word is:\n", myDict.get[a])