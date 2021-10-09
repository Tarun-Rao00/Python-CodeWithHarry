def remov(strg):
    word = input("Enter the word you want to remove: ")
    newStrng = strg.replace(word, "")
    newStrng1 = newStrng.strip()
    return newStrng1

strg = input("Enter your text: ")
print(remov(strg))


