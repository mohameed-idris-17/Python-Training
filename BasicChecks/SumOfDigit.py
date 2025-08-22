num = int(input())
sum =0
while num>0:
    b = num%10
   # print(b)
    sum+=b
    num = num//10
    #print(num)
print(sum)