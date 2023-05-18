# Hello World
my_name = 'Marlon'
print("Hello and welcome " + my_name + "!")

# variables
myInt = 9
print(myInt)

myFloat = 9.5
print(myFloat)

newFloat = float(myInt)
print(newFloat)

# multiple assigns
a,b = 3,4
print("multiple assigns", a, b)


# check instance of

myString = 'hello'
myFloat = 10.0
myInt = 20

if isinstance(myFloat, float):
    print('is float')
if isinstance(myInt, int):
    print('is int')

if myString == 'hello':
    print('hello is string')

