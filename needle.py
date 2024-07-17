def strStr(haystack:str, needle:str) -> str:
    indexes = [i for i in range(len(haystack)) if haystack.startswith(needle,i)]
    if indexes:
        strIndexes = (str(element) for element in indexes)
        separator =", "
        result = separator.join(strIndexes)
        return result
    else:
        return 0

# def strStr(haystack:str, needle:str) -> str:
#     return haystack.index(needle)

print(strStr("The fox jumps over the fence to chase the rabbit","o"))
    