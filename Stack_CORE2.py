



from collections import deque
class A:
    def __init__(self,Max,top=-1):
        self.Max=Max
        self.num=deque()
        self.top=top
    def ins(self):
        for i in range (self.Max):
            self.num.append(int(input()))
        else:
            print("full stack")
            return self.num
    def pop(self):
        if len(self.num)>0:
            self.num.pop()
            return self.top
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
                
    def __str__ (self):
        return self.num
        
        
    def __repr__(self):
        return self.num
