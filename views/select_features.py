import tkinter as Tk

class Select_features:
  """
  Class for the view displaying available features in a file
  """
  def __init__(self, root, features):
    """
    Sets master frame and packs self

    Gets features from controller and displayes them with a checkbox for each
    """
    self.frame = Tk.Frame(root)
    self.frame.grid(row=0, column=2, rowspan=2)
    lbl_title = Tk.Label(self.frame, text="Select features")
    lbl_title.grid(row=0, columnspan=2)

    self.feature_dict = {}
    
    for feature in features:
      self.feature_dict[feature] = Tk.IntVar()

    for r, feature in enumerate(features):
      lbl = Tk.Label(self.frame, text=feature)
      lbl.grid(row=r+1, column=0, sticky="W")
      self.checkbtn = Tk.Checkbutton(self.frame, variable=self.feature_dict[feature])
      self.checkbtn.grid(row=r+1, column=1, sticky="E")

    lbl_title_label = Tk.Label(self.frame, text="Select (one)label")
    lbl_title_label.grid(row=0, column=2, columnspan=2)
    
    self.selected_label = Tk.StringVar()
    self.selected_label.set(features[0])
    optn_menu_labels = Tk.OptionMenu(self.frame, self.selected_label, *features)
    optn_menu_labels.grid(row=1, column=3)

