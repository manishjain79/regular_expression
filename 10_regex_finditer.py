import re

string = 'John has 6 cats but I think my friend Susan has 3 dogs and Mike has 8 fish'
iter_object = re.finditer('(\w+) \w+ (\d+) (\w+)', string)
# print(iter_object)
# output is: <callable_iterator object at 0x0000013B70A514A8>
# 1.
# finditer() finds all the hits and gives out an iterable which can be iterate over
# to extract match using next().
# 2.
# finditer() also allows to use various other methods like group(), span(), groups()
#
# print(next(iter_object))
# output is: <re.Match object; span=(0, 15), match='John has 6 cats'>
# Remember here, one iteration is already exhausted.
# print(next(iter_object).group())  # should print out next match.
# output is: Susan has 3 dogs
# print(next(iter_object).group())  # should print out next match
# output is: Mike has 8 fish
# print(next(iter_object).group())  # Should get error as all the iterations are exhausted.
#   File "C:/Users/MANISHKUMARJAIN/PycharmProjects/regular_expressions/10_regex_finditer.py", line 20, in <module>
#     print(next(iter_object).group())
# StopIteration
string = 'John has 6 cats but I think my friend Susan has 3 dogs and Mike has 8 fish'
iter_object = re.finditer('(\w+) \w+ (\d+) (\w+)', string)
print("Manish")
# print(next(iter_object).groups())
# output is: ('John', '6', 'cats')
# print(next(iter_object).groups())
# output is: ('Susan', '3', 'dogs')
#
# You got the idea, it will iterate over.
for match in iter_object:
    print(match.group())
# output is:
# John has 6 cats
# Susan has 3 dogs
# Mike has 8 fish
# or you can try:
for match in iter_object:
    print(match.groups())

# or:
for match in iter_object:
    print(match.group(3,2,1))




