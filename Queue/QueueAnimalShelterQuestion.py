class AnimalShelter:
    def __init__(self):
        self.cat = []
        self.dog = []
        
    def enqueue(self,animal,type):
        if type == 'cat':
            self.cat.append(animal)
        else:
            self.dog.append(animal)
            
    def dequeueCat(self):
        if len(self.cat) == 0:
            return None
        else:
            return self.cat.pop(0)
        
    def dequeueDog(self):
        if len(self.dog) == 0:
            return None
        else:
            return self.dog.pop(0)
        
    def dequeueAny(self):
        if len(self.cat) == 0:
            result = self.dog.pop(0)
        else:
            result = self.cat.pop(0)
        return result
    
    
customQueue = AnimalShelter()
customQueue.enqueue('dog1','dog')
customQueue.enqueue('dog2','dog')
customQueue.enqueue('dog3','dog')
customQueue.enqueue('cat1','cat')
customQueue.enqueue('dog4','dog')
customQueue.enqueue('cat2','cat')
print(customQueue.dequeueDog())
print(customQueue.dequeueCat())