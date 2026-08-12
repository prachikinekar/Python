info={
    #property:value
    #key:value
    "firstname":"Prachi",
    "Lastname":"Kinekar",
    "Age":22,
    "rollno":27
}

print(info)
print(type(info))

# does dictionary stores the value by index ?--no
# print(info[0])
# retrive
q1=info["Lastname"]
print(q1)

# update
info["Lastname"]="Chaudhari"
print(info)

# add
info["Language"]="English"
print(info)

# pop
info.pop("Age")
print(info)



# program 2
vehicle={
    "color":"red",
    "type":"sedan",
    "year":2026,
    "color":"blue"
}

print("color" in vehicle)#True

print("Color" in vehicle)#FALSE


for key in vehicle:
    print(key)#key
    print(vehicle[key])#values

# program 3
student={
    "firstname":"Prachi",
    "lastname":"Kinekar",
    "age":22,
    "Rollno":27
}

print(student["firstname"])
print(student["lastname"])
print(student.get("age"))


# get--------even if the key doesnt exsist  it will give none
# print(student['language'])#execution halt
print(student.get('language'))#None
print("bye")


# clear()
student.clear()
print(student)#{}

# program 6
student={
    "firstname":"Prachi",
    "lastname":"Kinekar",
    "age":22,
    "Rollno":27
}

student.pop("firstname")
print(student)

# popitem:removes the last key and value of dict
student.popitem()
print(student)

# program 7
student={
    "firstname":"Prachi",
    "Lastname":"Kinekar",
    "age":22,
    "rollno":27
}

for x in student.keys():
    print(x)

for x in student.values():
    print(x)

for x in student.items():
    print(x)


# setdefault:is use to add key and value pairs or set the value 
# if property exist will return its value , else will set the default value

print(student.setdefault('age',22))
# if property does not exist ?
print(student.setdefault('city','pune'))
print(student)

# program 8
print(dict.fromkeys(["key1","key2","key3","key4"]))


student={
    "firstname":"Prachi",
    "Lastname":"Kinekar",
    "age":22,
    "rollno":27
}

studentA=student
studentA["firstname"]="Shrey"

print(studentA)
print(student)
#both will have same values as there memory add are same 


e=[11,22,33]
e1=e
e1[1]=33
print(e1)
print(e)
