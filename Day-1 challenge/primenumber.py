num  = int(input("Enter a number: "))
for i in range(2, int(n**0.5)+1):
    if num % i == 0:
        print(num, "is not a prime number")
        break
    else:  
        print("prime") 
    print(num, "is a prime number")