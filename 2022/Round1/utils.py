# Circular Queue implementation in Python


class CircularQueue():

    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    # Insert an element into the circular queue
    def enqueue(self, data):

        if ((self.tail + 1) % self.k == self.head):
            print("The circular queue is full\n")

        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data

    def enqueueList(self, data):
        pass

    
    # Delete an element from the circular queue
    def dequeue(self):
        if (self.head == -1):
            print("The circular queue is empty\n")

        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp

    def printCQueue(self):
        if(self.head == -1):
            print("No element in the circular queue")

        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()


class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
             
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
 
    ## Function to insert a node in
    ## tail in circular linked list
    def insertNode(self, d):
        ## First insertion in circular
        ## linked list
        if (self.head == None):
            newNode = Node(d)
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
        else:
            ## Non-empty list
            temp = Node(d)
            temp.next = self.tail.next
            self.tail.next = temp
            self.tail = self.tail.next
 
    ## Function to print circular linked list
    def printList(self):
        curr = self.head
 
        if(self.head == None):
            print("List is Empty")
            return
 
        ## Else iterate until node is NOT head
        print(curr.data, " ", end='')
        curr = curr.next
        while curr != self.head:
            print(curr.data, " ", end='')
            curr = curr.next
        print("\n")
 
    ## Function to reverse a node
    def length(self):
        if (self.head == None):
            return 0
 
        size = 0
        curr = self.head
 
        ## Else iterate until node is NOT head
        size += 1
        curr = curr.next 
        while (curr != self.head):
            curr = curr.next
            size += 1
        return size
 
    def checkIdentical(self, llist):
        ## Get the length of first linked list
        l1 = self.length()
 
        ## Get the length of first linked list
        l2 = llist.length()
 
        ## If l1!=l2 then linked list can not
        ## be identical
        if (l1 != l2):
            return False
 
        ## Initialize the variables
        Count = 0
        flag = 0
 
        ## Initialize temporary pointers
        h1 = self.head
        h2 = llist.head
 
        ## Traverse the list
        while True:
 
            ## If element matches in two
            ## circular linked list
            if (h1.data == h2.data):
                h1 = h1.next
                Count += 1
 
                ## If count equals to l1 or l2
                ## then linked list are identical
                if (Count == l1):
                    return True
 
            ## If element does not matches
            ## in two circular linked list
            else:
                h1 = self.head
                Count = 0
 
                ## If flag becomes 1 then one
                ## rotation is complete and
                ## if now data does not match then
                ## linked lists are not identical
                if (flag):
                    return False
 
            ## Check if h2 complete one rotation
            if (h2.next == llist.head):
                flag = 1
 
            ## Move h2 to h2.next
            h2 = h2.next

    def checkIdenticalNew(self, llist):
        ## Get the length of first linked list
        l1 = self.length()
 
        ## Get the length of first linked list
        l2 = llist.length()
 
        ## If l1!=l2 then linked list can not
        ## be identical
        if (l1 != l2):
            return False
 
        ## Initialize the variables
        Count = 0
        flag = 0
 
        ## Initialize temporary pointers
        h1 = self.head
        h2 = llist.head
        h2_track = h2
 
        ## Traverse the list
        while True:
 
            ## If element matches in two
            ## circular linked list
            if (h1.data == h2.data):
                h1 = h1.next
                Count += 1
 
                ## If count equals to l1 or l2
                ## then linked list are identical
                if (Count == l1):
                    return True
 
            ## If element does not matches
            ## in two circular linked list
            else:
                h1 = self.head
                h2 = h2_track
                h2_track = h2_track.next
                Count = 0
 
                ## If flag becomes 1 then one
                ## rotation is complete and
                ## if now data does not match then
                ## linked lists are not identical
                if (flag):
                    return False
 
            ## Check if h2 complete one rotation
            if (h2.next == llist.head):
                flag = 1
 
            ## Move h2 to h2.next
            h2 = h2.next
  
 
# Driver Code
if __name__=='__main__':
 
    llist1 = LinkedList()
    llist2 = LinkedList()
 
    llist1.insertNode(1)
    llist1.insertNode(2)
    llist1.insertNode(3)
    llist1.insertNode(4)
    llist1.insertNode(5)
    llist1.insertNode(1)
    llist1.insertNode(2)
    llist1.insertNode(6)
 
    llist2.insertNode(5)
    llist2.insertNode(1)
    llist2.insertNode(2)
    llist2.insertNode(6)
    llist2.insertNode(1)
    llist2.insertNode(2)
    llist2.insertNode(3)
    llist2.insertNode(4)
 
    flag = llist1.checkIdentical(llist2)
    if flag:
        print("Yes")
    else:
        print("No")
 
        # This code is contributed by subhamgoyal2014.