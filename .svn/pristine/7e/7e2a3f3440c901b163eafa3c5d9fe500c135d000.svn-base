import tkinter as Tk

class Model_selection():

  def __init__(self, root):
    self.frame = Tk.Frame(root)
    self.frame.grid(row=0, column=0)

    lbl_ols = Tk.Label(self.frame, text="Ordinary Least Squares")
    lbl_ols.grid(row=0, column=0, sticky="W")

    self.ols_selected = Tk.IntVar()
    self.checkbtn_ols = Tk.Checkbutton(self.frame, variable = self.ols_selected)
    self.checkbtn_ols.grid(row = 0, column = 1, sticky = "E")
     
    lbl_ridge = Tk.Label(self.frame, text="Ridge Regression")
    lbl_ridge.grid(row=1, column=0, sticky="W")

    self.ridge_selected = Tk.IntVar()
    self.checkbtn_ridge = Tk.Checkbutton(self.frame, variable = self.ridge_selected)
    self.checkbtn_ridge.grid(row = 1, column = 1, sticky = "E")

    lbl_svr = Tk.Label(self.frame, text="Support Vector Regression")
    lbl_svr.grid(row = 2, column=0, sticky="W")

    self.svr_selected = Tk.IntVar()
    self.checkbtn_svr = Tk.Checkbutton(self.frame, variable = self.svr_selected)
    self.checkbtn_svr.grid(row = 2, column = 1, sticky = "E")
    
    lbl_knn = Tk.Label(self.frame, text="K Nearest Neighbours")
    lbl_knn.grid(row = 3, column=0, sticky="W")

    self.knn_selected = Tk.IntVar()
    self.checkbtn_knn = Tk.Checkbutton(self.frame, variable = self.knn_selected)
    self.checkbtn_knn.grid(row = 3, column = 1, sticky = "E")

    self.btn_test_models = Tk.Button(self.frame, text = "Test Models!")
    self.btn_test_models.grid(row = 4)
