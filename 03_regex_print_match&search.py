import re
# you can print your match object as string output.
match_object1 = re.match('a', 'abcdef')
match_object2 = re.search('c', 'abcdef')

# A Match Object is an object containing information about the search and the result.
# Note: If there is no match, the value None will be returned, instead of the Match Object.
# So, in above two statements, match_object1 and match_object2 are two objects or kind 'Match Object'
# If we print them as it is, they will print out the entire object of match.
# ie. information about search and the result.
# The Match object has properties and methods used to retrieve information about the search, and the result:
#
# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match.
# The "group" feature of a regular expression allows you to pick out parts of the matching text.
# by default, when there is no group defined, that means, we asking print whole match using group(0).
# The above examples are not so complex, that the output is not in groups.
# But still, to extract such hit, we will have to call group() method of the match object
print(match_object1.span())  # output is: (0,1)
print(match_object2.string)  # output is: abcdef
print(match_object2.group())  # output is: c
print(match_object2.group(0))  # output is: c
# Note: If there is no match, the value None will be returned, instead of the Match Object.
#
match_object1 = re.search('d', 'abcdefghijk')
print(match_object1.group())
# output is: d
match_object1 = re.search('d.+', 'abcdefghijk')
print(match_object1.group())
# output is: defghijk
# . matches any character and + matches 1 or more previous listed character.
# In our case, previous listed character is '.' which is any character, so, all the characters matches .+ pattern.

# back to span()
# span() gives a tuple of index values. Actually we can extract those index values with start() and end() method
# of the match object.
print(match_object1.start())
# output is: 3
print(match_object1.end())
# output is: 11
