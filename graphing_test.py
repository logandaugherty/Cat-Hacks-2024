import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import random

def moving_avg(intervals):
    result = []
    for i in range (len(intervals)):
        moving_avg_max_i = 5
        moving_avg_min_i = 0
        if i < moving_avg_max_i:
            moving_avg_max_i = i
        else:
            moving_avg_min_i = i - 5
        
        length = moving_avg_min_i + moving_avg_max_i
        time_sum = 0
        for time_i in range (moving_avg_min_i, moving_avg_max_i):
            time_sum += intervals[time_i] / length
        
        result.append(time_sum)
    
    return result
            
            

def plot_graph(root, intervals):

    # Define your data values
    y = intervals
    t = range(len(intervals))

    # Create a figure
    fig = plt.figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(t, y)
    ax.set_xlabel("Time [s]")
    ax.set_ylabel("f(t)")
    ax.set_title("Beat intervals over index")
    ax.set_xbound(0.05,1.5)

    # Create a canvas for the figure
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()

    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Center the application window
    # center(root)

    # Start the Tkinter event loop

if __name__ == "__main__":

    test_data = []
    for i in range(100):
        test_data.append(random.randrange(900, 1100)/1000.0)

    root = tk.Tk()
    root.title("Matplotlib in Tkinter")
    root.geometry("600x600")
    plot_graph(root,test_data)
    root.mainloop()
