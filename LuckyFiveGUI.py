'''
@see https://docs.python.org/3/library/tkinter.html
@see https://effbot.org/tkinterbook
'''
from tkinter import Frame, Button, Label, font

from LuckyFive import LuckyFive


class LuckyFiveGUI(Frame):

    def __init__(self, master, title, **kwargs):
        super().__init__(master)
        self.pack(fill='both', expand=True, padx=5, pady=5)
        self.create_widgets()
        self.master.title(title)
        self.master.minsize(width=250, height=80)
        l5 = LuckyFive(**kwargs)
        l5.load()
        self.lucky_five = l5

    def create_widgets(self):
        # Add "Generate" Button
        self.generate = Button(self)
        self.generate["text"] = "Generate Ticket"
        self.generate["command"] = self.generate_ticket
        self.generate.pack(fill='both', expand=True, padx=5, pady=5, side='top')

        # All Ticket Label
        labelStyle = font.Font(family='monospace', size=20)
        self.ticket = Label(self, font=labelStyle)
        self.ticket["text"] = ""
        self.ticket.pack(fill='both', expand=True, padx=5, pady=5, side='bottom')

        # Add "Quit" Button
        self.quit = Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(fill='both', expand=True, padx=5, pady=5, side='bottom')

    def generate_ticket(self):
        # Generate ticket and update label
        self.ticket["text"] = ""
        new_ticket = self.lucky_five.generate()
        # print(new_ticket)
        self.ticket["text"] = new_ticket.to_str()
