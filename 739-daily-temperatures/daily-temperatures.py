class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer=[0]*len(temperatures)
        stack=[]
        for i,temp in enumerate(temperatures):
            while stack and temp>temperatures[stack[-1]]:
                prev_day_index=stack.pop()

                answer[prev_day_index]=i-prev_day_index

            stack.append(i)
        return answer
