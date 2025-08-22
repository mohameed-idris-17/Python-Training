arr = list(map(int,input().strip().split(" ")))
max =9999
for i in arr:
    if max>i:
        max = i
print(max)