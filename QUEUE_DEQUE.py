

class Search:
    """
        This class consists of methods used for searching
    """
    def __init__(self,arr):
        self.arr = arr
        
    def linear_search(self,ele):
        """ A function to search an element into array"""
        self. c= 0
        for i in range(len(self.arr)):
            self.c += 1
            if self.arr[i] == ele:
                return i+1,self.c
        else:
            return "No such element in the list"
        
    def binary_search(self,ele):
        if ele in self.arr:
            self.arr.sort()
            n = len(self.arr)
            low = 0
            high = n
            self.c = 0
            while low<=high:
                self.c += 1
                mid = ( low + high ) //2
                if ele == self.arr[mid]:
                    return self.arr,mid+1,self.c
                elif ele > l[mid]:
                    low = mid + 1
                elif ele < l[mid]:
                    high = mid - 1

        else:
            return "No such element"
        
    
obj = Search([1,2,3,14,15,18,90])
print(obj.linear_search(1))
print(obj.binary_search(1))
