#Task1-ex1

#Your task is to print values of primitive data types, 
# one type in one line. Use following types: integer, float, complex, string, boolean

print(234)
print(43.12)
print(3+2j)
print('Hello')
print(True)
print('\n')


#Task2-ex2

# Your task is to print two objects with separator for the same primitive types as in task 1.   
# The first object is a value of given type, the second object is a type of value.  
# The separator is a string " is type of ".


print(123, 'is type of', type(234))
print(43.23, 'is type of', type(43.12))
print(4-1j, 'is type of', type(4-1j))
print('How are you?', 'it type of', type('How are you?'))
print(True, 'is type of', type(True))
print('\n')

#Task3-ex1

# Your task is to check if given value is the instance of given class type using ```isinstance()``` function.  
# The first argument of this function should be value, for example `city` and the second argument should be class type, for example `int`.   
# Print at least one result for every primitive data type ('int', 'float', 'bool', 'complex', and 'str'). 


print(isinstance(123, int))
print(isinstance(123, float))
print(isinstance(True, bool))
print(isinstance(5+2j, complex))
print(isinstance(123, str))
print('\n')

#Task4-ex1

# Your task is a slightly modification of task 3. Instead  printing `True` or `False`
#  modify your code to get readable information about the type of your value. 


print('Is 123 an instance or int?:' ,isinstance(123,int))
print('Is 43.12 an instance or bool?:' ,isinstance(43.12, bool))
print('Is (4-1j) an instance or complex?:' ,isinstance(4-1j, complex))
print('Is True an instance or bool?:' ,isinstance(True, bool))
print("Is 'How are you?'  an instance of float?: ",isinstance('How are you?', float))

#Task5-ex1

#Use  block comments, inline comments, and multiline comments to your code. 

# This is my first comment
# Block comments are indented to the same level as that code
'''
print("Hello")
print("Line with inline code!")  # remember about spacing!

print(type(123.45))  # getting type of number
'''