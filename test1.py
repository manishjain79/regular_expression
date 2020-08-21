import sys, itertools, re

print(sys.version_info)
print(sys.version)

a = ["manish", "kiran", "devang", "garbage"]
b = ["jain", "jain", "jain"]

for fn, ln in itertools.zip_longest(a, b):
    if ln is None:
        print(f'{fn} does not have last name')
    else:
        print(fn, ln)

file = 'C:\cygwin64\home\MANISHKUMARJAIN\hmc_serial_number'
# look = input("Enter Your Python re Pattern: ")
# look = fr'{look}'
# mysearch = re.compile('((.*\n){1})\*SE')
mysearch = re.compile('(".*\n"{2})\*SE.*\n(.*\n)')

print(mysearch)
with open(file, mode='r') as hmc_sn:
    matches = mysearch.finditer(hmc_sn.read())
for match in matches:
    print(match.groups())
