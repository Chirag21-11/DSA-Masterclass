class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None
        self.prev = None
    
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
            

# Creation Of Circular Doubly Linked List

    def createDLL(self,nodeValue):
        new_node = Node(nodeValue)
        self.head = new_node
        self.tail = new_node
        new_node.next = new_node
        new_node.prev = new_node
        
        
# Insertion in CDLL

    def insert(self,value,location):
        if self.head is None:
            return "The CDLL does not exists"
        else:
            new_node = Node(value)
            if location == 0:
                new_node.next = self.head
                self.head.prev = new_node
                new_node.prev = self.tail
                self.tail.next = new_node
                self.head = new_node
            elif location == 1:
                new_node.prev = self.tail
                self.tail.next = new_node
                new_node.next = self.head
                self.head.prev =new_node
                self.tail = new_node
            else:
                temp_node=self.head
                index=0
                while index < location -1:
                    temp_node = temp_node.next
                    index +=1
                new_node.next = temp_node.next
                temp_node.next.prev = new_node
                temp_node.next = new_node
                new_node.prev = temp_node 
            return "the node is succesfully inserted"
        
        
    def traverseCDLL(self):
        if self.head is None:
            return None
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node.value)
                if temp_node.next == self.head:
                    break
                temp_node = temp_node.next
                
    def rev_tevaerse(self):
        if self.tail is None:
            return None
        temp_node = self.tail
        while temp_node:
            print(temp_node.value)
            if temp_node.prev == self.tail:
                break
            temp_node = temp_node.prev
                
                
    def search(self,nodevalue):
        if self.head is None:
            return "There is no node in CDLL"
        else:
            temp_node = self.head
            while temp_node:
                if temp_node.value == nodevalue:
                    return temp_node.value
                if temp_node == self.tail:
                    return "Not present"
                temp_node = temp_node.next
            
        
    def delete(self,location):
        if self.head is None:
            return "There is no node in CDLL"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.tail = None
                    self.head = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.tail = None
                    self.head = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                curr_node = self.head
                index =0
                while index < location-1:
                    curr_node = curr_node.next
                    index +=1
                curr_node.next = curr_node.next.next
                curr_node.next.prev = curr_node
            
                    
    def deleteCDLL(self):
        self.tail.next =None
        curr_node = self.head
        while curr_node:
            curr_node.prev = None
            curr_node = curr_node.next
        self.head = None
        self.tail = None
                    
        
circularDLL = CircularDoublyLinkedList()
print(circularDLL.createDLL(5))
circularDLL.insert(0,0)
circularDLL.insert(1,1)
circularDLL.insert(2,2)
circularDLL.insert(21,3)
print([node.value for node in circularDLL])
print(circularDLL.delete(0))
print([node.value for node in circularDLL])
print(circularDLL.deleteCDLL())
print([node.value for node in circularDLL])