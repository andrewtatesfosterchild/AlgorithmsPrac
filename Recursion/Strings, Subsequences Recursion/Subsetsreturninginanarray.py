def subseqinlist(p, up):
    if not up:
        list = []
        list.append(p)
        return list
    
    char = up[0]
    left = subseqinlist(p + char , up[1:])
    right = subseqinlist(p , up[1:])
        
    left.extend(right)

    return left

print(subseqinlist("" , "abc"))