import re

# Lets understand difference between search and match.
# re.search(PATTERN, STRING, FLAG)
# re.match(PATTERN, STRING, FLAG)
# search method of re, finds the PATTERN anywhere in the given string. Only first occurrence.
# match method of re, finds the PATTERN only at the beginning of the string.

# Let's build our understanding with few examples.
match_object = re.match('c', 'abcdef')
# PATTERN is c and STRING is 'abcdef' and re method is 'match'
# Because the method is match, it will look for pattern only at the beginning of the string.
# Since, we can see here in the string that c is not really at the beginning of the string 'abcdef', it will produce
# None.
# print(match_object)
# Output is: None
# Lets change our string to 'cabdcef'
match_object = re.match('c', 'cabcdef')
# Let's print the match_object
# print(match_object)
# output is: <re.Match object; span=(0, 1), match='c'>
# which matches to the first 'c' at the beginning of the string.
# Look at the span. From index value 0 to 1 of the string 'cabcdef', found c.

# Now, let's try the search method of re with string 'abcdef'
match_object = re.search('c', 'abcdef')
# print it now,
# print(match_object)
# output is: <re.Match object; span=(2, 3), match='c'>
# Because we used 'search' method of re, it tries to find pattern 'c' anywhere in the string.
# Look at the span, from index value 2 to 3 of the string 'abcdef', found c.

# Now, lets change our string to include more 'c' characters.
match_object = re.search('c', 'cabcdefc')  # Added one c at beginning and one at end.
# print it,
print(match_object)
# output is: <re.Match object; span=(0, 1), match='c'>.
# From this output, we understand that although 'search' method of re can find pattern anywhere in the string,
# but it will stop its search after first such occurrence. Look at the span index values of string.
# From 0 to 1, it found 'c' and stopped there.
# 'Search' method matches only one occurrence anywhere in the string.
# Let me remove first 'c' in the string.
match_object = re.search('c', 'abcdefc')
print(match_object)
# output is: <re.Match object; span=(2, 3), match='c'>
# This time matches the only 'c' at index 2,3.

# Another difference:
# e.g. we have a multi-line string and I put 'c' as beginning after new line as I used it in below two methods.
match_object1 = re.search('c', 'abde\nfc')  # 'search' method can still find pattern occurring after new line.
match_object2 = re.match('c', 'abde\nc')  # 'match' method cannot find even the beginning after new line.
print(match_object1)  # <re.Match object; span=(6, 7), match='c'>
print(match_object2)  # None

# Those are the two major differences between 'match' and 'search'
# 'match' = finds pattern only at the beginning of the string or of the multi-line string.
# 'search' = finds pattern anywhere of the string/multi-line string but the fist occurrence only.

# With the above understanding, sometimes it is required to just check if we have a perfect match or not.
# we can use bool function for that purpose.
match_object = re.search('c', 'abde\nfc')
print(bool(match_object))
# output is: True
# If the output is True, we have a hit.
match_object = re.match('c', 'abde\nfc')
print(bool(match_object))
# output is: False
# If the output is False, we have a miss.

# So, we can use 'bool' function to check miss or hit.
