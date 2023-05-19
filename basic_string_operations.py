myString = "hello world"
# check size
print('string size %d' % len(myString))

#index of letter
print("index of letter %d" %myString.index('o'))


#count how many letters, words on string
print("count how many letters on string %d" %myString.count('l'))

# slicing string using []

print("from 3 to 6 %s" % myString[3:7])
print("just 3 %s" % myString[3])
print("untill index 6 - without using the first %s" % myString[:7])
print("using negative to start at the end %s" % myString[:-7])

# using stride parameter, it refers to how many character to move forward after the first chart is retrieved from string
print("without stride parameter '%s' with stride parameter '%s'" % ("abcdefg"[0:7], "abcdefg"[0:7:2]))
