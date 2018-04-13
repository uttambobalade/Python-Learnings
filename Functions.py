# functions are going to perform certain task

def hello_func(): # function defination start with 'def' keyword
    print("inside function")

hello_func() #function call


# function with parameter with return value

def print_message(message):
    return 'Hello {} welcome to this course. '.format(message)

print(print_message("Uttam")) # prints hello uttam welcome to this course
