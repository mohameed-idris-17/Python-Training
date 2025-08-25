#square the number using lambda function 
square = lambda x:x*x 
print(square(int(input())))
# find the maximum value of two numbers 
max_value = lambda x,y:x if x>y else y
print(max_value(100,90))
#square the each array numbers 
arr = [10,20,30,40,55]
square_arr = list(map(lambda X:X**2,arr))
print(square_arr)
#using the filter() return the true value based on condit ion
odd = list(filter(lambda x:x&1==1,arr))
print(odd)
#sort function in lambda  "Key" is the variable used to sort the array based on key value
dummy = [(1,'b',"idris"),(4,'c',"imthiyas"),(3,'a',"Ayesha")]
sort = sorted(dummy, key=lambda x:x[2])
print(sort)
#reduce() advance of lambda function it contain the variable called "acc" it return the value what is stored 
#to use the reduce() we need to import it from functools import reduce
from functools import reduce
numbers = [1,2,3,4,5]
# 3+3 = 6
# 6+4 = 10
# 10+5 = 15
sum_of_array = reduce(lambda acc,x:acc+x,numbers)
print(sum_of_array)
#find the max value in the array
max_number = reduce(lambda acc,x:acc if acc>x else x,numbers)
print(max_number)
