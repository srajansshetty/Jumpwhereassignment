class SubsetGenerator:
    def __init__(self, nums):
        self.nums = nums

    def generate_subsets(self):
        n = len(self.nums)
        subsets = [[]]
        for i in range(n):
            for j in range(len(subsets)):
                subsets.append(subsets[j] + [self.nums[i]])
        return subsets