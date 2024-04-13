import tkinter as tk
from PIL import ImageTk, Image

import Manage_Data
import time

# Initialize variables
space_pressed = False
start_time = time.time()
intervals = []

begin_time = time.time()

def on_click(event):
    global counter, start_time
    counter += 1
    round_button.itemconfig(counter_text, text=str(counter))  # Update the text directly

    end_time = time.time()
    
    elapsed_time = end_time - start_time

    start_time = time.time()
    intervals.append(elapsed_time)
    print(f"Elapsed time: {elapsed_time:.2f} seconds")

def on_space(event):
    on_click(event)

def validate_input(P):
    if P == "" or P.isdigit() and 0 <= int(P) <= 120:
        return True
    return False

# Initialize variables
counter = 0

# Create the root window
root = tk.Tk()
root.title("Heart Counter")
root.geometry("400x770")
root.resizable(False, False)  # Set window size fixed (not resizable)

# Add background image
background_img = Image.open("background.png")
background_img = background_img.resize((480, 800), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_img)
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a label for counter
counter_label = tk.Label(root, text="Click the heart or press spacebar to increment:", font=("Arial", 10), bg="white")
counter_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

# Create a round button with heart icon
round_button = tk.Canvas(root, width=200, height=200, highlightthickness=0, bd=0, bg="white")
heart_img = Image.open("heart.jpg")
heart_img = heart_img.resize((180, 180), Image.LANCZOS)
heart_icon = ImageTk.PhotoImage(heart_img)
round_button.create_image(100, 100, image=heart_icon)

# Display counter text (centered within the heart icon)
counter_text = round_button.create_text(100, 100, text=str(counter), font=("Arial", 24), anchor=tk.CENTER)

# Create two text inputs (Entry widgets)
validate_integer = root.register(validate_input)
input1 = tk.Entry(root, font=("Arial", 12), validate="key", validatecommand=(validate_integer, "%P"))

# Create a dropdown menu for the right option
options = ["Resting", "Moving"]
selected_option = tk.StringVar(root)
selected_option.set(options[0])  # Default value
dropdown_menu = tk.OptionMenu(root, selected_option, *options)

# Position the text input and dropdown menu side-by-side
input1.place(relx=0.35, rely=0.9, anchor=tk.CENTER)
dropdown_menu.place(relx=0.65, rely=0.9, anchor=tk.CENTER)

# Bind events
round_button.bind('<Button-1>', on_click)
root.bind('<space>', on_space)

# Place the round button
round_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Start the GUI event loop
root.mainloop()
