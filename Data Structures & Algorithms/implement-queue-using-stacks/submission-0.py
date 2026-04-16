class MyQueue:

    def __init__(self):
        # [1,2],3
        # [1,2,3]
        self.stack1 = []
        self.stack2 = []
        # Goal = [2,1]
        # [2,1] 
        # []
        # You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
        # [1,2]


    def push(self, x: int) -> None:
        # empty contents of stack 1 into stack 2 then append the val to self.stack1 as the 'last value'
        while self.stack1:
            val = self.stack1.pop()
            self.stack2.append(val)
        self.stack1.append(x)
        while self.stack2:
            val = self.stack2.pop()
            self.stack1.append(val)
        # now its at the top viola


        

    def pop(self) -> int:
        # just get rid of the first element in pop
        # what if there is no element?
        return self.stack1.pop() if self.stack1 else -1
        

    def peek(self) -> int:

        return self.stack1[-1] if self.stack1 else -1
        

    def empty(self) -> bool:
        return len(self.stack1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()