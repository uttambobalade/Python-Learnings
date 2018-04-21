
print("Imported my module file as module")

message ="test module"

def find_index(to_search, target):
    ''' find the index of value in sequesnce'''
    for i,value in enumerate(to_search):
        if value == target:
            return i

    return -1

