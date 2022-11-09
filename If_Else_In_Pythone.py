#How to use If-Else in pythone 

x = 10
y = 5
if x == y:
    print("It is correct")
else:
    print("Not correct")

# it is mandotory to use else block with if

a = 50
if a == 50 :
    print ("Yes, A is Equals to 50!!")
print("A is not Equel to 50")

# Nested if -else condition

marks = 65
if marks>90:
    print("Grade A+")
elif marks>=80 and marks<90:
    print("Grade A")
    
elif marks>=70 and marks<80:
    print("Grade B+")
elif marks>= 60 and marks<70:
    print("Grade B")
else:
    print("Grade C")
