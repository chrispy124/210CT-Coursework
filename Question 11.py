class Node(object):
    def _init_(self, value):
        self.value = value
        self.next = None
        self.prev = None


class List(object):
    #Initialize
    def _init_(self):
        self.head = None
        self.tail = None
    
    def insert(self, head, num):
        if head != None:
            num.next = head.next
            head.next = num
            num.prev = num
            if num.next != None:
                num.next.prev = num
        if self.head == None:
            self.head = self.tail = num
            num.prev = num.next = None
        elif self.tail == head:
            self.tail = num

    #Node delete function
    def deleteNode(self, head):
        if H.prev != None:
            H.prev.next = H.next
        else:
            left.head = head.next
        if H.next != None:
            H.next.prev = head.prev
        else:
            left.tail = head.prev

    #function to print tree            
    def display(self):
        values=[]
        n=self.head
        while n!=None:
            values.append(str(n.value))
            n=n.next
        print("List: ",",".join(values))

#allows for progrma to run,testing nodes
if __name__ == '_main_':
    l=List()
    l.insert(None, Node(4))
    l.insert(l.head,Node(6))
    l.insert(l.head,Node(8))
    l.insert(l.head,Node(10))
    
    l.display()
