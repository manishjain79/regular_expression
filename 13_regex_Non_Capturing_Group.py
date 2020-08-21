import re
string = '1234 9876'
match = re.findall('((\d)+)', string)
# print(match)
# output is: [('1234', '4'), ('9876', '6')]
# It printed out bigger group of first match and then final occurrence of smaller group. And same for second match.
#
# You do not get confuse. Remember that findall() method would have captured all the matches if we hadn't put pattern
# into groups.
# Let's see the following, probably repeating from findall() education:
string = '1234 9876'
match = re.findall('\d+', string)
# print(match)
# output is: ['1234', '9876']
#
# If I put my pattern into group.
match = re.findall('(\d)+', string)
print(match)  # ['4', '6']
match = re.findall('(\d+)', string)
print(match)  # ['1234', '9876']
# So, this is the group output. Probably we have seen it multiple times now. The group overwrites its value with
# next occurrence and keeps last occurrence. That's what group captured and gives us the output/result.
# Now Let's see the following:
# Prepend the group patter with ?: and it will become non-capturing group.
match = re.findall('(?:\d)+', string)
# In this case, since group is prepended with ?:, the value of the group will not be in result, rather what was
# used to make the group is in the output.
print(match)  # ['1234', '9876']
match = re.findall('(?:\d+)', string)
print(match)    # ['1234', '9876']
# This happens in this case because findall() did not had any other group to capture and result out.
# In other words, we can say that, if we make the only group a non-capturing group then the result will be the matches
# used to make group. But it won't display group value.
# But what if there are multiple groups and one of them is non-capturing ?
# In that case, only capturing group will be displayed.
# Let's see below example.
# I have the following string:
string = '123123 = Alex, 123456 = Danny, 123123123123 = Mike, 456456 = Randy, 132123 = Luis'
# What we want is, name of people who has IDs starting with 123.
# To capture the result, definitely we will need multiple groups:
# one that can capture entries starting with 123 and other that can only keep names.
# Finally, we have to print only names by making first group a non-capturing group.
match = re.findall('(?:123)+ = (\w+)', string)
print(match)
# ['Alex', 'Mike', 'Luis']
# We made first group a non-capturing group and the output of match only displays 2nd group value.
#
# Let's try the following to capture non-capturing group using search group() and groups() methods.

match = re.search('(?:\d+)', string)
print(match)            # <re.Match object; span=(0, 6), match='123123'>
print(match.groups())   # ()
print(match.group())    # 123123
#
# Essentially match is there. match='123123'
# Since it is a non-capturing group, there is no group. Hence the output: ()
# group() / group(0) is really not a group, but the match value. So it has the output of 123123.
# With above we understand that, really there are no groups that we can display.



