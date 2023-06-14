myMap = {}

myMap["alice"] = 90
myMap["bob"] = 80
print(myMap)
print(len(myMap))

myMap["alice"] = 100
print(myMap["alice"])

print("alice" in myMap)
myMap.pop("alice")
print("alice" in myMap)

myMap = {"alice": 10, "bob": 20}

# looping through maps

for key in myMap:
    print(key, myMap[key])

for val in myMap.values():
    print(val)

for key, val in myMap.items():
    print(key, val)
