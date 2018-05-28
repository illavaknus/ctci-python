from random import randint

class StackOfPlates:
    def __init__(self,size=10):
        self.size = size
        self.stack = [[0] * self.size]
        self.top_index = -1
    
    def push(self,item):
        self.top_index += 1
        if (self.top_index + 1) > (len(self.stack) * self.size):
            self.stack.append([0] * self.size)
        self.stack[int(self.top_index / self.size)][self.top_index % self.size] = item
    
    def pop(self):
        if self.top_index == -1:
            raise Exception('Stack is empty')
        temp = self.stack[int(self.top_index / self.size)][self.top_index % self.size]
        self.top_index -= 1
        return temp
    
    def peek(self):
        return self.stack[int(self.top_index / self.size)][self.top_index % self.size]

if __name__ == '__main__':
    sop = StackOfPlates()
    for i in range(1,22):
        sop.push(randint(0,40))

    print(sop.stack)

    for i in range(1,22):
        print(i,sop.pop())
        
