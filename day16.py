# function as  parameter and function as return type

# # sum of two number using lambda function

# addA=lambda x,y:x+y
# q1=addA(3,4)
# print(q1)

# # square of number using lambda function 
# square=lambda x:x*x
# q2=square(2)
# print(q2)

# # function as a paramete to another function

# mulA=lambda x,y:x*y

# def multiplication(fn,x,y):
#     e4=fn(x,y)
#     return e4

# af=multiplication(mulA,4,5)
# print(af)

# print("-------------------------")

# divC=lambda y,z:y/z

# def divisionC(fn,y,z):
#     e6=fn(y,z)
#     return e6

# k=divisionC(divC,7,2)
# print(k)


# print("-------------------------")

# # function as return type
# def AddA():
#     return lambda f,g:f+g

# a=AddA()
# j=a(35,5)
# print(j)

# default parameters
def addN(x=10,y=29):
    print(x+y)

addN()
addN(9,8)

# position arguments
def subN(k,l):
    print(k-l)
subN(3,4)
subN(l=90,k=97)


# y = 10
# x = 20

# *args
# d=[11,22,33,44]
# e=(1,2,3,4,5)

def addAll(*args):
    print(args)
    total=0
    for x in args:
        total=total+x
    return total
e0=addAll(12,2,3,4,5)
print(e0)