import re

# We will move from bigger character set metacharacter to more granular one.
#
# [.]     = [a-z][A-Z][0-9] & any other symbol - [*%$#):;], except \n.
# [\w]    = [a-z][A-Z][0-9][_]
# [\W]    = opposite of \w. Represents anything other than: [a-z][A-Z][0-9][_]
# So, we can say
# [.] & \n == [\w] & [\W]
#
#
# '.' Matches any character except '\n'. Let's see this.
match_object = re.search('.', 'abcd')
print(match_object)
# output is: <re.Match object; span=(0, 1), match='a'>
match_object = re.search('.', '\nbcd')
print(match_object)
# output is: None. Because, it could not hit newline character.
match_object = re.search('.', '^bcd')
print(match_object)
# output is: <re.Match object; span=(0, 1), match='^'>
match_object = re.search('.', '*bcd')
print(match_object)
# output is: <re.Match object; span=(0, 1), match='*'>
match_object = re.search('.', ' bcd')
print(match_object)
# output is: <re.Match object; span=(0, 1), match=' '>. It matched space.
# [.] = [a-zA-Z0-9] & any other symbol, except \n.
# with match() and search() the output remains same.
# But if I use, findall(), it will find all instances of 'any-character'
match_object = re.findall('.', ' bcd')
print(match_object)
# output is: [' ', 'b', 'c', 'd']
# '\w' Matches alphanumeric characters only and underscore. It doesn't match any other character.
# ['\w'] = [a-zA-Z0-9_]
match_object = re.match('\w', 'abcd')
print(match_object)
# output is: <re.Match object; span=(0, 1), match='a'>
match_object = re.match('\w', '\nbcd')
# print(match_object)
# output is: None. Because, it could not hit newline character. But if I would apply search() method instead
# it would have skipped all miss (in this case \n) and would have had a hit on b.
# with search() output is: <re.Match object; span=(1, 2), match='b'>
match_object = re.match('\w', '^bcd')
print(match_object)
# output is: None
match_object = re.match('\w', '*bcd')
# print(match_object)
# output is: None
# match_object = re.match('\w', ' bcd')
# print(match_object)
# output is: None
match_object = re.findall('\w', 'ab cd&87*sda%3#23')
# print(match_object)
# output is: ['a', 'b', 'c', 'd', '8', '7', 's', 'd', 'a', '3', '2', '3']
match_object = re.findall('\w\w', 'ab cd&87*sda%3#23')
# print(match_object)
# output is: ['ab', 'cd', '87', 'sd', '23']


print(match_object)
# output is: ['b ', 'd&', '7*', 'a%', '3#']
