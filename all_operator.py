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
#AND operator
print("a       b     :  a and b")
print("_" *60)
print(f"0       0     :  {0 and 0}         # False")
print(f"0       1     :  {0 and 1}         # False")
print(f"1       0     :  {1 and 0}         # False")
print(f"1       1     :  {1 and 1}         # True")
print("_" *60)

#OR operator
print("a       b     :  a or b")
print("_" *60)
print(f"0       0     :  {0 or 0}         # False")
print(f"0       1     :  {0 or 1}         # True")
print(f"1       0     :  {1 or 0}         # True")
print(f"1       1     :  {1 or 1}         # True")
print("_" *60)

#NOT operator
print("a      :  not a ")
print("_" *60)
print(f"0      : {not 0}")
print(f"1      : {not 1}\n\n")


print("==" *30)
print("                        Membership operator                 "                       )
print("==" *30)
num_list = [1,2,3,4,5]
print (f"checking 3 is in list     :{3 in num_list}")
print (f"checking 5 is in list     :{5 in num_list}")
print (f"checking 6 is in list     :{6 in num_list}")
print (f"checking 6 is not in list :{6  not in num_list}")
print (f"checking 3 is not in list :{3 not in num_list}")



print("==" *30)
print("                        Identity operator                 "                       )
print("==" *30)
a = [1,2,3]
a = b
print("a = [1,2,3]\n a = b")
print(f"a is b     : {a is b}               #both a and b points same list object")
print(f"a is  not b: {a is not b}\n")     

a = [1,2,3]
b = [1,2,3]
print(f"a = {a}\nb = {b}")
print(f"a is  b    :{a is b}         #even though values are same they stored in different memory location")
print(f"a is not b :{a is not b}          #both have diffwrant memory location\n")       
print(f"a is not b :{a is not b}          #both have diffwrant memory location")       
