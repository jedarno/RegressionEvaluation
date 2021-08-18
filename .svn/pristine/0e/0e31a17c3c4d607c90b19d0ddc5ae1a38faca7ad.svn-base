import tkinter as Tk
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

class Boxplot:
  
  def __init__(self, root, algorithms, results):
    self.frame = Tk.Frame(root)
    fig = plt.figure()
    ax = fig.add_subplot()
    plt.boxplot(results)
    ax.set_xticklabels(algorithms)    

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=2, columnspan=2)
    
