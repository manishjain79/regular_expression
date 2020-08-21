import re

string = "abababababkkkk"
match = re.search('(ab)+', string)
print(match.group())
print(match.group(1))
print(match.groups())
# output is:
# ababababab        # remember that it is not a group. It is just a match.
# ab                # that's the group.
# ('ab',)           # That's all the groups. Just one? why?
# The repetition overwrites the group value. Essentially, there is only one group, but repeating over.
# Let's try the following
string = "abababababababab"
match = re.search('(ab)+(ab)+', string)
# Now we defined two groups of same pattern.
# The first pattern actually match the entire string. But the other pattern is still pending for its execution.
# When it comes to 2nd pattern, it steals last occurrence from the hits obtained by the first pattern match.
# leaving rest of the match with 1st pattern group and last match with 2nd pattern group.
# we can see this behaviour using span() method later.
print(match.group(0))    # abababababababab
print(match.group(1))   # ab
print(match.group(2))   # ab
print(match.groups())   # ('ab', 'ab')
# This happens only in case that you have same pattern written again to satisfy the result.
# what if the pattern is differ.... try with
# match = re.search('(ab)+(b)+', string)
# print(match)
# output is: None.
# We can show that actual start position of the two groups obtained above. ('ab', 'ab').
print(match.span(1))    # (12, 14)
print(match.span(2))    # (14, 16)

# You see, the group(1) snap is 12:14. Which means that, each occurrence of 'ab' got overwritten into group-1
# and final occurrence was kept as group extraction.
# group(2) span obviously will be last occurrence: 14:16.
# Remember that, if we want entire match, use group(0)
# quantifier does'nt have any effect on the amount of groups we are pulling out. It will overwrite the group value
# with next occurrence.
#
match = re.findall('(ab)+', string)
print(match)  # output is: ['ab']
# similarly with findall() method, the output will have only last/final occurrence of the match.
match = re.findall('((ab)+)', string)
print(match)  # [('abababababababab', 'ab')]
# First, it will print out the bigger group and then second, it will print out the final occurrence of smaller group.
string = '1234 9876'
match = re.findall('((\d)+)', string)
print(match)
# output is: [('1234', '4'), ('9876', '6')]
# It printed out bigger group of first match and then final occurrence of smaller group. And same for second match.
#
# You do not get confuse. Remember that findall() method finds all the matches if we haven't

