# prime number using functions

#find if the number is prime or not using function 
def prime(num): 
    if num> 1:   
        for n in range(2,num):   
            if (num % n) == 0:   
                return False 
        return True 
    else: 
        return False 
print(prime(8)) 
print(prime(5))