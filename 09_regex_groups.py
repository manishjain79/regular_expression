import re
#
# groups allow us to pull out sections of a match and store them.
#
string = 'John has 6 cats but I think my friend Susan has 3 dogs and Mike has 8 fish'
match_object = re.findall('\w+ \w+ \d+ \w+', string)
# print(match_object)
# output is: ['John has 6 cats', 'Susan has 3 dogs', 'Mike has 8 fish']
#
# Instead of \w to match words in our string, we could have given the following as well:
# match_object = re.findall('[A-Za-z]+ [a-z]+ \d+ [a-z]+', string)
# using /w in our case was much simpler.
#
# How to group?
# ()    = Parentheses allows the selection to put in groups.
match_object = re.findall('(\w+) \w+ \d+ \w+', string)
# print(match_object)
# output is: ['John', 'Susan', 'Mike']
match_object = re.findall('(\w+) \w+ (\d+ \w+)', string)
print(match_object)
# output is: [('John', '6 cats'), ('Susan', '3 dogs'), ('Mike', '8 fish')]
#
# With method findall() we do not have much of an option to do anything in terms of groups. It just extract out the
# match into a python list.
# But then, we can use python list function/methods to manipulate the information in match_object variable.
# try the following:
for i in zip(*match_object):
    print(i)
# output is:
# ('John', 'Susan', 'Mike')
# ('6 cats', '3 dogs', '8 fish')
# If your list contains multiple lists or multiple tuples,
# then if you zip them with '*' followed by name of the list, the outer list elements will be expanded into
# smaller list.
# To show how a normal basic zip functionality,
a = [1, 2, 3]
b = ['pencil', 'eraser', 'ruler']
for i in zip(a, b):
    print(i)
# output is:
# (1, 'pencil')
# (2, 'eraser')
# (3, 'ruler')
# zip needs to lists or tuples in order to zip them, so when we applied *match_object, the internal lists of
# match_objects were expanded into smaller tuples and zip a valid function.
#
# This time we made three groups. And see how the information changed.
match_object = re.findall('(\w+) \w+ (\d+) (\w+)', string)
for i in zip(*match_object):
    print(i)
# output is:
# ('John', 'Susan', 'Mike')
# ('6', '3', '8')
# ('cats', 'dogs', 'fish')
#
# Again mentioning that we are applying for loop and zip to print out the extracted result from group because of
# findall() method's limited functionality.
#
# Lets explore search.
match_object = re.search('(\w+) \w+ (\d+) (\w+)', string)
print(match_object)
# output is: <re.Match object; span=(0, 15), match='John has 6 cats'>
# Because search matches first occurrence of the matched pattern.
# 1.
# group() or group(0)   =   pulls out the entire match.
print(match_object.group(0))
# output is: John has 6 cats
print(match_object.group())
# output is: John has 6 cats
# 2.
# groups()      =   pulls out information of all the groups as separate element of tuple.
print(match_object.groups())
# output is: ('John', '6', 'cats')
# we had three groups.
#
# 3.
print(match_object.group(1))
# output is: John
#
# 4.
print(match_object.group(2))
# output is: 6
#
# 5.
print(match_object.group(3))
# output is: cats
#
# 6.
# You can print a group multiple time and in any order.
print(match_object.group(3,1,2,1,1))
# output is: ('cats', 'John', '6', 'John', 'John')
#
#
# Similarly, we can use span(), start(), end() methods as well.
print(match_object.span())
# output is: (0, 15) <- Gives index value for the entire match.
#
print(match_object.span(1))
# output is: (0, 4)
print(match_object.span(2))
# output is: (9, 10)
print(match_object.span(3))
# output is: (11, 15)
#
#
print(match_object.start())
print(match_object.end())
print(match_object.start(1))
print(match_object.end(1))
print(match_object.start(2))
print(match_object.end(2))
print(match_object.start(3))
print(match_object.end(3))
#
#
#
# Note: findall does'nt have group() methods. We will have to apply python list and tuple methods in order
# to extract information from findall() hits.
#
# Making group of group
match_object = re.findall('((\w+) \w+ (\d+) (\w+))', string)
print(match_object)
# Well, in this pattern, we have four groups.
# First we created three groups. And then, we engulfed all of these three groups into one bigger group.
# In other words, we created a group of group.
# So, how the hits will be put into group.
# First the hit will present the information into bigger group followed by it smaller groups.
# The output of above is:
# [('John has 6 cats', 'John', '6', 'cats'), ('Susan has 3 dogs', 'Susan', '3', 'dogs'), ('Mike has 8 fish', 'Mike', '8', 'fish')]
#
# Since we used findall() method, we cannot use group() method.
# We have to use python list/tuple operations to take out the information.
#
for i in match_object:
    print(i[0])
# output is:
# John has 6 cats
# Susan has 3 dogs
# Mike has 8 fish
# We can print out i[1], i[2] etc.....
# Let's try search method.
match_object = re.search('((\w+) \w+ (\d+) (\w+))', string)
print(match_object)                 # <re.Match object; span=(0, 15), match='John has 6 cats'>
print(match_object.group())         # John has 6 cats
print(match_object.groups())        # ('John has 6 cats', 'John', '6', 'cats')
print(match_object.group(1))        # John has 6 cats
print(match_object.group(2))        # John
print(match_object.group(3))        # 6
print(match_object.group(4))        # cats.
#
# So, essentially there are four groups and
# groups() prints out all the groups.
# group() - prints out only the match.
