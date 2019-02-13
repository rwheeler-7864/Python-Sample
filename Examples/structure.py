#Pythons Structure


#object reference  (objectreference = value)
x = "blue" ##creates a string "object" with the text "blue"
y = "green"
z = x


# = # (the '=' operator binds an object reference to an object in memory)



route = 866
print(route, type(route)) #prints: 866 <class 'int'>
route = "north"
print(route, type(route)) #prints:866 <class 'str'>

#type() - function returns the data type, also know as the class of the data item
#---! Only can be used in Python Shell, useful for Testing/Debugging, alternativly use [print()] outside shell.


##tuple example!! 
#---! [doesn't store data types / / takes copies of the lists and stores them in memory] --!#
##('blue, 'green', 'blue')

####Creating Lists#### 
#---! [doesn't store data types / takes copies of the lists and stores them in memory] --!#
####[1, 2, 3, 4, 5]
####['alpha', 'bravo', 'charlie'
####['zebra, 49, -987, 'elephant',200]

####Methord [Simply a function that is called for a paticular object]

####functonName(arguments) e.g objectName.methordName(argument)
####[dot ....  (above) - used to access the objects attributes]

####The if statement example block structure
if boolean_express1:
    suite1
elif boolean_expression2:
    suit2
elif boolean_expressionN:
    suiteN       
else:else_suite     