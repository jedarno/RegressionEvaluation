import tkinter as tk

from views.boxplot import boxplot
from model import Model
from view import View

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

class Controller:
  """
  class to act as the controller in the mvc. Actsa as an observer for the view.
  All communication between the view and the model goes throught the controller
  """

  def __init__(self):
    """
    Initialiser function, initialises instance of controller object. Created a view and model and sets commands
    for buttons in the view.
    """
    self.root = tk.Tk()
    self.model = Model()
    self.view = View(self.root, self.model)
    self.has_csv = False

    self.view.model_selection.btn_test_models.config(command=self.run_test)
    self.view.data_box.btn_add_data.config(command=self.get_csv)

  def run(self):
    """
    Starts the mainloop for the GUI
    Call this to open/start GUI
    """
    self.root.title("Regression method analysis")
    self.root.deiconify()
    self.root.mainloop()

  def run_test(self):
    """
    Called when a user runs a test. Gets results from the model.
    """
    self.ols_selected = self.view.model_selection.ols_selected.get()
    self.ridge_selected = self.view.model_selection.ridge_selected.get()
    self.svr_selected = self.view.model_selection.svr_selected.get()
    self.knn_selected = self.view.model_selection.knn_selected.get()
    self.kernel_selected = self.view.select_kernel.selected_kernel.get()
    selected_features = None
    selected_label = None
    
    if self.has_csv:
      selected_features = self.features_selected()
      selected_label = self.label_selected()

    names, scores, avg_scores = self.model.run_evaluation(self.ols_selected, self.ridge_selected,\
      self.svr_selected, self.knn_selected, features=selected_features, label=selected_label, kernel=self.kernel_selected)

    for name, score in zip(names, avg_scores):

      if name == "Least squares":
        self.view.results.lbl_ols_score.configure(text=score)

      if name == "Ridge":
        self.view.results.lbl_ridge_score.configure(text=score)

      if name == "SVR":
        self.view.results.lbl_svr_score.configure(text=score)

      if name == "KNN":
        self.view.results.lbl_knn_score.configure(text=score) 

    self.view.draw_boxplot(names, scores)

  def get_csv(self):
    """
    Called when user pressed button to add a file. 
    passes file to model and retrieves data from model, sending it to the view.
    """
    self.has_csv = True
    filename = self.view.data_box.ent_csv.get()
    self.model.add_data(filename)
    features = self.model.get_features()
    self.view.draw_features(features)

  def features_selected(self):
    """
    Gets the users feature selection from the view.

    return: A list object containing the names of the features as strings
    """
    feature_dict = self.view.select_features.feature_dict
    features = []

    for feature in feature_dict:
      if feature_dict[feature].get() == 1:
        features.append(feature)

    return features    

  def label_selected(self):
    """
    Gets the users label selection

    return: The selected labal as a string
    """
    return self.view.select_features.selected_label.get()


