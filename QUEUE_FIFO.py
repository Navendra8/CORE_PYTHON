


class Queue:
    def __init__(self,max_size=0):
        self.__arr = [None for _ in range(max_size)]
        self.__max_size = max_size
        self.__rear = -1
        self.__front = -1
        
    def get_max_size(self):
        """
            It is used to return the maximum size
        """
        return self.__max_size
    
    def is_empty(self):
        """
            It will return true if the queue is empty
        """
        if self.__rear == -1:
            return True
        return False
    
    def is_full(self):
        """
            It will return true if the queue is full
        """
        if self.__rear == self.get_max_size() - 1:
            return True
        return False
    
    def enqueue(self,ele):
        if self.is_full():
            return "Queue is full"
        else:
            self.__rear += 1
            self.__arr[self.__rear] = ele
            
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            self.__front += 1
            self.__arr[self.__front] = None
            
    def __str__(self):
        return f"{self.__arr}"
