def orderedSequentialSearch(list, item):
    found = False
    count = 0
    stop = False

    while not found and not stop and count < len(list):
        if list[count] == item:
            found = True
        elif item < list[count]:
            stop = True
        else:
            count+=1
    return found

list = [4, 6, 8, 10]
print(orderedSequentialSearch(list, 5))