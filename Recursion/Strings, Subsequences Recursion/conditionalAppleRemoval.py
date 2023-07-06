def eraserofapifnotapple(string):

    if string == "":
        return ""

    if string.startswith("ap") and not string.startswith("apple"):
        return eraserofapifnotapple(string[2:])
    else:
        return string[0] + eraserofapifnotapple(string[1:])


print(eraserofapifnotapple("baccapplacca"))