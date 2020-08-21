import re
#
# []            = Allows to declare set of my own defined characters to be pattern as opposed to using
#               \d or \w or . etc....
# [A-Z]         =   Match an Upper Case character.
# [A-Z,]        =   Match an Upper Case character and a comma
# [A-Z,"?.]     =   Match an Upper Case character, a comma, a ", a ? and a .
# [0-9]         =   Match a digit.
#
# Similarly, you can create your own character set with different symbols.
# One more thing:
# [^A-Z]        =   ^ negate the selection. I.e. anything other than A-Z
#
#
match_object = re.search('[A-Z]', 'How Are You?')
print(match_object)
# output is: H
#
match_object = re.search('[A-Z,"?.]', '"How Are You?", asked John.')
print(match_object)
# output is: "
# out of all the characters in our defined character set, it hits " on first match.
match_object = re.findall('[A-Z,"?.]', '"How Are You?", asked John.')
print(match_object)
# output is: ['"', 'H', 'A', 'Y', '?', '"', ',', 'J', '.']
