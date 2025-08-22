num = int(input())
bo = True
for i in range(2,num**0.5):
    if num%i == 0:
        print("not a prime number")
        bo = False
        break
if(bo):
    print("prime number")