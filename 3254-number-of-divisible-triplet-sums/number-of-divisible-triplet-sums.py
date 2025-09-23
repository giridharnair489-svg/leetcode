class Solution:
    def divisibleTripletCount(self, nums: List[int], d: int) -> int:
        # (nums[i] + nums[j] + nums[k]) % d == 0
        # (nums[i] + nums[j]) % d = a
        # a + (nums[k] % d) = 0
        # a = -(nums[k] % d)
        # -a % d = nums[k]


        # remainder_count = defaultdict(int)
        # for num in nums:
        #     remainder_count[num % d] += 1

        # keys = list(remainder_count.keys())
        # n = len(keys)
        # res = 0

        # for i in range(n):
        #     r1 = keys[i]
        #     for j in range(i, n):
        #         r2 = keys[j]
        #         for k in range(j, n):
        #             r3 = keys[k]

        #             if (r1 + r2 + r3) % d != 0:
        #                 continue

        #             f1, f2, f3 = remainder_count[r1], remainder_count[r2], remainder_count[r3]

        #             if r1 == r2 == r3:
        #                 res += math.comb(f1, 3)
        #             elif r1 != r2 == r3:
        #                 res += math.comb(f2, 2) * f1
        #             elif r1 == r2 != r3:
        #                 res += math.comb(f1, 2) * f3
        #             elif r1 != r3 == r2:
        #                 res += math.comb(f3, 2) * f1
        #             else:
        #                 res += f1 * f2 * f3
        # return res

        n = len(nums)
        remainder_dict = defaultdict(list)
        for i, num in enumerate(nums):
            remainder_dict[num % d].append(i)


        res = 0

        for i in range(n):
            for j in range(i + 1, n):
                a = (nums[i] + nums[j]) % d
                num_k = -a % d
                if num_k in remainder_dict:
                    indices = remainder_dict[num_k]
                    indices_len = len(indices)
                    pos = bisect.bisect_right(indices, j)
                    res += (indices_len - pos)
        return res
