#Task1
print(234)
print(43.12)
print(3+2j)
print('Hello')
print(True)
print('\n')


#Task2
print(123, 'is type of', type(234))
print(43.23, 'is type of', type(43.12))
print(4-1j, 'is type of', type(4-1j))
print('How are you?', 'it type of', type('How are you?'))
print(True, 'is type of', type(True))
print('\n')

#Task3
print(isinstance(123, int))
print(isinstance(123, float))
print(isinstance(True, bool))
print(isinstance(5+2j, complex))
print(isinstance(123, str))
print('\n')

#Task4
print('Is 123 an instance or int?:' ,isinstance(123,int))
print('Is 43.12 an instance or bool?:' ,isinstance(43.12, bool))
print('Is (4-1j) an instance or complex?:' ,isinstance(4-1j, complex))
print('Is True an instance or bool?:' ,isinstance(True, bool))
print("Is 'How are you?'  an instance of float?: ",isinstance('How are you?', float))

# This is my first comment
# Block comments are indented to the same level as that code

print("Hello")
print("Line with inline code!")  # remember about spacing!

print(type(123.45))  # getting type of number

"""
You can use triple-quoted strings. When they're not a docstring (the first thing in a class/function/module), they are ignored.
Read aforementioned answer from Stack Overflow!
"""