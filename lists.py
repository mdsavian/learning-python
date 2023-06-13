# lists

myList = []
myList.append(1)
myList.append(2)
myList.append(3)
myList.append(4)

print(myList[0])
print(myList[1])
print(myList[2])

for x in myList:
    print(x)

numbers = []
strings = ["My", "name", "is", "Marlon"]
names = ["John", "Eric", "Jessica"]

numbers.append(1)
numbers.append(2)
numbers.append(3)

for n in numbers:
    print(n)

for s in strings:
    print(s)

for name in names:
    print(name)

# slicing array
print(myList[2:4])

# unpacking
a, b, c, d = myList
print(a, b, c, d)

# getting the index and the position value using enumerate
for i, n in enumerate(myList):
    print(i, n)

# interate through two arrays
for n, name in zip(numbers, names):
    print(n, name)

# reversing array
numbers.reverse()
print(numbers)

# sorting
numbers.sort()
print(numbers)

# sortint reverse
numbers.sort(reverse=True)
print(numbers)

# with lambda function
names.sort(key=lambda name: len(name))
print(names)

# comprehension
newNames = [x for x in names if "e" in x]
print(newNames)

# create 2d arrays
arr = [[0] * 4 for i in range(4)]
print(arr)
