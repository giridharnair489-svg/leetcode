class Solution:
    def jump(self, nums: List[int]) -> int:
        curr_end = 0
        curr_far = 0
        answer = 0
        n = len(nums)

        for i in range(n - 1):
            curr_far = max(curr_far, i + nums[i])

            if i == curr_end:
                curr_end = curr_far
                answer += 1

        return answer

