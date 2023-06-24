# V. imp core concept of recursion,
# Declaring variables INSIDE the recursion and returning them

'''
    For this, You don't return the answer obtaine from below calls immediately

    Instead, You append the answers obtained from below into the current instance of the list
    and only then you return the current instance of the list to the above function call

    That's it ;)
'''


def findallindex(arr , target , index):
    list = [] # Instantiated everytime

    if (index == len(arr)):
        return list
    
    # This only contains answer for the current function call
    if (arr[index] == target):
        list.append(index)
    
    # This brings the answers from below function calls
    ansfrombelowcalls = findallindex(arr , target , index + 1)

    # Notice how there is no return statement, So it brings the answer from below call, Extends the list and returns the current instance of the last to the next above function call

    list.extend(ansfrombelowcalls)

    return list # Current instance of the list is returned to the above call




arr = [1 , 2 , 3 , 4 , 4 , 7]

print (findallindex(arr , 4 , 0))