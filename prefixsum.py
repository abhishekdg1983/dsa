class NumArray:
# https://leetcode.com/problems/range-sum-query-immutable/solutions/5689337/prefix-sum-approach/
    def __init__(self, nums: List[int]):
        self.prefix_sum = []
        current_sum = 0
        for num in nums:
            current_sum += num
            self.prefix_sum.append(current_sum)

    def sumRange(self, left: int, right: int) -> int:
        prefix_sum = self.prefix_sum
        prefix_sum_r = prefix_sum[right]

        if left == 0:
            prefix_sum_l = 0
        else:
            prefix_sum_l = prefix_sum[left - 1]
        return prefix_sum_r - prefix_sum_l
