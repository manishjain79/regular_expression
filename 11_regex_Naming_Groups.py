import re
# There are times when your pattern grows very big and you may have so many groups.
# It is good to give names to them ; some meaningful names.
string = "Tehsil Jagraon, Dist LDH Punjab, 142026"
match = re.search('(?P<CITY>[A-Za-z\s]+),(?P<STATE>[A-Za-z.\s]+), (?P<PINCODE>\d+)', string)
# match = re.search('(\w+ \w+), (\w+)', string)
# print(match.group())
print(match.group('CITY'))
print(match.group('STATE'))
print(match.group('PINCODE'))
# output is:
# Tehsil Jagraon
#  Dist LDH Punjab
# 142026
#
# The syntax is to prepend group RE with ?<'Group_Name'>.
# The Group Name does'nt take space in-between.
# And in syntax, it must be enclosed with quotes.

# There could be chances you want to list out the group names in order to look through first.
# Or, you forgot the names of the group.
print(match.groupdict())
# output is: {'CITY': 'Tehsil Jagraon', 'STATE': ' Dist LDH Punjab', 'PINCODE': '142026'}
match_dic = match.groupdict()
print(type(match_dic))
# output is: <class 'dict'>
for i in match_dic:
    print(i,":", match_dic[i])
# output is:
# CITY : Tehsil Jagraon
# STATE :  Dist LDH Punjab
# PINCODE : 142026

