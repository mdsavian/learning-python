name = 'Marlon'
print("Hello %s" % name)

age = 28

print('%s is %d years old.' % (name,age))

# print a list or a integer with %s, it converts the object

print('A list %s ' % [1,2,3])
print('An int %s ' % 100)

# %d numbers
print('number %d' % 100)

# %f floats
print('float %f' % 10.50)
print('float with limited decimals (3) %.3f' % 10.50)

#You will need to write a format string which prints out the data using the following syntax: Hello John Doe. Your current balance is $53.44.

data = ("John", "Doe", 53.44)

print("Hello %s %s. Your current balance is $%f." % data)