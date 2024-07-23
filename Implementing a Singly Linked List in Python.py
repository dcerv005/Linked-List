class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class SinglyLinkedList:
    def __init__ (self):
        self.head=None
        self.tail=None

    def insertion(self, data, index):
        new_node=Node(data)
        if index == 0:
            if not self.head:
                self.head= new_node
                self.tail=new_node
            else:
                new_node.next= self.head
                self.head=new_node
        else:
            current = self.head
            current_position=0
            previous= None
            while current and current_position < index:
                previous = current
                current = current.next
                current_position +=1
            previous.next =new_node
            new_node.next = current
            if current is None:
                self.tail=new_node

    def deletion(self, data):
        current=self.head
        previous=None
        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next
                else:
                    self.head=current.next
                if current.next is None:
                    self.tail=previous
                return True
            previous=current
            current=current.next
        return False
    
    def __iter__(self):
        current=self.head
        while current:
            yield current.data
            current=current.next
        
    
    def traversal(self):
        print("Linked list elements:")
        for data in self:
            print(data , end=" -> ")
        print("None")



example1=SinglyLinkedList()

example1.insertion("David", 0)
example1.insertion("Hello", 0)
example1.insertion("Delete", 1)


example1.deletion("Delete")
example1.traversal()

            

