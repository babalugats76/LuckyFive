import pickle
import random

from Ticket import Ticket


class LuckyFive:
    def __init__(self, datafile=None, max_num=48, num_count=5, compare_to_threshold=4):
        self.datafile = datafile
        self.max_num = max_num
        self.num_count = num_count
        self.compare_to_threshold = compare_to_threshold
        self.past_tickets = []

    def load(self):
        pickled = []
        with open(self.datafile, 'rb') as f:
            pickled = pickle.load(f)
            print("Found %s tickets" % len(pickled))
            for p in pickled:
                self.past_tickets.append(Ticket(p))

    def generate(self):
        nums = random.sample(range(self.max_num), self.num_count)
        new_ticket = Ticket(tuple(nums))
        for old_ticket in self.past_tickets:
            if old_ticket.is_match(new_ticket, self.compare_to_threshold):
                print("%s matches %s" % (new_ticket, old_ticket))
                return self.generate()
        return new_ticket
