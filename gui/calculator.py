# Simple calculator to practice GUI
# Ray Poynter 2017

from tkinter import  Tk, Label, Button, Entry, IntVar, END, W, E

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.total = 0
        self.entered_number = 0

        self.greet_button = Button(master,text="Greet",command=self.greet)
        self.greet_button.grid(row=1)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

root = Tk()
root.geometry("500x500")
my_gui = Calculator(root)
root.mainloop()