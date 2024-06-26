class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)

class DoublyLinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self,value):
        new_node= Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length +=1

    def __str__(self):
        temp_node = self.head
        result = ' '
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next:
                result += ' <-> '
            temp_node = temp_node.next
        return result


    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else: 
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length +=1


    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next
            
    
    def rev_traverse(self):
        current_node = self.tail
        while current_node:
            print(current_node.value)
            current_node = current_node.prev


    def search(self,target):
        index = 0
        temp_node = self.head
        while temp_node:
            if temp_node.value ==target:
                return index
            temp_node = temp_node.next
            index +=1
        return -1

    def get(self,index):
        if index < 0 or index >= self.length:
            return False 
        if index < self.length //2:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail
            for _ in range(self.length-1,index,-1):
                current_node = current_node.prev
        return current_node



    def set_value(self,index,value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False
    
    
    def insert(self,value,index):
        new_node = Node(value)
        if index <0 or index > self.length:
            return None
        if index == 0:
            self.prepend(value)
            return
        elif index == self.length:
            self.append(value)
            return
        temp_node = self.get(index-1) 
        new_node.next = temp_node.next
        new_node.prev = temp_node
        temp_node.next.prev = new_node
        temp_node.next = new_node
        
        
    def pop_first(self):
        if not self.head:
            return None
        popped_node = self.head
        if self.length ==1:
            self.head = None
            self.tail = None
        else:
            self.head =self.head.next
            self.head.prev = None
            popped_node.next = None
        self.length -= 1 
        return popped_node       
        
        
    
    def pop(self):
        popped_node = self.tail
        if not self.head:
            return None
        if self.length ==1:
            self.head == None
            self.tail == None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            popped_node.prev = None
        self.length -=1
        return popped_node
    
        
    def remove(self,index):
        if index == 0:
            return self.pop_first()
        if index <0 or index > self.length:
            return None
        if index == self.length-1:
            return self.pop()
        current_node = self.get(index-1)
        popped_node = current_node.next
        next_node = popped_node.next
        current_node.next = popped_node.next
        next_node.prev = current_node
        self.length-=1
        
    
newdll = DoublyLinkedList2()
newdll.append(10)
newdll.append(20)
newdll.append(20)
newdll.prepend(30)
print(newdll)
newdll.remove(3)
print(newdll)
