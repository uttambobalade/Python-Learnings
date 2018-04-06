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

# join() method converts list object into string with seperator
course_str = ' - '.join(courses) # prints list values with '-' seperator
print(course_str)
# back to list object from string using split() function
new_list = course_str.split(' - ') # retuns list object
print(new_list)


### Tuples ####

# tuples are Immutable and lists are Mutable, paranthesis are used in tuples for assigning object
tuple_1 = ('physics', 'education', 'compsci', 'art')
print(tuple_1)

### Sets ###
# sets contain unordered and no duplicate values
cs_courses = {'physics', 'education', 'compsci', 'it'}
print(cs_courses) # prints un ordered values from list

art_courses = {'art','it','env sci', 'education','design'}

# intersection() - common from both lists
print(cs_courses.intersection(art_courses))
# Difference() - different values from lists 2
print(cs_courses.difference(art_courses))
# Union() - All values from list one and non common values from list2
print(cs_courses.union(art_courses))


# Empty Lists
l1 = []
l2 = list()

# Empty tuples
t1 = ()
t2 = tuple()

# empty sets
# s1 = {} # this isn't right , it's dictonary
s2 = set()
