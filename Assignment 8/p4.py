class PairFinder:
    def __init__(self, numbers, target):
        self.numbers = numbers
        self.target = target

    def find_pair(self):
        num_dict = {}
        for i, num in enumerate(self.numbers):
            complement = self.target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return None