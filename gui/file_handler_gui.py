# file_handler_gui
# Ray Poynter 2017

# GUI to allow users to run the options in FileHandler

from tkinter import Tk, Label, Button, W
from gui.greet import Greet

class FileHGUI(object):
    def __init__(self):
        self.master = Tk()
        self.master.geometry("500x500")
        self.master.title("File Handler GUI")

        self.label = Label(self.master, text="This is a test label")
        self.label.pack()

        self.label.grid(columnspan=2, sticky=W)

        self.greet_button = Button(self.master, text="Greet", command=self.greet)
        self.greet_button.grid(row=1)

        self.close_button = Button(self.master, text="Close", command=self.master.quit)
        self.close_button.grid(row=1, column=1)

    def greet(self):
        Greet.display()
        # print("Greetings!")

    def run(self):
        self.master.mainloop()