# string is similar to array
# array is collection of similar data type
# string is a collection of characters, alphabets or words
# one of the primitive data structures
# building blocks for data manipulation
# features:
# supports indexing
# String indexing in Python is zero-based
# first element is indexed 0, second is indexed one and so on
# strings are immutable i.e. they can't be changed after they are created
# supports slicing
some_string = 'this is test string'
# strings can be denoted using 'string' ,"string","""string""",'''string'''
# i.e.  string in Python can be easily created using single, double, or even triple quotes
# 'roshan',"roshan","""roshan"""
# defined inside str class
print(some_string)
print(type(some_string))
# indexing
print(some_string[0])
print(some_string[1])
# negative indexing is supported
print((some_string[-1]))
print((some_string[-2]))
# immutable
some_string = 'new text assigned'
print(f"Changed string is {some_string}")
# not allowed
# uncomment and run the following code which will generate error message: TypeError: 'str' object does not support item assignment
# some_string[0] ='a'
# slicing
# sub string can be accessed using slicing
# [start:end:step]
print(some_string[::]) #display whole string
print(some_string[1::]) # from index 1 to end
print(some_string[0:5]) # from index 0 to index 4 i.e. excluding 5
print(some_string[::2]) # from 0 to end showing each second characters
print(some_string[1:7:2]) # from 1 to 6 excluding 7 and step 2
print(some_string[::-1]) # reverse the string
