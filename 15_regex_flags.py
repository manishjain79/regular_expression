import re
################################################################
#
#   re.MULTILINE    re.M        explained below
#   re.IGNORECASE   re.I        No need for explanation
#   re.DOTALL       re.S        explained below
#   re.ASCII
#   re.DEBUG
#   re.LOCALE
#
# re.MULTILINE
# e.g.
# pattern starting with ^ or match() method looks for pattern at the beginning of the string.
# If our string is a multiline string, then by using re.MULTILINE, pattern can be applied to
# staring of each new line.
# That all depends on regex that what do we want to find, but re.MULTILINE expands the search
# to multiline.
string = '''My name is Manish Jain.
I am here to learn regex in Python.
My strong advice is to learn regex from Orielly book first.'''
match = re.findall('^My', string)
print(match)
# output is: ['My']
# Now, let's add, re.MULTILINE flag.
match = re.findall('^My', string, flags=re.MULTILINE)
print(match)
# output is: ['My', 'My']
match = re.search('^I', string, flags=re.MULTILINE)
print(match)
# Search() method stops after first occurrence. If my pattern was ^My, it would have stopped there. and re.MULTILINE
# probably wont have an effect.
# But pattern ^I should be at the beginning. But with re.MULTILINE, still I am able to capture it.
# output is : <re.Match object; span=(24, 25), match='I'>
match = re.match('^I', string, flags=re.MULTILINE)
print(match)
# re.MULTILINE does'nt work with match() method.
# output is: None
##########################################################
# re.DOTALL
# .(DOT) matches any character except \n.
# with re.DOTALL it includes \n as well.
match = re.match('.*', string)
print(match)
# It should match all characters in first line and should stop when \n is hit.
# output is: <re.Match object; span=(0, 23), match='My name is Manish Jain.'>
# Let's introduce re.DOTALL flag
match = re.match('.*', string, flags=re.DOTALL)
print(match.group())
# output is: My name is Manish Jain.
# I am here to learn regex in Python.
# My strong advice is to learn regex from Orielly book first.

