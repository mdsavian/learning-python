number = 1+2*3/4.0

print(number)

# to get the remainder of division we use the % operator
remainder = 11 % 3
print(remainder)

# two * ( ** ) makes a power 
poweredTwo = 2**2
print(poweredTwo)

# form multiple strings multiplicating it
multipleString = 'hello ' * 10
print(multipleString)


# join lists with + operator
firstNumbers = [1,2,3]
lastNumbers = [8,9,10]

print(firstNumbers + lastNumbers)

# we can use the multiplication operator to multiple the elements of a list
# we are not multipling the array, just the elements

print([1,2,3]*2) # [1,2,3,1,2,3]


# The target of this exercise is to create two lists called x_list and y_list, which contain 10 instances of the variables x and y, respectively. 
# You are also required to create a list called big_list, which contains the variables x and y, 10 times each, by concatenating the two lists you have created.

x = object()
y = object()

x_list = [x] *10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")