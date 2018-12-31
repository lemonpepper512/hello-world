#Updated Calculator
#Earlier we created a very simple calculator saved in the user_input.py file
#Now that we know how to use comparisons, we are going to make an even better calculator app

#Let's begin by requesting input from the user

num1 = float(input("Enter first number: ")) #Containing this code inside the float() will convert any
#and all input from the user for num1 into an integer, this is easier than trying to convert it later
operator = input("Enter an operator: ") #Requesting an operator from the user
num2 = float(input("Enter a second number: ")) #Requesting num2 from user
#Okay this looks good, but now we need to figure out what the user has input for the operator
#We can do this with an If Statement. Why do we need to know this? Because we need to apply
#the operator chosen to our numbers, else nothing is going to happen.

if operator == "+": #If input from user is + then run code below
    print(num1 + num2)
elif operator == "-": #Else-if input is -, run this code below
    print(num1 - num2)
elif operator == "/": #Else-if input is /, run this code
    print(num1 / num2)
elif operator == "*": #Else-if input is *, run this code
    print(num1 * num2)
else:
    print("Invalid operator") #If input is NONE of the above, then run this code.

