# Lists
courses =['History', 'math', 'physics','compsci']
print(courses)
print(courses[3]) # prints value of 3 index
print(courses[-1]) # negative indexesgave last items - here output is 'compsci'
print(courses[-2]) # prints physics

print(courses[0:2]) # first param is starting point nad second param is stoping index

# Lists mehtod
courses.append('art') # Append () adds value at last
print(courses)

courses.insert(1, 'art') # insert () adds value at given index
print(courses)

courses_2 =['education','chemistry'] # another list object

# try to insert one list object into another
#courses.insert(0,courses_2)
print(courses) # prints [['education', 'chemistry'], 'History', 'art', 'math', 'physics', 'compsci', 'art']

# To overcome on above issue, will use extend() function
courses.extend(courses_2)
print(courses) # add all values from second list into first one

courses.remove('math') # removes perticular value
print(courses)
rmstr = courses.pop() # removes last value from list and pop() returns removed value
print(courses)
print(rmstr) # prints removed value

# reverse List
courses.reverse()
print(courses)
