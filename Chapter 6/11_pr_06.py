text = input("Enter your text: ")

text1 = text.capitalize()

num1 = text1.find("Harry")
num2 = text1.find("harry")


if (num1==-1 and num2==-1):
    print("Not talking about Harry")
else:
    print("Talking about Harry")