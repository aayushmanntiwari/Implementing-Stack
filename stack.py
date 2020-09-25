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

s = Stack([1,2,3,4])
s.push()
print(s.items)
print(s.pop())
print(s.peek())
print(s.size())




