

class Queue_:
    def __init__(self,max_size):
        self.__arr = []
        self.__max_size = max_size
        
    def get_max_size(self):
        """
            It is used to return the maximum size
        """
        return self.__max_size
    
    def is_empty(self):
        """
            It will return true if the queue is empty
        """
        if len(self.__arr):
            return False
        return True
            
    def is_full(self):
        """
            It will return true if the queue is full
        """
        if len(self.__arr) == self.get_max_size():
            return True
        return False
    
    def enqueue(self,ele):
        if self.is_full():
            return "Queue is full"
        else:
            self.__arr.append(ele)
            
    def dequeue(self):
        if self.is_empty():
            return "queue is empty"
        else:
            self.__arr.pop(0)
            
    def __str__(self):
        return f"{self.__arr}"
    
    def __repr__(self):
        return f"{self.__arr}"
            
