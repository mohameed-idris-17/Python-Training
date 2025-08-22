arr = list(map(int,input().strip().split(" ")))
sum ,count=0,0
for i in arr:
        count+=1
        sum += i
print(sum/count)