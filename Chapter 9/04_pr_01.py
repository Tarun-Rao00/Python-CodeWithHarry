f = open('poem.txt', 'r')
a = f.read()
f.close()

b = a.find('twinkle')

if b == -1:
    print('The given text does not contains TWINKLE')
else:
    print('Yes, the given text contains TWINKLE')



