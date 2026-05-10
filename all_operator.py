print("==" *30)
print("                        Basic Arithmetic Operation                  "                       )
print("==" *30)
a = 10
b = 4
subtraction = a-b
Multiplication = a*b
division = a/b
floor_division = a//b
modulus = a%b
exponent = a**b
print(f"{a}\n {b}")
print(f"addition          : {a+b}\nsubtraction       : {a-b}\nmultiplication    : {a*b}\ndivision          : {a/b}\nfloor_division    : {a//b}\nmodulus           : {a%b}\nexponent          : {a**b}")

print("==" *30)
print("                        Comparision Operator                  "                       )
print("==" *30)
a = 10
b = 15
print("a is equal to b                :",a==b)                 # False--because a value is less than b.
print("a is not equal to b            :",a!=b)             # True--a and b are having different values.
print("a is greater than b            :",a>b)              # False--a value is less than b.
print("a is greater than or equal to b:",a>=b) # False--Atleast one condition should satisfy,here both condition are false.
print("a is less than b               :",a<b)                 # True-- a value is less than b.
print("a is less than or equal to b   :",a<=b)    # True--here one condition is satisfied.


print("==" *30)
print("                         Logical Operator                 "                       )
print("==" *30)
#AND operation
print("a       b     :  a and b")
print("_" *60)
print(f"0       0     :  {0 and 0}         # False")
print(f"0       1     :  {0 and 1}         # False")
print(f"1       0     :  {1 and 0}         # False")
print(f"1       1     :  {1 and 1}         # True")
print("_" *60)

#OR operation
print("a       b     :  a or b")
print("_" *60)
print(f"0       0     :  {0 or 0}         # False")
print(f"0       1     :  {0 or 1}         # True")
print(f"1       0     :  {1 or 0}         # True")
print(f"1       1     :  {1 or 1}         # True")
print("_" *60)