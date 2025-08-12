marks = [map(int, input("Enter 25 subject marks separated by space: ").split())]
sum =0.0
for i in marks:
    sum += i
average = sum / 25
print("The average of the marks is:", average)