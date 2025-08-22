arr = list(map(int,input().strip().split(" ")))
max =0
for i in arr:
    if max<i:
        max = i
print(max)