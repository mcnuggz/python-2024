# taken from youtube short video, seems very convoluted for what needs to be done
# uses the two pointer approach

# def strStr(haystack: str, needle: str) -> int:
#     for i in range(len(haystack)):
#         j = 0
#         while j < len(needle) and i+j < len(haystack) and needle[j] == haystack[i+j]:
#             j += 1
#         if j == len(needle):
#             return i
#     return -1

# finds substring throughout string if there are multiple occurances

# def strStr(haystack:str, needle:str) -> str:
#     indexes = [i for i in range(len(haystack)) if haystack.startswith(needle,i)]
#     if indexes:
#         strIndexes = (str(element) for element in indexes)
#         separator =", "
#         result = separator.join(strIndexes)
#         return result
#     else:
#         return 0

# returns only the index of first occurance of substring

def strStr(haystack:str, needle:str) -> str:
    return haystack.index(needle)

# print(strStr("The fox jumps over the fence to chase the rabbit","o"))
print(strStr("abcyesxyz", "yes")) 