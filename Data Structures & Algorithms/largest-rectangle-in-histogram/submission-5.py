class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []  # (start_index, height)

        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                idx, h = stack.pop()
                res = max(res, h * (i - idx))
                start = idx  # inherit start position
            stack.append((start, height))

        for idx, h in stack:
            res = max(res, h * (len(heights) - idx))

        return res