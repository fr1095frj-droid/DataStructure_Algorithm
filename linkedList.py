import Nodes

class LinkedList:
    firstNode = Nodes.node1
    lastNode = Nodes.node5
    size = 0

    def traversal(self):
        LinkedList.size = 0
        currentNode = LinkedList.firstNode
        while currentNode != None:
            print(currentNode.data)
            LinkedList.size += 1
            currentNode = currentNode.next
        print(None)


    def addLast(self, item):
        currentNode = LinkedList.firstNode
        while currentNode != None:
            if currentNode.next == None:
                last = Nodes.Node(item)
                currentNode.next = last
                LinkedList.lastNode = last
                break
            currentNode = currentNode.next
        LinkedList.size += 1


    def addFirst(self, item):
        first = Nodes.Node(item)
        first.next = LinkedList.firstNode
        LinkedList.firstNode = first
        LinkedList.size += 1


    def indexOf(self, item):
        currentNode = LinkedList.firstNode
        index = 0
        while currentNode != None:
            if currentNode.data == item:
                return index
            index += 1
            currentNode = currentNode.next
        return -1


    def contains(self, item):
        currentNode = LinkedList.firstNode
        while currentNode != None:
            if currentNode.data == item:
                return 1
            currentNode = currentNode.next
        return 0


    def removeFirst(self):
        LinkedList.firstNode = LinkedList.firstNode.next
        LinkedList.size -= 1


    def removeLast(self):
        currentNode = LinkedList.firstNode
        while currentNode != None:
            if currentNode.next == LinkedList.lastNode:
                currentNode.next = None
                LinkedList.lastNode = currentNode
            currentNode = currentNode.next
        LinkedList.size -= 1


    def reversed_linkedlist(self):
        pastNode = LinkedList.firstNode
        currentNode = pastNode.next
        temp = currentNode.next
        pastNode.next = None

        LinkedList.firstNode = LinkedList.lastNode
        LinkedList.lastNode = LinkedList.firstNode

        while True:
            if temp.next == None:
                temp.next = currentNode
                currentNode.next = pastNode
                return 0

            currentNode.next = pastNode
            pastNode = currentNode
            currentNode = temp
            temp = temp.next


    def K_node_from_last(self, k):
        variable_k = linked_list.firstNode
        if k > 2:
            for i in range(k - 2):
                variable_k = variable_k.next

            currentNode = LinkedList.firstNode
            while variable_k.next != None:
                variable_k = variable_k.next
                currentNode = currentNode.next

            return currentNode.data
        elif k in (0, 1):
            return LinkedList.lastNode.data
        elif k == 2:
            currentNode = LinkedList.firstNode
            while currentNode.next != LinkedList.lastNode:
                currentNode = currentNode.next
            return currentNode.data













linked_list = LinkedList()


print(linked_list.K_node_from_last(1))
