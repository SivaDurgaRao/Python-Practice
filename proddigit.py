# product of a given digits using functions

def Product(n):
 
    product = 1
    while (n != 0):
        product = product * (n % 10)
        n = n // 10
    return product
 
n =int(input("Enter number:"))
print(Product(n))