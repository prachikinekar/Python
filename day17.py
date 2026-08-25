# # default parameter 
# def addA(x=10,y=7):
#     print(x+y)
# addA(12,3)
# addA()

# # # positional arguments
# # y=20
# # x=30

# def subB(x,y):
#     print(x-y)
# subB(y=90,x=30)


# # *args
# def addAll(*args):
#     print(args)
#     total=0
#     for x in args:
#         total=total+x
#     return total
# e=addAll(2,3,4,5,6,7)
# print(e)


# # kwargs
# def addCity(**kwargs):
#       print(kwargs)
#       kwargs['city']='pune'
#       kwargs.update({"language":"marathi"})
#       return kwargs
# e5=addCity(fn="Prachi",ln="Kinekar")
# print(e5)


# # operation with every ele of list

# birthYear=[2002,2003,2004,2005]
# ages=[]

# for x in birthYear:
#     ages.append(2026-x)
# print(ages)


# filtering
marks=[35,52,23,12,98,78]
above35=[]

for x in marks:
    if x>35:
        above35.append(x)
print(above35)


# sum of all elements of list
nums=[11,22,33,44]
total=0

for x in nums:
    total=total+x

print(total)