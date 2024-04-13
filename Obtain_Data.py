import tkinter as tk
import pandas as pd
import time

import Manage_Data

# Initialize variables
space_pressed = False
start_time = time.time()
intervals = []

begin_time = time.time()

def on_key_press(event):
    global space_pressed, start_time

    if event.keysym == "space":
        end_time = time.time()
        
        elapsed_time = end_time - start_time

        start_time = time.time()
        intervals.append(elapsed_time)
        print(f"Elapsed time: {elapsed_time:.2f} seconds")
        print(f"Total Time: {time.time()-begin_time:.2f} seconds")

def display_array():
    filtered_data = Manage_Data.filter(intervals)
    BPS = Manage_Data.calculateBPS(filtered_data)
    print(BPS)

# Create the root window
root = tk.Tk()
root.title("Space Bar Timer")

# Bind the space bar key press event
root.bind("<KeyPress>", on_key_press)

# Add a button to display the array
array_button = tk.Button(root, text="Display Array", command=display_array)
array_button.pack()

# Start the GUI event loop
root.mainloop()

