
# write a code to print from 1 to 10

for i in range(1,10):
    print(i)

# print odd numbers start from 1 to 10 

for i in range(1,11,2):
    print(i)

# print numbers start from 10 to 1 

for i in range(10,0, -1):
    print(i)

# write  a program to calculate the sum of given list ekements using for loops 
int_list = [4,8,-2,10,5]
output = 0
for i in int_list:
    output = output + i
print("Totoal of the sum is: ",output)
