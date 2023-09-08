def bubblesort(list):
    for num in range(len(list)-1, 0, -1):
        print(f"num: {num}")
        for i in range(num):
            print(f"i: {i}")
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp

list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubblesort(list)
print(list)