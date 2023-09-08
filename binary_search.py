def binarySearch(list, item):
    if len(list) == 0:
        return False
    else:
        middle = len(list)//2

        if list[middle] == item:
            return True
        elif list[middle] < item:
            return binarySearch(list[middle+1:], item)
        elif list[middle] > item:
            return binarySearch(list[:middle], item)

list = [1, 3, 5, 7, 9, 10, 12]
print(binarySearch(list, 0))