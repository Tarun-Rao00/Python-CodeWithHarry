# n = 4
# product = 1
# for i in range(n):
#     product = product * (i+1)

# print(product)

def fact_iter(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product

f = fact_iter(5)
print(f)