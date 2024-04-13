import tkinter as tk
from tkinter import PhotoImage, Label
from PIL import ImageTk, Image
import time
import Manage_Data

# Initialize variables
counter = 0
start_time = time.time()
intervals = []
first_click = True

def start_calibrate():
    time_title_label.config(text=f"~ Calibrating ~\n")
    count_down(Manage_Data.get_start_null_time())
    root.after(Manage_Data.get_start_null_time()*1000+1, start_collect)

def start_collect():
    time_title_label.place_forget()
    time_left = Manage_Data.get_read_duration_time() + Manage_Data.get_end_null_time() 
    count_down(time_left)
    root.after(time_left*1000+1, end_measure)

def end_measure():
    print('End!')
    filtered_data = Manage_Data.filter(intervals)
    BPM = Manage_Data.calculateBPM(filtered_data)
    print(BPM)

def count_down(time_left):
    if time_left > 0:
        # Update the label with the remaining time
        time_label.config(text=f"{time_left}")
        time_label.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
        root.after(1000, count_down, time_left - 1)
    else:
        # Countdown completed, display a message
        time_label.place_forget()

def on_click(event):
    global start_time, first_click

    if first_click:
        first_click = False
        start_calibrate()

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

# Create the root window
root = tk.Tk()
root.title("Heart Counter")
root.geometry("400x770")
root.resizable(False, False)

# Add background image (you can replace this with your actual background image)
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

# Create a label for displaying the countdown timer
time_title_label = tk.Label(root, text="", font=("Helvetica", 25),bg = 'white')
time_title_label.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
time_label = tk.Label(root, text="", font=("Helvetica", 40),bg = 'white')
time_label.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

root.bind('<space>', on_space)

update(14)

root.mainloop()
