arr = [map(int,input().split())]
for i in range(len(arr)):
    for j in range(i,len(arr)):
        if(arr[i]==arr[j]):
            print(arr[i])