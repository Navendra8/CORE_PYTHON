class Stack:
    top= -1
    
    def __init__(self,):
        self.Stack=[]
        self.maximum=int(input("Max number of elements in stack "))
        
    def check_empty(self):
        if self.Stack==[]:
            return "Empty Stack"
        else:
            return "you can go ahead"
    def check_full(self):
        if self.Stack==self.maximum:
            return "FUll Stack"
        else:
            return "You can go ahead"
    def insert (self,element):
        if self.Stack==[]: 
            self.Stack.append(element)
        elif len(self.Stack)<self.maximum:
            self.Stack.append(element)
        else:
            print("Stack is full max limit is :",self.maximum)
      
    def pop(self):
        if len(self.Stack)>0:
            self.Stack.pop()
            return a
        else:
            print("Stack already empty")
            
