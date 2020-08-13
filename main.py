'''
Bootstrap
'''

from tkinter import Tk

from LuckyFiveGUI import LuckyFiveGUI

root = Tk()
app = LuckyFiveGUI(root, 'Lucky Five', datafile="tickets.dat", max_num=48, num_count=5, compare_to_threshold=4)
app.mainloop()

"""
# Test Ticket class
from Ticket import Ticket
n = random.sample(range(48), 5)
t = Ticket(n)
print(t)
"""

"""
# Test LuckyFive
from LuckyFive import LuckyFive
l5 = LuckyFive("tickets.dat",max_num=48,num_count=5,compare_to_threshold=2)
l5.load()
for t in l5.past_tickets:
    print(t)
nt = l5.generate()
print("New Ticket %s" % nt)
"""
