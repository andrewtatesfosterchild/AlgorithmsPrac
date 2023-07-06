def eraser(string):

    if string == "":
        return ""

    if string.startswith("apple"):
        return eraser(string[5:])
    else:
        return string[0] + eraser(string[1:])


print(eraser("baccappleacca"))