mySet = set()

mySet.add(1)
mySet.add(2)
print(mySet)

print(1 in mySet)
print(2 in mySet)
print(3 in mySet)

mySet.remove(2)
print(mySet)

# list to set
print(set([1, 2, 3, 4]))

# comprehension
mySet = {i for i in range(5)}
print(mySet)
