# Testing running sub progs this just greets
# Ray Poynter
# Sept 2017
from tkinter import Tk, Label, W, Button


class Greet(object):
    def __init__(self):
        self.master = Tk()
        self.master.geometry("300x300")
        self.master.title("Greet sub program")

        self.label = Label(self.master, text="Greet Program")
        self.label.pack()

        self.label.grid(columnspan=2, sticky=W)

        self.close_button = Button(self.master, text="Close", command=self.master.quit)
        self.close_button.grid(row=1, column=1)

    @classmethod
    def display(cls):
        greet = cls()
        greet.master.mainloop()