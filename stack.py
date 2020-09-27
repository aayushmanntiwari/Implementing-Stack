'''Stack has the following methods 
1. push - to push element at the last index
2. pop - pop out last index element 
3.peek - return last index element 
5.size - return size of stack items
6.is_empty - check wheather stack items  is empty or not and return 1 or 0
'''

class Stack:
    def __init__(self,items):
        self.items = items

    def push(self):
        '''It will push the element at the last index '''
        self.items.append(5)

    def pop(self):
        '''It will pop out the last element'''
        return self.items.pop()

    def peek(self):
        '''It will return last element '''
        return self.items[-1]

    def size(self):
        '''It will return the size of the stack'''
        if self.items is not None:
            return len(self.items)
        else:
            return None
            
    def is_empty(self):
        '''It will check wheather list is empty or not  '''
        if self.items == [] :
            return True
        return False

s = Stack([1,2,3,4])
s.push()
print(s.items)
print(s.pop())
print(s.peek())
print(s.size())
print(s.is_empty())




