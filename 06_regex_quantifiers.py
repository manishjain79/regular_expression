import re
#
# '+'       = 1 or more occurrences of match
# '?'       = 0 or 1 occurrences of match
# '*'       = 0 or more occurrences of match
# {m,n}     = minimum m and maximum n occurrences of match
# {m}       = exact occurrences of match
#
match_object = re.findall('\w+', 'ab cd&87*s\nda%3#23')
# print(match_object)
# output is: ['ab', 'cd', '87', 's', 'da', '3', '23']
match_object = re.search('\w+', 'ab cd&87*s\nda%3#23')
# print(match_object)
# output is: <re.Match object; span=(0, 2), match='ab'>
match_object = re.match('\w+', 'ab cd&87*s\nda%3#23')
# print(match_object)
# output is: <re.Match object; span=(0, 2), match='ab'>
match_object = re.findall('\W+', 'ab cd&87*s\nda%3#23')
# print(match_object)
# output is: [' ', '&', '*', '\n', '%', '#']
match_object = re.search('\W+', 'ab cd&87*s\nda%3#23')
# print(match_object)
# output is: <re.Match object; span=(2, 3), match=' '>
match_object = re.match('\W+', 'ab cd&87*s\nda%3#23')
# print(match_object)
# output is: None
match_object = re.findall('.+', 'ab cd&87*s\nda%3#23')
# print(match_object)
# output is: ['ab cd&87*s', 'da%3#23'] because it did not match \n.
match_object = re.search('.+', 'ab cd&87*s\nda%3#23')
# print(match_object)
# output is: <re.Match object; span=(0, 10), match='ab cd&87*s'>. Whatever encounters first in string.
match_object = re.match('.+', 'ab cd&87*s\nda%3#23')
# print(match_object)
# output is: <re.Match object; span=(0, 10), match='ab cd&87*s'>
# if I had, \n at the beginning of the string which '.' does'nt match, it would have given None.
match_object = re.match('.+', '\nab cd&87*s\nda%3#23')
# print(match_object)
# output is: None
match_object = re.findall('.?', 'ab cd&87*s\nda%3#23')
# print(match_object)
# output is: ['a', 'b', ' ', 'c', 'd', '&', '8', '7', '*', 's', '', 'd', 'a', '%', '3', '#', '2', '3', '']
match_object = re.search('.?', 'ab cd&87*s\nda%3#23')
# print(match_object)
# output is:<re.Match object; span=(0, 1), match='a'>
match_object = re.match('.?', 'ab cd&87*s\nda%3#23')
# print(match_object)
# output is: <re.Match object; span=(0, 1), match='a'>
match_object = re.findall('.{2}', 'ab cd&87*s\nda%3#23')
# print(match_object)
# output is: ['ab', ' c', 'd&', '87', '*s', 'da', '%3', '#2']
match_object = re.search('.{2,3}', 'ab cd&87*s\nda%3#23')
# print(match_object)
# output is: <re.Match object; span=(0, 3), match='ab '>
match_object = re.match('.{4,5}', 'ab cd&87*s\nda%3#23')
print(match_object)
# output is: <re.Match object; span=(0, 5), match='ab cd'>


