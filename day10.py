# slicing
# string[start:end(not included):step(1)]

# 0    1   2   3   4   5   6   7   8   9
# c    h   a   n   d   r   a   p   u   r
# -10 -9  -8   -7  -6  -5  -4  -3  -2 -1


city="Chandrapur"
print(city[0:2])
print(city[1::])
print(city[2:6:])
print(city[-8:7:])
print(city[-8:-1:])
print(city[1:-1:])
print(city[-1:-4])
print(city[::2])
print(city[::3])
print(city[::-1])

#list[start:end:step]
city=["pune","Mumbai","Nagpur","Banglore","Hyderabad","Chennai"]
# print(city[::-1])
print(city[2:6:])
print(city[2:6:2])
print(city[3:-1:1])