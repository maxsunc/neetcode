class MyQueue:

    def __init__(self):
        # we just want to use two stacks
        self.stack1 = []
        self.stack2 = []

        # [2,4,5,6]
        # [5,4,2],[2,4]


    def push(self, x: int) -> None:
        
        # remove what we have on stack1 onto stack2
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        # add to stack 1
        self.stack1.append(x)

        # add back the stuff rom stack2
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def pop(self) -> int:
        # just call pop from the stack
        return self.stack1.pop()
        

    def peek(self) -> int:
        # return the first element
        return self.stack1[-1]
        

    def empty(self) -> bool:
        # reutrn wehther stack1 is empty or not
        return len(self.stack1) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()