comment = input("Enter Your Comment: ")

b = comment.find("make a lot of money")
c = comment.find("buy now")
d = comment.find("subscribe this")
e = comment.find("click this")

if ( b==-1 and c==-1 and d==-1 and e==-1):
    print("Not Spam!")
else :
    print("Spam!")