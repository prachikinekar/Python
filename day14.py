# lambda function
def addA(x,y):
    return x+y

e=addA(12,3)
print(e)

# lambda-keyword
# x,y-parameter
# return-x+y


addB=lambda x,y:x+y
e2=addB(12,3)
print(e2)

square=lambda x:x*x
e3=square(3)
print(e3)

cube=lambda x:x*x*x
e4=cube(8)
print(e4)


# int as parameter , int as return 
# float as parameter and float as return 
# string as paramter and string as return 
# dict as paramter and dict as return 
# list as paramter and list as return 
# tuple as paramter and tuple as return 
# set as paramter and set as return 
# boolean as paramter and boolean as return 

# function as a parameter function as return

# addA=lambda x,y:x+y
# print(addA)
# print(addA(1,2))


# c=20
# print(c)


# function as a parameter
# addA=lambda x,y:x+y
# def addition (fn,x,y):
#     e4=fn(x,y)
#     return e4

# e5=addition(addA,11,2)
# print(e5)


# subB=lambda x,y:x-y
# def substraction(fn,x,y):
#     e6=fn(x,y)
#     return e6

# e6=substraction(subB,12,6)
# print(e6)


# mulA=lambda a,b:a*b
# def multi(fn,a,b):
#     e6=fn(a,b)
#     return e6

# e7=multi(mulA,4,5)
# print(e7)


# function as return type
def multiplication():
    return lambda x,y:x*y

e7=multiplication()
print(e7)

e9=e7(9,7)
print(e9)

def division():
    return lambda x,y:x%y
e10=division()
print(e10)

e13=e10(5,6)
print(e13)