# # program 1
# birthyear=[1999,1998,1997,1996,1995]
# age=[]

# for x in birthyear:
#     age.append(2026-x)
# print(age)

# # map()

# e=map(lambda x:2026-x,birthyear)
# print(list(e))

# # program 2
# numbers=[1,2,3,4,5,6,7,8,9,10]
# e4=list(map(lambda x:x*3,numbers))
# print(e4)

# program 3 

marks=[90,87,67,95,97,99,98]
above90=[]

for x in marks:
    if x>90:
        above90.append(x)
print(above90)

f=filter(lambda x:x>=90,marks)
print(list(f))

# progam 3
transactions=[90,45,66,-199,45,66,77,-67,78,12,-34]
deposit=list(filter(lambda x:x>0,transactions))
print(deposit)
withdrawal=list(filter(lambda x:x<0,transactions))
print(withdrawal)


# program 4
arr=[11,22,33]
total=0

for x in arr:
    total=total+x

print(total)

from functools import reduce
e2=reduce(lambda total,x:total+x,arr,5)
print(e2)