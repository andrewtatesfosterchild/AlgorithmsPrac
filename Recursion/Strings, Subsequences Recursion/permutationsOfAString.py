def permutations(p , up):
    if not up:
        print(p)
        return

    char = up[0]
    for i in range(0,len(p)+1):
        f = p[0:i]
        s = p[i:len(p)]
        permutations(f + char + s , up[1:])
    
permutations("" , "abc")