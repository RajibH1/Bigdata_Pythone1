
# How to use the break statement 
int_list = [1,5,7,8,19,13,17,3]

# Find the enen value in the given list 

for num in  int_list :
    print(num)
    if num % 2 == 0:
        print("Even number in the list= ", num)
        break

# if break is removed ?
for num in  int_list :
    print(num)
    if num % 2 == 0:
        print("Even number in the list= ", num)

# How to use continue keyword?
# Print the numbers from for loop and start them from value one 
# But print values on terminal if number is grater than 10

for num in range (1,21):
    if num  < 10:
        continue 
    print (num)

# if there in not any continue 

for num in range (1,21):
    if num  < 10:
        continue
    print (num)
