# a=10
# b=5
# print(a+b)
# print(a-b)
# print(a*b)
# print(a%b)

# print("--------------------")
# c=6
# d=3

# print(c-d)
# print(c+d)
# print(c*d)
# print(c%d)

# print("--------------------")
# def Calculator(x,y):
#    print(x+y)
#    print(x-y)
#    print(x*y)
#    print(x/y)
#    print(x%y)

# Calculator(7,8)
# Calculator(10,8)


# # int as parameter and int as return int
# def CalA(x,y):
#    return x+y
# e=CalA(12,3)
# print(e)

# print("--------------------")

# #  float as parameter and float as return int
# def CalB(a,b):
#    return a-b
# k=CalB(2.7,1.2)
# print(k)

# boolean as a parameter and boolean as return type

# def CanDrive(age,haveVehicle):
#    if age>=18 and haveVehicle:
#       return True
#    else:
#       return False

# f=CanDrive(21,True)
# print(f)

# # string a parameter and string as return type 
# def Greet(word):
#    return "hello"+word
# g=Greet("Prachi")
# print(g)


#  # list as a parameter and list as a return type 
# city=["Mumbai","Pune","Hyderabad"]
# def addCity(lst):
#    lst.append("Nagpur")
#    return lst
# city2=addCity(city)
# print(city2)


# dict as a parameter and dict as a return type 

# info={
#    "firstname":"Prachi",
#    "lastname":"Kinekar"
# }

# def addCity1(info):
#    info["city"]="Pune"
#    return info

# a=addCity1(info)
# print(a)


# # Tuple as a parameter and tuple as a return type
# numbers=(11,22,33)
# def addToTuple(tupA):
#     tupA=list(tupA)
#     tupA.append(44)
#     tupA=tuple(tupA)
#     return tupA

# add=addToTuple(numbers)
# print(add)