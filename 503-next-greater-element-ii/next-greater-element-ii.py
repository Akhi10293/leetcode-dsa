class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n=len(nums)
        res=[-1]*n
        stack=[]

        for i in range(2*n-1,-1,-1):
            curr_idx=i%n

            while stack and nums[stack[-1]]<=nums[curr_idx]:
                stack.pop()

            if stack:
                res[curr_idx]=nums[stack[-1]]
            stack.append(curr_idx)
        return res