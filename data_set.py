# Data set class
# Ray Poynter - September 2017

# This looks after a range of utlities for CSV variables

# Import section
import csv #std library for comma separated variables
from tkinter import filedialog as fd
from tkinter import messagebox

class DataSet(object):
    def __init__(self,input_file_path="", output_file_path=""):
        self.my_data = []
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.n_rows = 0
        self.min_fields = 0
        self.max_fields = 0

    def get_input_file(self):
        self.input_file_path = fd.askopenfilename()

    def process(self):
        with open(self.input_file_path) as csvfile:
            readCSV = csv.reader(csvfile,delimiter=',')
            for row in readCSV:
                self.my_data.append(row)
                self.n_rows += 1
                if self.n_rows == 1:
                    self.min_fields = len(row)
                    self.max_fields = len(row)
                if len(row) > self.max_fields:
                    self.max_fields = len(row)
                if len(row)<self.min_fields:
                    self.min_fields = len(row)


    def run(self):
        if len(self.input_file_path) < 1:
            self.get_input_file()
        self.process()
        myMessage = "Number of rows=" + str(self.n_rows) + "  Min=" + str(self.min_fields) + "  Max=" + str(self.max_fields)
        messagebox.showinfo("Finished",myMessage)