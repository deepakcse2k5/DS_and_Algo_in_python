class Stack():
    def __init__(self) -> None:
        self.items=[]
    def push(self,item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return self.items == []
    def get_stack(self):
        return self.items
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    
            
        
    