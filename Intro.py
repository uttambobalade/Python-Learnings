# print Welcome message
print('welcome to Python!')

message = "Hello World"
print(message)

# multiline test string assignment
multiline_text = """This is multiline text
string contains n number of lines"""

print(multiline_text)

# string functions

print(len(multiline_text)) # length of string
print(multiline_text[1]) # returns index position char from string
#print(multiline_text[145]) # trying to access char which is not in string

#split function
print(message[0:5]) # returns string with start index:next char count
print(message[2:8])

# Upper and lowercase functions
print(message.lower())
print(multiline_text.upper())

# Count functions
print (message.count('o')) #count the input string

print(message.find('World')) # returns index of the input str

# replace function
new_message = message.replace('World','Python')

print(message) #prints Hello World
print(new_message) # prints Hello Pyhton

# Concat strings

greeting ='hello'
name= 'Uttam'
concat_str = greeting +' ' + name +'. Welcome!' # normal way to concat strings
print(concat_str)
formatted_str = '{},{}. Welcome!'.format(greeting, name) # using formatted string , count curly parantesis = count of input params
print(formatted_str)
