def product(num, i):
        pro = num*i
        final = f'{num} x {i} = {pro}'
        return final



for i in range(2,51):

    num = i
    with open(f"Tables\{i}", 'w') as f:
        for j in range(1,11):
            f.write(f'{product(num, j)}\n')
    


           


print("Task Done!!!")