def sequentialSearch(list, item):
    found = False
    count = 0
    
    while not found and count < len(list):
        if list[count] == item:
            found = True
        else:
            count+=1
    return found

list = [1, 2, 45, 7]
print(sequentialSearch(list, 9))