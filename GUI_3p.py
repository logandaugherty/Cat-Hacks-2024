import tkinter as tk
from tkinter import PhotoImage, Label
from PIL import ImageTk, Image
import time

def on_click(event):
    global start_time

    # Calculate elapsed time since last click
    end_time = time.time()
    elapsed_time = end_time - start_time
    start_time = time.time()
    intervals.append(elapsed_time)
    print(f"Elapsed time: {elapsed_time:.2f} seconds")

    # Start the animation
    update(0)

def on_space(event):
    # Trigger on_click function when spacebar is pressed
    on_click(event)

# Initialize variables
counter = 0
start_time = time.time()
intervals = []

# Create the root window
root = tk.Tk()
root.title("Heart Counter")
root.geometry("400x770")
root.resizable(False, False)

# Add background image
background_img = Image.open("background.png")
background_img = background_img.resize((480, 800), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_img)
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Load GIF frames
frameCnt = 16
frames = [PhotoImage(file='heart_Beat2.gif', format='gif -index %i' % i) for i in range(frameCnt)]

def update(ind):
    # Update animation frame
    frame = frames[ind]
    ind += 1
    if ind < frameCnt:
        label.configure(image=frame)
        root.after(10, update, ind)

# Create a label for displaying the animation
label = Label(root, bg='white')
label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
label.bind('<Button-1>', on_click)  # Bind left mouse button click event

# Bind spacebar event
root.bind('<space>', on_space)

# Start the animation
update(14)

# Start the GUI event loop
root.mainloop()
