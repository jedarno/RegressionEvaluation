import tkinter as Tk

class Data_box:

  def __init__(self, root):
    self.frame = Tk.Frame(root)
    self.frame.grid(row=0, column=1)
    
    self.lbl_csv = Tk.Label(self.frame, text="Enter name of csv file as 'name.csv'")
    self.lbl_csv.grid(row=0, column=0)

    self.ent_csv = Tk.Entry(self.frame)
    self.ent_csv.grid(row=0, column=1)

    self.btn_add_data = Tk.Button(self.frame, text="Add Data")
    self.btn_add_data.grid(row=1, column=1)
 
    self.lbl_boston = Tk.Label(self.frame, text="If no file is provided, the boston \n  housing data set will be used.")
    self.lbl_boston.grid(row=2)
    
