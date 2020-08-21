import re
string = ''' My name is Manish. I am taking Devang to a swimming lesson today. I will swim probably as well.'''
match = re.split('\.', string)
print(match)
# output is:
# [' My name is Manish', ' I am taking Devang to a swimming lesson today', ' I will swim probably as well', '']
# Few things to observe:
# The split point has disappeared.
# We have an empty entry at last.
# if we want to include the split point into result, make it a group.
match = re.split('(\.)', string)
print(match)
# output is:
# [' My name is Manish', '.', ' I am taking Devang to a swimming lesson today', '.',
# ' I will swim probably as well', '.', '']
#
#
string = '<p>My mother has <span style="color:blue">blue</span>eyes.</p>She is beautiful.'
match = re.split('<[^<>]+>', string)
print(match)
# output is: ['', 'My mother has ', 'blue', 'eyes.', 'She is beautiful.']
#
# Whenever there is split at edges, i.e. at the beginning of string or at the end, we end up with an empty string.
string = ',hello,friend,'
match = re.split(',', string)
print(match)
# ['', 'hello', 'friend', '']
new_string = filter(None, string.split(','))
print(list(new_string))
# output is: ['hello', 'friend']
