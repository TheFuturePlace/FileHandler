# file_handler_gui
# Ray Poynter 2017

# GUI to allow users to run the options in FileHandler

from tkinter import Tk, Label, Button, W

class FileHGUI(object):
    def __init__(self, master):
        self.master = master
        master.title("File Handler GUI")

        self.label = Label(master, text="This is a test label")
        self.label.pack()

        self.label.grid(columnspan=2, sticky=W)

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.grid(row=1)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=1, column=1)

    def greet(self):
        print("Greetings!")

    def run(self):
        root = Tk()
        root.geometry("500x500")
        my_gui = FileHGUI(root)
        root.mainloop()


# root = Tk()
# root.geometry("500x500")
# my_gui = FileHGUI(root)
# root.mainloop()