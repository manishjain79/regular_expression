import re
# re.sub
# re.sub finds pattern in through out the file/multiline string and substitute it with desired string.
string = '''Manish works with IBM Singapore Pte. Ltd. and Kiran works with Wipro International.'''
result = re.sub('(Manish|Kiran)', r'\1 Jain', string)
print(result)
# output is: Manish Jain works with IBM Singapore Pte. Ltd. and Kiran Jain works with Wipro International.
# Look at the desired string pattern, I started it with r'' as raw string. It did not work without r in front.
string = '&1234 ^Manish'
result = re.sub("(\W)(?P<number>\d+) (\W)(?P<word>\w+)", r"\g<word> \g<number>", string)
print(result)
# output is: Manish 1234
# Few examples.
# input = 'abcdefghijkl'
# result = re.sub('abc',  '',    input)           # Delete pattern abc
# result = re.sub('abc',  'def', input)           # Replace pattern abc -> def
# result = re.sub(r'\s+', ' ',   input)           # Eliminate duplicate whitespaces
# result = re.sub('abc(def)ghi', r'\1', input)    # Replace a string with a part of itself

# Note: Take care to always prefix patterns containing \ escapes with raw strings (by adding an r in front of the
# string). Otherwise the \ is used as an escape sequence and the regex won't work.
#
#
# Lamdda Expressions
square = lambda x: x**2
print(square)  # <function <lambda> at 0x000001E158B4AA60>
print(square(3))
# output is: 9
# lambda functions return a function of x the value of the expression written at the right side after :
x = lambda x: x
print(x(3))
# output is: 3
string = 'Devang has 3 cats'
result = re.sub('(\d+)', lambda x: (x.group(0)), string)
print(result)
# output is: 3 which was return value of f(x).
string = 'Devang has 3 cats'
result = re.sub('(\d+)', lambda x: str(square(int(x.group(0)))), string)
print(result)
# output is:
# Devang has 9 cats
# step-1: lambda x: x.group(0)  x is the match object.
# step-2: turn the result into int, because we are running lambda expression on an integer.
# step-3: use square function
# step-4: turn back to string because in re.sub we are dealing with string here.
#
# Another example:
string = 'eat sleep laugh study'
result = re.sub('\w+', lambda x: x.group(0) + 'ing', string)
print(result)
# output is: eating sleeping laughing studying


