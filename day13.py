# setA={11,22,33}
# setB={44,55,66,11,22}
# setC=setA.intersection(setB)#common from setA and setB
# print(setA)
# print(setB)
# print(setC)

# # program 2
# setA={11,22,33}
# setB = {44,55,66,11,22}

# # setA.intersection_update(setB)#there will be change in A only
# # print(setA)
# # print(setB)


# setB.intersection_update(setA)
# print(setA)
# print(setB)#there will be change in B only


# # program 2
# setD={22,33,44,77}
# setE={55,66,77,44}

# print(setD.difference(setE))#{22,33}
# print(setE.difference(setD))#{55,66}


# print(setD)
# print(setE)


# program 3
# # symmetric diff and symmetric diff update
# setG={44,55,66,99}
# setH={66,77,88,99}

# # print(setG.symmetric_difference(setH))#{55, 88, 44, 77}
# # print(setH)
# # print(setG)

# setH.symmetric_difference_update(setG)
# print(setH)#{55, 88, 44, 77}
# print(setG)#{44,55,66,99}

# program 4
# disjoint --return True when there is null intersection

# setH={11,22}
# setJ={12,44,77}
# print(setH.isdisjoint(setJ))#True

# setA={11,22}
# setB={11,22,33,44}
# print(setA.issuperset(setB))#False
# print(setB.issuperset(setB))#true
# print(setA.issubset(setB))#true
# print(setA.union(setB))#Return a new set with elements from the set and all others.


setA={11,22}
setA.discard(22)
print(setA)

# discard() and remove()

