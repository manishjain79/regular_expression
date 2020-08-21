import re

# r'\n' means it is a raw string.\ and n are two characters as opposed to just one special character.
# lets see some examples
match_object = re.search('n', '\n')  # first item is pattern, second item is string.
# print(match_object)
# The output is 'None'. Let's see what we want to achieve. Search character 'n' in the string '\n'.
# \n is not a two character string. It is a new-line character expanded by shell.
# The character \ makes n special in this case.
# If we want to handle this, i.e., to make python ignore the special meaning of '\', we can escape it with another \.
# backslashing a backslash makes the special character '\n' look like 'n'.
# Now, the string '\\n' is treated as a two character string '\' & 'n'
match_object = re.search('n', '\\n')
# print(match_object)  # <re.Match object; span=(1, 2), match='n'>
# Not working the below
# match_object = re.search('\', '\\n')
# print(match_object)
# End of not working
# Now, e.g. we have a string which has a lot of these special characters with backslash. In order to escape them all,
# we will need to add another \ to all those instances. But that is very tedious.
# The best way to proceed with such string is to add 'r' in front of the string to treat it as a raw string.

match_object = re.search('n', r'\nManish Jain\nKiran Jain\nDevang Jain')
print(match_object)  # <re.Match object; span=(1, 2), match='n'>
# The match output is 'n'. But why not all instances of n. We will learn soon.

# Until now we learnt that a string can be treated as raw string so that special meaning of / characters is taken away.
# But that's not the case with regular expressions. Regex with '\n' and r'\n' both look for new line.
# So, let's try to find new line in a string.

match_object = re.search('\n', '\nManish Jain\nKiran Jain\nDevang Jain')
# the above says, search for a new line in string.
# let's print it.
print(match_object)
# <re.Match object; span=(0, 1), match='\n'>
# We found newline in string.
# Now, write the new line regex with 'r' in front to make it look like raw regex.
match_object = re.search(r'\n', '\nManish Jain\nKiran Jain\nDevang Jain')
# so, if print it now,
print(match_object)
# <re.Match object; span=(0, 1), match='\n'>
# It matches new line, because '\n' also looks for new line.

# Now, look for newline character in above string, but make it a raw string.
match_object = re.search('\n', r'\nManish Jain\nKiran Jain\nDevang Jain')
# Here we could write regex '\n' as r'\n' as both look for new line.
# It wont match. As in the raw string, there is no new line character '\n', rather they are treated as two characters.
# Let's print it,
print(match_object)
# Output: None

# Take away from this discussion is that, adding 'r' in front of regex doesn't have much of the effects on
# metacharacters. However, adding 'r' in front of the string, takes away special metacharacter purpose.

