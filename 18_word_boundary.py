import re
string = 'cat catherine catholic copycat wildcat uncatchable'
# if we want to capture all occurrences of cat, we can simply write
match = re.findall('cat', string)
print(match)
# ['cat', 'cat', 'cat', 'cat', 'cat', 'cat']
#
# let's change the pattern a little bit.
match = re.findall('cat ', string)  # cat with space.
print(match)
# ['cat ', 'cat ', 'cat ']
#
# Let's change the pattern again.
match = re.findall(' cat ', string)  # cat with space.
print(match)
# []
#
# So, if we want the exact match of cat and it should not include any other instance of it, then,
#
match = re.findall(r'\bcat\b', string)  # cat with space.
print(match)
# ['cat']
# why it pulled out only cat. Essentially there is space character after cat.
# This is how /b works. before first \b and after second \b it will match any non-alphanumric.
# So, in above example, after second \b, there was space and it matched it and hance we got that output.
# But with all other occurrences of cat, there is an alpahnumeric character either before first /b or after second \b.
# take this example
string = '+cat catherine catholic copycat wildcat uncatchable'
match = re.findall(r'\bcat\b', string)  # cat with space.
print(match)
# output is: ['cat']
# there is a non-alphanumeric character before first & second /b which is + and a space
# hence we have a hit on first cat.
#
# Another nuance with \b is, immediately after first \b and just before second \b, it must be alphanumeric character.
# consider the following string.
string = '''@manish @manish2017 @manish2005 python@manish_jain'''
# Well I want to pull out first and last occurrences.
# I can simply write the following pattern,
match = re.findall(r'\b(manish)(_\w+)?\b', string)
print(match)
# [('manish', ''), ('manish', '_jain')]

