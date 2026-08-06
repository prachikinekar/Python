# print(1)
# print(2)
# print(3)
# print(4)

# 1 to 100
# for loop,while loop

# range(startindex,endindex(not included),stepsize)
# range(5)--->startindex-0,endindex-5,stepsize-1
# range(1,5)--->startindex-0,endindex-5,stepsize-1
# range(1,11,2)--->startindex-1,endindex-11,stepsize-2



# print-->0,4
# for x in range(5):
#     print(x)

# # print 1 to 5
# for x in range(1,6):
#     print(x)

# # print hello 3 times
# for x in range(3):
#     print("hello")
#     print("bye")

# # print 1 to 10
# for x in range(1,11):
#     print(x)

# # table of 2
# for x in range(2,21,2):
#     print(x)

# for x in range(1,11):
#     print(x*2)


# # print 5 to 1
# for x in range(5,0,-1):
#     print(x)

# # table of 3  rev
# for x in range(30,2,-3):
#     print(x)

# table of 3
# for x in range(3,31,3):
#     print(x)


# # table of 5
# for x in range(5,51,5):
#     print(x)

# table of 5 reverse
for x in range(50,4,-5):
    print(x)


# break statement with for python
for x in range(5):
    if x==3:
        break
    print(x)#0 1 2 

for x in range(1,6):
    print(x)#1 2 
    if x==3:
     break

# continue statement with for loop
for x in range(1,6):
   if x==3:
      continue
   print(x)#1 2 4 5


for x in range(5,0,-1):
   if x==3:
    continue
   print (x)#5 4 2 1

