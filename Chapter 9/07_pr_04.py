with open('donkey.txt', 'r') as f:
    text = f.read()

print(text)
new = text.replace('donkey','######')
print(new)

with open('donkey.txt', 'w') as f:
    f.write(f'{str(new)}')
