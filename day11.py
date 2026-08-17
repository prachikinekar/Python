a=10
print(a)
print(type(a))

a=1000
print(type(a))
print(a)

b=10.5
print(b)
print(type(b))
# 10.4, -12.5,0.34

c=True
print(c)
print(type(c))


# collection
d="prachi"
print(d)
print(type(d))
d="Shreya"
print(d[0])#it is accessible but cannot be updated 


# list

numbers=[11,22,33,44,55]
numbers[0]=990
print(numbers)

dictA={
    "Firstname":"Prachi",
    "Lastname":"Kinekar"
}
print(dictA["Firstname"])
dictA["Firstname"]="Krish"
print(dictA)

# tuple

# define
a=11
print(a)
print(type(a))

b=11,22
print(b)
print(type(b))#tuple

c=(11,22)
print(c)
print(type(b))#tuple

# does tuple stores the value by index ??? - yes

names=("Prachi","Krish","Vaish")
print(names[0])

# can we update 1 single value ? No , fixed length 
# tuples are fixed length 
# names[0] = "samay"
# names[3] = "sham"

# particular value exist 

# names=("Prachi","Krish","Vaish")

# print("Prachi" in names)#true


# # number of elements
# print(len(names))
# print(max(11,22,33,44,55,889987))
# print(min(11,22,33,44,55,889987))


# # unpacking
# numbers=[11,22,33,44]
# a=numbers[0]
# b=numbers[1]
# c=numbers[2]
# print(a)
# print(b)
# print(c)

# a,b,c,d=numbers
# print(a)
# print(b)
# print(c)
# print(d)



number=(11,22,33,44)

# # for -range()
# for x in range(len(number)):
#     print(number[x])

# # while
# i0=0

# while (i0<len(number)):
#     print(number[i0])
#     i0=i0+1


# for each
for a in number:
    print(a)


numberB=(11,22,33,11)
q=numberB.count(11)
print(q)

v=11,22,33
print(v.index(11))

