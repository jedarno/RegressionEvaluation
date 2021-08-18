import tkinter as Tk

class Select_kernel:
  """
  Class for view where user selects kernel
  """
  def __init__(self, root):
    """
    initialises and packs view

    param root: the parent for this view
    """
    self.frame = Tk.Frame(root)
    self.frame.grid(row=1, column=0)
  
    kernels = ["linear", "poly"]
    self.selected_kernel = Tk.StringVar()
    self.selected_kernel.set(kernels[0])

    lbl_select_kernel = Tk.Label(self.frame, text="Select kernel")
    lbl_select_kernel.grid(column=0, row = 0)

    optn_menu_kernels = Tk.OptionMenu(self.frame, self.selected_kernel, *kernels)
    optn_menu_kernels.grid(column=1, row = 0)


