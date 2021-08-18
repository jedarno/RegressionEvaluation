import tkinter as Tk

class Results:

  def __init__(self, root):
    self.frame = Tk.Frame(root, relief="solid", borderwidth=1)
    self.frame.grid(row=1, column=1)

    self.frame.rowconfigure([0,1,2,3,4], minsize=10, weight=1)
    self.frame.columnconfigure([0,1], minsize=200, weight=1)

    self.lbl_table_title = Tk.Label(self.frame, text="Results", relief="solid")
    self.lbl_table_title.grid(row=0, sticky = "NESW", columnspan=2)

    self.lbl_desc_title = Tk.Label(self.frame, text="Algorithm", font="Helvetica 16 bold")
    self.lbl_desc_title.grid(row=1, column=0, sticky = "W")
    self.lbl_score_title = Tk.Label(self.frame, text="Average Score", font="Helvetica 16 bold")
    self.lbl_score_title.grid(row=1, column=1, sticky = "E")  

    self.lbl_ols_desc = Tk.Label(self.frame, text="Ordinary Least Squares")
    self.lbl_ols_desc.grid(row=2, column=0, sticky = "W")
    self.lbl_ols_score = Tk.Label(self.frame, text="")
    self.lbl_ols_score.grid(row=2, column=1, sticky = "E")

    self.lbl_ridge_desc = Tk.Label(self.frame, text="Ridge Regression")
    self.lbl_ridge_desc.grid(row=3, column=0, sticky = "W")
    self.lbl_ridge_score = Tk.Label(self.frame, text="")
    self.lbl_ridge_score.grid(row=3, column=1, sticky = "E")

    self.lbl_svr_desc = Tk.Label(self.frame, text="Support Vector Regression")
    self.lbl_svr_desc.grid(row=4, column=0, sticky = "W")
    self.lbl_svr_score = Tk.Label(self.frame, text="")
    self.lbl_svr_score.grid(row=4, column=1, sticky = "E")

    self.lbl_knn_desc = Tk.Label(self.frame, text="K Nearest Neighbours Regression")
    self.lbl_knn_desc.grid(row=5, column=0, sticky = "W")
    self.lbl_knn_score = Tk.Label(self.frame, text="")
    self.lbl_knn_score.grid(row=5, column=1, sticky = "E")
