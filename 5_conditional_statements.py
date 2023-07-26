# if condition_is_true:
#     execute this
a = 22
print(f"a in this case is {a}")
if a > 20:
    print("Inside if block")
# comment previous if
# uncomment following if for analyzing the concept and operations
a = 5
print(f"a in this case is {a}")
if a > 20:
    print("current value of a is greater than 20")
    print("Condition satisfied")
    print("Inside if block")
# 5 is not greater than 20 so the program flow don't enter the if block
# add another if for another condition
if a < 20:
    print("Inside second if block")

# if else
# comment out the above statements
a = 22
print(f"a in this case is {a}")
if a > 20:
    print(">20")
else:
    print("<20")
# change the value of a to 10 from 22 and execute the program
# multiple conditions
# if elif
# comment out the previous ones
a = 17
print(f"a in this case is {a}")
if a > 20:
    print(">20")
elif a > 15:
    print(">15")
elif a > 10:
    print(">10")
else:
    print("<=10")
# NOTE:
# change the value of a to 22 and execute
# change the value of a to 12 and execute
# change the value of a to 5 and execute
# GOOD TIMES