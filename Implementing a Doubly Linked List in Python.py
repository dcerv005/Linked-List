class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        self.prev=None

class DoublyLinkedList:
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
            
            while current and current_position < index:
                current.prev = current
                current = current.next
                current_position +=1
            current.prev=new_node
            new_node.next = current
            if current is None:
                self.tail=new_node

    def deletion(self, data):
        current=self.head
        
        while current:
            if current.data == data:
                if previous:
                    current.prev.next = current.next
                if current == self.head:
                    self.head=current.next
                if current == self.tail:
                    self.tail = current.prev
                if current.next:
                    current.next.prev=current.prev
                return True
            
            current=current.next
        return False
    
    
        
    
    def traversal(self):
        if not self.head:
            print("Empty list")
        else: 
            current=self.head
            while current:
                print(f"Data: {current.data}")
                current=current.next



example2=DoublyLinkedList()

example2.insertion("David", 0)
example2.insertion("Hello", 0)
example2.insertion("Delete", 1)


example2.deletion("Delete")
example2.traversal()
