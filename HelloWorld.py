# # print("Hellow World!", end='')
# # print('Goodbye world')
# # print('Test1')
# # print('Goerge', 'Foreman', 42, 'Old man', sep='\t') #\t is a tab
# # print('Goerge', 'Foreman', 42, 'Old man', sep='\n') #\n is a new line

# # #Strings, Integers, Float Numbers, and Boolean } Types of data


# # fname = 'George' #string
# # lname = 'of the Jungle' #sting
# # age = 42 #integer
# # salary = 12345.66 #float

# # print(type(fname), type(lname), type(age), type(salary))
# # print(fname, lname, age, salary)


# # Rules of Variable names
# #   must start with _ or a character (letter)
# #   Can't start with a number
# #   Cannot be a keyword

# # Conventions of Variable Names - 
# #   Multiple words are seperated with an _
# # Best Practice
# #   use all lowercase
# #   Not too long, not too short, meaningful


# # Comments are done with # or with 


# # OPERATORS
# # Arithmetic Operators
# # + - * /

# # age = 10
# # print('Age will always be 10')
# # print(age + 10, ' age + 10') #gives integer
# # print(age - 5 , ' age - 5') #gives integer
# # print(age * 2, ' age * 2') #give integer
# # print(age / 5, 'age / 5') #gives float

# # age = 10
# # age = age ** 2 #Raise to the power
# # print(age)
# # age = age ** 0.5 #Square Root
# # print(age)

# #  // will print an integer without the number behind it
# # # % is modulus which is a remainder function
# # age = 10
# # print( age % 3) #3 goes into 10 3 times so the print will be 1 because there is one left over
# # print ( age // 3)


# # #############################################################################    WEEK 2     ####################################################################################################################


# # Expression vs Statement
# # An expression is anything that needs to be evaluated/simplified. Usually one or more values and 0 or more operators

# # EXPRESSIONS# just something that can be simplified
# # 42
# # 'Hello World'
# # 'Hello' + ' ' + 'World'
# # 10 * 2 - 3 / 4 + 5
# # age >= 8 and height >= 42 (Boolean expression)


# # Statements A full command that can be executed by python
# # print(age >= 8 and height >=  42)
# # can__ride = age> 8 and height >= 42
# # if age >= 8 and height >= 42:
# #     print('Can Ride!')



# # Syntax vs semantics

# # Sentence
# #     big black dogs bark loudly

# # Syntax: (basic structer = is this put together correctly?)
# #     adjective adjective noun verb adverb

# # semantics: (What am i trying to accomplish with this statemetnt?)
# #     a statement about what (some) large dogs do


# # print('Hello') #Syntacticly correcty 
# # print('Hello") #Syntax error
# #   print('Hello') #indentation error

# # a = 0
# # b = 45
# # avg = b/a
# # print('Average', avg)  This gives a runtime (divide by zero) error
# # print('a: ' + a) #TThis gives a runtime (type error), can only concatenate str (not int) to another str

# # age = age + 1
# # age += age + 1 This is a Logic error - syntax is fine, doesn't cause runtime error


# # Types of Errors

# #   1.  Syntax error where the structure of the program is incorrect (doesn't even try to run the program)
# #             Indentation Error
# #   2.  Runtime Error -  Structure is fine but it runs into a problem when trying to run the program (for example dividing by zero.) (Runs the program and then hits an error)
# #   3.  Logic Error - Syntax is fine, it doesn't cause a runtime error (You just get the wrong answer)



# # Strings

# # greeting = 'Hello'
# # print(greeting)

# # greeting = 'World'
# # print(len(greeting))


# # Strings are immutable 



# # #slice operator [start:end:step]
# # greeting = 'Hello World'
# # print(greeting[2:8:1]) #Start is inclusive, End is exclusive so the last character here will be character 7, gets every character
# # print(greeting[2:8:2]) #This gets every second character instead of every character



# # types of conversion functions


# # Input functions


# # Project 1


# # Multi-Line strings


# # String Formatting

# #FOR LOOPS
# # for value in range(5,250):
# #     is_prime = True
# #     limit = int(value ** 0.5) + 1
# #     for i in range(2, limit):
# #         if value % i == 0:
# #             is_prime = False
# #             break

# #     if is_prime:
# #         print(f'{value} is prime.')


# #WHILE LOOPS

# total = 0.0
# entry = input('Number: ')
# while entry != 'done':
#     total += float(entry)
#     entry = input('Number: ')

# print(f'total: {total}')


import turtle

for i in range(4):
    turtle.forward(80)
    for j in range(3):
        turtle.right(90)
        turtle.forward(20)

