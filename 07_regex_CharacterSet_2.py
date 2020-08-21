import re

# We will move from bigger character set metacharacter to more granular one.
#
# [.]     = [a-z][A-Z][0-9] & any other symbol - [*%$#):;], except \n.
# [\w]    = [a-z][A-Z][0-9][_]
# [\W]    = opposite of \w. Represents anything other than: [a-z][A-Z][0-9][_]
# So, we can say
# [.] & \n == [\w] & [\W]
#
# [\d]      = [0-9] Matches any digit
# [\D]      = Opposite of \d. Matches any non-digit character.
#
# [\s]      = Matches any white space character
# [\S]      = Opposite of \s. Matches any non-white space character

match_object = re.findall('\D', 'ab cd&87*s\nda%3#23')
print(match_object)
# output is: ['a', 'b', ' ', 'c', 'd', '&', '*', 's', '\n', 'd', 'a', '%', '#']
match_object = re.findall('\d', 'ab cd&87*s\nda%3#23')
print(match_object)
# output is: ['8', '7', '3', '2', '3']
#
# You can test for \s and \S
#
# Look at below some.
#
s = '''This is me.
I am this.
I am everywhere.'''
match_object = re.findall('.+', s)
print(match_object)
# output is: All lines in
match_object = re.search('.+', s)
print(match_object)
# output is: first line.
