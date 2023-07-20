def subseqinlist(p, up):
    if not up:
        list = []
        list.append(p)
        return list
    
    char = up[0]
    first = subseqinlist(p + char , up[1:])
    second = subseqinlist(p , up[1:])
    third = subseqinlist(p + (str(ord(char))), up[1:])

        
    first.extend(second)
    first.extend(third)

    return first

print(subseqinlist("" , "abc"))