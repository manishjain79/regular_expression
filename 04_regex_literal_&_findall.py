import re

# In Previous discussions we have been trying to match literal c or d or n etc.
# Let's see the following
match_object = re.match('a|n|c', 'abcdefgh')
# Here, | command is OR.
# it says to find either of the three literals. And in this case, it is a True hit for match() method as it could
# find 'a' at the beginning of the string 'abcdefgh'
print(match_object)
# Similarly,
match_object = re.search('a|n|c', 'abcdefgh')
# will find either the three literal whichever hits first. In this case that would be again a.
print(match_object)

# Now, if we want to find all occurrences of pattern in the string ?
# This is where findall() method of re helps.

match_object = re.findall('d', 'abcdefgh dyu\n7tdiu')
print(match_object)
# output is: ['d', 'd', 'd']
# It found three occurrences of 'd'
# Also, the output from findall is not grouped. However, it gives list.
print(type(match_object))
# output is: class list.



