info=["Prachi","Kinekar",8766079061,22,55]

# dictionary
info={
    "firstname":"Prachi",
    "Lastname":"Kinekar",
    "Mobilenum":8766079061,
    "age":22,
    "rollno":27
}

print(info["firstname"])
print(info["Lastname"])


names=["Prachi","vaish","Krish"]
print(type(names))

# does list stores the value by index--yes
# retrive
print(names[0])
print(names[2])

# update
names[0]="Shreya"
print(names[0])

# add
names.append("Radha")
print(names)

# insert: add at index 1  and move the value to next index
names.insert(1,"Ritu")
print(names)

# delete ---pop deletes last element
names.pop()
print(names)

# remove-removes specific value
names.remove("Shreya")
print(names)


# does list allows to store duplicate values ?--yes list allows to store duplicate values

names.append("Krish")
print(names)

# how many elements in list 
print(len(names))


# for - range
for x in range(len(names)):
    print(names[x])


# while
i0=0
while (i0<len(names)):
    print(names[i0])
    i0=i0+1

# for each
numA=[11,22,33,44,55,66]
for y in numA:
    print(y)


vehicle={
    "color":"red",
    "type":"Xuv",
    "price":700000
}

for key in vehicle:
    print(key,vehicle[key])