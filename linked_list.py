class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append_start(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            tmp = self.head
            self.head = Node(value)
            self.head.next = tmp


    def printList(self):
        list = []
        dictionary = dict()
        printValue = self.head
        while printValue != None:
            list.append(printValue.value)
            printValue = printValue.next
        for i in range(0, len(list)):
            if i == len(list)-1:
                dictionary[list[i]] = "Points to: ", None
            else: 
                dictionary[list[i]] = "Points to: ", list[i+1]
        print(dictionary)


if __name__ == "__main__":
    LinkedList = LinkedList()
    LinkedList.append_start(4)
    LinkedList.append_start(3)
    LinkedList.append_start(2)
    LinkedList.append_start(3)
    LinkedList.append_start(8)
    LinkedList.append_start(5)

    LinkedList.printList()
    
# this is just a test

