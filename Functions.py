# functions are going to perform certain task

def hello_func(): # function defination start with 'def' keyword
    print("inside function")

hello_func() #function call


# function with parameter with return value

def print_message(message):
    return 'Hello {} welcome to this course. '.format(message)

print(print_message("Uttam")) # prints hello uttam welcome to this course

# function with default value param
def default_param(message, name='You'):
    return '{}, {}'.format(message, name)

print(default_param('Hi')) # print Hi with default value of param 'name'
print(default_param('Hi','Uttam')) # prints Hi Uttam
