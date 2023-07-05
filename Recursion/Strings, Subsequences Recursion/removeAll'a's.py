# Tail recursion ftw

def helper(string , pos , res):
    if pos == len(string):
        return res
    
    if string[pos] != 'a':
        res = res + string[pos]

    return helper(string , pos+1 , res)

def charremover(string):
    res = ""
    pos = 0
    return helper(string , pos , res)
    

print(charremover("recursionezaf"))
