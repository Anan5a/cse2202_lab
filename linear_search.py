def linearSearch(itemlist, key):
    n = len(itemlist)
    for i in range(0, n):
        if itemlist[i] == key:
            return i
    return False


array = [2, 4, 0, 1, 9]
x = 1
result = linearSearch(array, x)
if not result:
    print("Element not found")
else:
    print("Element found at index: ", result)
