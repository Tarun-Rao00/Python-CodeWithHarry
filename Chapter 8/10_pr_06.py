def convert(inch):
    cm = inch * 2.54
    return cm


inch = float(input("Enter a value in Inches: "))
print(f"{inch} inch is equal to {convert(inch)} cm")
