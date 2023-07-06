def subsets(string , processed):
    if string == "": # Base case
        print(processed)
        return

    char = string[0]
    subsets(string[1:] , processed + char)
    subsets(string[1:] , processed)




subsets("abc" , "")