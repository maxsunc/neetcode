class MinStack:

    def __init__(self):
        # make a stack class
        # [5,3,7,6,7]

        # keep another stack that tracks the current min which we have
        # 
        self.stack = []
        self.curMinStack = []

        # [5,3,7]

    def push(self, val: int) -> None:
        # O(1)
        # put onto the top of the stack
        # compares top of curMinStack with val to see if we get a new minmium (only if curMinStack is not empty tho)
        minVal = val if not self.curMinStack else min(self.curMinStack[-1],val);
        self.curMinStack.append(minVal)
        self.stack.append(val)

    def pop(self) -> None:
        # take off the top
        self.stack.pop()
        self.curMinStack.pop()
        

    def top(self) -> int:
        # get the top value if it exists
        return self.stack[-1]
        

    def getMin(self) -> int:
        # gets the minimium element
        # 
        return self.curMinStack[-1]
        
