import re
# Back referencing is the technique to refer back the specific group by numbers.
# one use could be to tell re to use same group-re somewhere else in the whole regex.
string = 'Merry Merry Christmas'
# Let's look for repeated words.
match = re.search(r'(\w+) \1', string)  # that's numeric 1.
print(match)          # output is: <re.Match object; span=(0, 11), match='Merry Merry'>. Remember match is entire match.
print(match.group(1))   # output is: Merry. Because we have only one group and that is the only one will be displayed.
# unfortunately the regex did not work without making it a 'raw'
match = re.search('(\w+) \1', string)  # There is no r'' in front of regex.
print(match)
# output is: None
string = 'Happy Happy Holidays. Merry Merry Christmas'
match = re.findall(r'(\w+) \1', string)
print(match)
# Since there is only group and that's value will be displayed.
# output is: ['Happy', 'Merry']
match = re.findall(r'(\w+) (\1)', string)
print(match)
# output is: [('Happy', 'Happy'), ('Merry', 'Merry')]
string = 'Happy Happy Holidays. Merry Merry Christmas Manish Jain Jain'
match = re.findall(r'(\w+) (\1)', string)
print(match)
# output is: [('Happy', 'Happy'), ('Merry', 'Merry'), ('Jain', 'Jain')]
match = re.findall(r'(\w+) \1', string)
print(match)
# output is: ['Happy', 'Merry', 'Jain']


