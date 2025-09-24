class Solution:
    def canJump(self, nums: List[int]) -> bool:
        final_idx = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= final_idx:
                final_idx = i
        # print(final_idx)
        return final_idx == 0