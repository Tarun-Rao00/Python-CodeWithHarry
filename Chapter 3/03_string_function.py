story = "once upon a time there was a youtuber Harry who uploaded free python course with handwritten notes"
name = "Tarun Rao"
name_small = "tarun Rao"

# String Functions
# Length
print(len(story))
print(len(name))
string = "This will number of characters in the string"
print(len(string))

# Endswith
print(string.endswith("ing"))
print(string.endswith("ING")) # Tells that endswith function is case sensitive
print(string.endswith("The"))

# Story Count
print("Number of 'a' in story :",story.count("a"))
print("Number of 'r' in story :",story.count("r"))

# Capitalise (Also decapitalizes other than first character- Changes  "small Capital" to "Small capital")
print(story.capitalize())
print(name_small.capitalize()) 

# Find Function (Tells the position of a string, returns -1 if string is not present, tells the position of only first occurance)
print(story.find("uploaded"))
print(story.find("unknown"))

# Replace Function (Replaces all occurances)
print(story.replace("Harry","Tarun"))