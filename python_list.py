# Declaration emplty list

l1 = []
print(type(l1))

# Insert values in the list 

l1.append(5)
l1.append(6)
l1.append(7)
print(l1)

int_list = []
for num in range(1,20):
    int_list.append(num)
print(int_list)

# How to calculate a length of list?
len_of_list = len(l1)
print('Length of list is: ',len_of_list) 

list1 = [1,'Shashank',20,'Hi']

list2 = [1,'Shashank',20,'Hi']

print("lists are equele: ", list1 == list2)

list4 = [1,2,3,4,5]
list5 = [80,90,100,110]
result =  list4 + list5
print(result)


list6 = [10,15,20,25,30,35]
for i in list6:
    print(i)

# pint the thired eliment from the list
# syntex = list_name[index]
print(list6[2])
print(list6[0])
print(list6[4])

# what will happen?
print(list6[100])

list7 = [1,"Rajib",100]
# how to update the value in the list index item?
# Update Rajib to Rahul
print(list7)
list7[1] = "Rahul"
print(list7)

for index in range(0, len(list7)):
    print(list7[index])

lsit8 = [1,2,50,'Rajib',[6,6,6],'Rahul']
print(len(lsit8))

# difference between appand and extend 

list9 = [20,30,40]
list10 = ['hi',"Hello", 'Bye']
list9.append(list10)
list9.extend(list10)
print("The appand result is: ",list9)

list11 = [20,30,40]
list12 = ['hi',"Hello", 'Bye']
list11.extend(list12)
# print("The extent result1 is: ",list11)

# List slicing 
list13 = [20,30,40,50,60,80,90]
# Syntax -> list_name[start : end]
# end index is exclusive
print(list13[ 0 : ])
print(list13[ 3 : ])
print(list13[ : ])
print(list13[ : 4 ])
print(list13[ 2 : 6 ])
print(list13[ 0 : : 2]) # 3rd value is for step

# How to print the last value of the list?
print(list13[ len(list13) - 1 ])
print(list13[-1]) # negative index -1 means last element of the list

# Print second last element from the list??
print(list13[-2])

# print inout list in reverse direction
print(list13[-1 : : -1])
