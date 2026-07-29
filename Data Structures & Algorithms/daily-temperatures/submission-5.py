class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ans = [0]*len(temperatures)

        stack = deque()

        for i, temp in enumerate(temperatures):

            while stack and temp> temperatures[stack[-1]]:
                prev_day = stack.pop()
                ans[prev_day] = i - prev_day
            stack.append(i)
        return ans


        