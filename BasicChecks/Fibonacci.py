n = int(input())
f1,f2=0,1
print(f1,f2)
for i in range(n):
    f3 = f1+f2
    print(f3,end=" ")
    f1=f2
    f2=f3
