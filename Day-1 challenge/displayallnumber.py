arr = [map(int, input("Enter numbers separated by space: ").split())]
for i in arr:
    if(i%10 != 0):
        print(i, end=' ')
