class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # 2 4 -7 -1

        # (2) -->  (4) -->  <-- (4) <-- (1)

        # stack

        # [2]
        # opposite indicate collision
        # -1 

        # retunr the stack
        stack = []

        for rock in asteroids:
            if not stack:
                # if its empty just add the value
                stack.append(rock)
            else:
                # its not empty, we can make a comparison
                top = stack[len(stack)-1]
                # check if they're different signs
                if top > 0 and rock < 0:
                    # we need to make a collision. case where - dominates
                    while stack and top < abs(rock) and top > 0:
                        stack.pop()
                        if stack:
                            top = stack[-1]
                    if(top > 0):
                        if abs(top) == abs(rock):
                            stack.pop()
                        elif abs(top) < abs(rock):
                            # beats all, append to list
                            stack.append(rock)
                    else:
                        stack.append(rock)
                else:
                    # signs are equal
                    stack.append(rock)
        return stack

                    
