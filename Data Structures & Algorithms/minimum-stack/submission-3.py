class MinStack:

    def __init__(self):
        self.stack = []
        # each function is O(1)??
        # how aare we going to get the min vlaue within the stack
        # somehow keep track of the past min values as well
        # prefix approach to get the minimium element
        # prefix? tf
        # what can we use to store the min element?
        # have another stack that stores the minimium element at each element of the stack
        # that way when we call pop we can also pop from the min element
        # jsut keep track of the current min as the top of the stack
        self.minStack = []
    def push(self, val: int) -> None:
        if not self.minStack:
            # just push it on
            self.minStack.append(val)
        else:
            # compare with the top value which one is more min
            minVal = min(self.getMin(), val)
            self.minStack.append(minVal)
        self.stack.append(val)
        print(self.minStack)
        

    def pop(self) -> None:
        if not self.stack:
            return
        # pop off both
        self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

        
