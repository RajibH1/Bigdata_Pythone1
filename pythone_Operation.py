# numeric operators in python
# + for multiplication 
# - for substractions 
# * for multiplication 
# / for float division 
# // for integer division 
# ** for power calculation 
# % for Modulus 

x = 5
y = 3

print ("Addition of x + y = ", x+y)
print ("subtriction of x - y = ", x-y)
print ("multiplication of x * y = ", x*y)
print ("float division  of x / y = ", x/y)
print ("integer division of x // y = ", x//y)
print ("power calculation  of x ** y = ", x**y)
print ("Modulus of x % y = ", x%y)
# some operation in string 
str_data = 'Rajib'
empty_str = ''

# concat operation for string 
full_name = str_data + " "+ "Hossen"
print("Full name = ", full_name)

# if we can use - as well (minus operation does not works for string)

# minus_str = "rajib" - "Hossen"
# print("Minus str = ", minus_str)

# check multiplication if works (it does not work)

mul_str = "rajib" * "Hossen"
print("mul_str str = ", mul_str)

 # multipli numeric string
mul_num_str = "rajib" * 5
print("mul_num_str str = ", mul_num_str)

# Assingment operation 

#  = , x = 5
#  += , x += 5 --> x = x + 5
#  -= , x -= 5 --> x = x - 5
#  *= , x *= 5 --> x = x * 5
#  /= , x /= 5 --> x = x / 5
#  //= , x //= 5 --> x = x // 5
#  %= , x %= 5 --> x = x % 5


# Comparison Operation ( we compare operands vales)
# == , Equal to condition, x == y
# != , Not Equal to condition, x != y
# < , Less than condition, x < y
# > , grater than condition, x > y
# >= , Less than Equel to condition, x >= y
# => , Grater than Equel to condition, x => y

a = 10
b = 5
print ("Result of a == b, ", a == b)
print ("Result of a != b, ", a != b)
print ("Result of a > b, ", a > b)
print ("Result of a < b, ", a < b)
print ("Result of a >= b, ", a >= b)
print ("Result of a <= b, ", a <= b)


# logical operation in python ( Logical check will happen for expression result)
# and -> Returns true if both statements are true  
# or -> Returns true if one of statement are true
# not -> Reverse the result, returns false if the result is true


m = 10
n = 8
print('m>10 and n<10', m>10 and n<10) # False and True -> False

print('m>10 or n<10', m>10 or n<10)  # False and True -> True

print('m>20 and n<10', m>20 and n<10)  # False and True -> False
