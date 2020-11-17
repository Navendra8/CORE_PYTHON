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
    def __str__(self):
        return self.Stack
    def __repr__(self):
        return self.Stack
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
    def __str__(self):
        print(top)
        return self.Stack
    def __repr__(self):
        print(top)
        return self.Stack
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
            return self.Stack.pop()
        else:
            print("Stack already empty")
    def __str__(self):
        print(top)
        return self.Stack
    def __repr__(self):
        print(top)
        return self.Stack


from collections import deque
class A:
    
    def __init__(self,Max=None):
        self.Max=Max
        self.num=deque()
    def ins(self):
        for i in range (self.Max):
            self.num.append(int(input()))
        else:
            print("full stack")
            return self.num
    def pop(self):
        if len(self.num)>0:
            self.num.pop()
            return self.num.pop()
        else:
            print("stack is empty")
    def check_empty(self):
        if len(self.num)==0:
            return "Stack is empty"
        
    def check_full(self):
            if len(self.num)>self.Max:
                print("Stack is full ")
            else:
                print("Stack is not full ")
        
