import tkinter as tk
import time

# Initialize variables
space_pressed = False
start_time = time.time()

def on_key_press(event):
    global space_pressed, start_time

    if event.keysym == "space":
        end_time = time.time()
        
        elapsed_time = end_time - start_time

        start_time = time.time()
        print(f"Elapsed time: {elapsed_time:.2f} seconds")

def display_array():
    print("Array: []")

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

