# Lists
courses =['History', 'math', 'physics','compsci']

print(courses[3]) # prints value of 3 index
print(courses[-1]) # negative indexesgave last items - here output is 'compsci'
print(courses[-2]) # prints physics

print(courses[0:2]) # first param is starting point nad second param is stoping index

# Lists mehtod
courses.append('art') # Append () adds value at last

courses.insert(1, 'art') # insert () adds value at given index

courses_2 =['education','chemistry'] # another list object
# try to insert one list object into another
#courses.insert(0,courses_2)
print(courses) # prints [['education', 'chemistry'], 'History', 'art', 'math', 'physics', 'compsci', 'art']

# To overcome on above issue, will use extend() function
courses.extend(courses_2) # add all values from second list into first one

courses.remove('math') # removes perticular value
rmstr = courses.pop() # removes last value from list and pop() returns removed value
print(rmstr) # prints removed value

# reverse List
courses.reverse()
# sort list - stirng sorts alphabetical and number sorts ascending order
courses.sort() # sorts list with alphabetical/ascending order

courses.sort(reverse=True) # sorts list decending order with param

sorted_courses = sorted(courses) # returns sorted copy input list without modifing input lists
print(sorted_courses)

print(courses.index('compsci')) # prints index of input value from list , here output is 2

# in operator will check value is present or not in list by returning true/false
print('compsci' in courses) # prints True
print('biology' in courses) # prints False
