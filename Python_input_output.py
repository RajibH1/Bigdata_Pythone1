# Declare & Assign variable
int_var = 60
float_var = 18.25
string_var = 'ineuron batch2' # or another way "ineuron batch2"
bool_var = True

# Function in python for output
# Function does what? They might or might not accept some parameter
print("Hello World", int_var,float_var ,string_var,bool_var)
print("Value of int_var = ", int_var)
print("Value of float_var = ", float_var)
print("Value of string_var = ", string_var)
print("Value of bool_var = ", bool_var)

# How to check the variable type in python
# We can use type () function 
print("Type of int_var ?", type(int_var))
print("Type of int_var ?", type(float_var))
print("Type of int_var ?", type(string_var))
print("Type of int_var ?", type(bool_var))


## type casting in pythone ?
int_var = int_var + 10
print(int_var)

casted_float_var = int(float_var)
print("Type of casted_float_var ?", type(casted_float_var))

numeric_str = "123"
numeric_str = int(numeric_str) + 50

print(numeric_str)

name = input("Please intput your name: ")
age = input("Please intput your age: ")
