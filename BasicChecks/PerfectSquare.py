num = int(input())
s,e=0,num
while s<=e:
    mid = (s+e)//2
    val = mid*mid
    if val == num:
        print(mid)
        break
    elif val>num:
        e = mid-1
    else:
        s = mid +1