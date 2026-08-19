a=10
print(a)
b=12.4
print(b)
c=True
print(c)
d="Prachi"
print(d)
e=[11,22,33]
print(e)
f=12,
print(f)
print(type(f))
g={
    "firstname":"Prachi"
}

print(g)

# loop , hasValue , methods , CRUD

# set
setA={22,33,44,22}
print(setA)#33,44,22

setB={22,33,44,22}
print(setB)
# set does not stores duplicate values

# program 2
# does set stores value by index?_-No

setC={11,22,33,44,55}
# print(setC[0])---does not access
# setC[0]=111#---immutable --- tuple,set,string


setD={133,44,55,66}
print(44 in setD)
print(66 in setD)


# program 3
for item in setD:
    print(item)

# range() , while
# program 4
setJ={11,22,33,44,55,22,33}
print(len(setJ))

# program 5
setH={22,33,555,4434,665}
print(min(setH))
print(max(setH))
print(type(setH))

# methods of set
# add()
setA={11,22,33,44}
setA.add(88)
print(setA)

# clear()
# # setA.clear()
# print(setA)

# del setA
# print(setA)

# # pop()
# setA.pop()
# print(setA)

# remove
setA.remove(33)
print(setA)


# update_--it adds the ele it doesnot update the set  
setC={11,22,33,44,55}
setC.update({12,34,5,67,78})
setC.update({"String"})
setC.update({64,66667,7788})
print(setC)
print(len(setC))


# copy()
setG={11,22,33,44}
setN={33}
# setN=setG.copy()
# print(setN)#{11,22,33,44}
# print(setG)#{11,22,33,44}
# setG.remove(44)
# print(setN)#{11,22,33,44}
# print(setG)#-------{11,22,33}
setG=setN
setN.add(888)
print(setN)
print(setG)

