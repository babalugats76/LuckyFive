class Ticket:
    def __init__(self, nums=()):
        self.nums = nums

    def is_match(self, compare_to, threshold=4):
        return len(set(compare_to.nums).intersection(self.nums)) >= threshold

    def to_str(self):
        return " ".join(str(n) for n in self.nums)

    def __str__(self):
        return self.to_str()
