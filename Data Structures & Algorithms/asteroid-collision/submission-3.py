class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i,val in enumerate(asteroids):
            if val > 0:
                stack.append(val)
            elif val < 0:
                maxVal = 0
                while stack:
                    maxVal = max(maxVal, stack[-1])
                    if stack[-1] > 0 and stack[-1] <= abs(val):
                        if stack[-1] < abs(val):
                            # we can break it
                            stack.pop()
                        elif stack[-1] == abs(val):
                            stack.pop()
                            break
                    else:
                        # we're either not bigger or its negative
                        if stack[-1] < 0:
                            stack.append(val)
                        break
                if not stack and maxVal < abs(val):
                    stack.append(val)

        return stack