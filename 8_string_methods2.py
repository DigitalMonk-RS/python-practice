# python string methods is a collection of in-built Python functions
# isnumeric(),find(),isalpha(),endswith(), split(),istitle(),islower(),rstrip(),lstrip(),swapcase()

# string methods in python
            # 1 isnumeric()
# Return True if the string is a numeric string otherwise False
print("\t\tDemo of isnumeric()")
some_string = "123"
print(some_string.isnumeric())
some_string = "hello123"
print(some_string.isnumeric())
some_string = "III123"
print(some_string.isnumeric())
            # 2 find()
# Return the lowest index in S where substring sub is found and -1 if not found
some_string = 'this is test rest nest'
print("\t\tDemo of find()")
print(some_string.find('i'))
print(some_string.find('X'))
            # 3 isalpha()
# Return True if the string is an alphabetic string, False otherwise
some_string = 'thisistestrestnest'
print("\t\tDemo of isalpha()")
print(some_string.isalpha())
some_string = 'thisistestrestnest1'
print(some_string.isalpha())
            # 4 endswith()
# Return True if S ends with the specified suffix, False otherwise
print("\t\tDemo of endswith()")
some_string = 'roshan shrestha'
print(some_string.endswith('a'))
print(some_string.endswith('x'))
            # 5 split()
# Return a list of the substrings in the string, using sep as the separator string.
print("\t\tDemo of split()")
some_string = 'hello there come here'
print(some_string.split('e'))
print(some_string.split('o'))
            # 6 istitle()
# Return True if the string is a title-cased string, False otherwise.
some_string = 'Roshan Shrestha'
print("\t\tDemo of istitle()")
print(some_string.istitle())
some_string = 'Roshan shrestha'
print(some_string.istitle())
            # 7 islower()
# Return True if the string is a lowercase string, False otherwise.
some_string = 'roshan shrestha'
print("\t\tDemo of istitle()")
print(some_string.islower())

some_string = 'roshan sHrestha'
print(some_string.islower())
            # 8 rstrip()
# rstrip() method removes any trailing characters (characters at the end a string)
some_string = 'this is demo '
print("\t\tDemo of rstrip()")
print(some_string.rstrip())
some_string = 'this is demo'
print(some_string.rstrip('o'))
            # 9 lstrip()
# Return a copy of the string with leading whitespace removed.
# If chars is given and not None, remove characters in chars instead.
print("\t\tDemo of lstrip()")
print(some_string.lstrip('t'))
            # 10 swapcase()
# Convert uppercase characters to lowercase and lowercase characters to uppercase.
some_string = 'RoSHan sHreSTHa'
print("\t\tDemo of swapcase()")
print(some_string.swapcase())
