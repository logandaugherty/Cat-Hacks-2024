import tkinter as tk
from tkinter import PhotoImage, Label
from PIL import ImageTk, Image
import time
import Manage_Data

class BPMRecorderApp:
    def __init__(self, master):
        self.master = master
        # Initialize variables
        self.counter = 0
        self.start_time = time.time()
        self.intervals = []
        self.first_click = True
        self.completed = False

        # Add background image (replace with your actual background image)
        self.background_img = Image.open("background.png")
        self.background_img = self.background_img.resize((480, 800), Image.LANCZOS)
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.background_label = tk.Label(master, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Load GIF frames
        self.frameCnt = 16
        self.frames = [PhotoImage(file='heart_Beat2.gif', format='gif -index %i' % i) for i in range(self.frameCnt)]

        # Create a label for displaying the animation
        self.label = Label(master, bg='white')
        self.label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.label.bind('<Button-1>', self.on_click)  # Bind left mouse button click event

        # Create a label for displaying the countdown timer
        self.time_title_label = tk.Label(master, text="", font=("Helvetica", 25), bg='white')
        self.time_title_label.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
        self.time_label = tk.Label(master, text="", font=("Helvetica", 40), bg='white')
        self.time_label.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

        self.update(14)

    def hide(self):
        self.label.place_forget()
        self.time_label.place_forget()
        # self.background_img.place_forget()
        self.background_label.place_forget()
        # self.background_photo.place_forget()

    def start_calibrate(self):
        self.time_title_label.config(text=f"~ Calibrating ~\n")
        self.count_down(Manage_Data.get_start_null_time())
        self.master.after(Manage_Data.get_start_null_time()*1000+1, self.start_collect)

    def start_collect(self):
        self.time_title_label.place_forget()
        time_left = Manage_Data.get_read_duration_time() + Manage_Data.get_end_null_time() 
        self.count_down(time_left)
        self.master.after(time_left*1000+1, self.end_measure)

    def end_measure(self):
        filtered_data = Manage_Data.filter(self.intervals)
        BPM = Manage_Data.calculateBPM(filtered_data)
        self.completed = True
        print(BPM)

    def count_down(self,time_left):
        if time_left > 0:
            # Update the label with the remaining time
            self.time_label.config(text=f"{time_left}")
            self.time_label.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
            self.master.after(1000, self.count_down, time_left - 1)
        else:
            # Countdown completed, display a message
            self.time_label.place_forget()

    def on_click(self,event):

        if self.first_click:
            self.first_click = False
            self.start_calibrate()

        # Calculate elapsed time since last click
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        self.start_time = time.time()
        self.intervals.append(elapsed_time)
        print(f"Elapsed time: {elapsed_time:.2f} seconds")

        # Start the animation
        self.update(0)

    def on_space(self,event):
        # Trigger on_click function when spacebar is pressed
        self.on_click(event)

    def update(self,ind):
        # Update animation frame
        frame = self.frames[ind]
        ind += 1
        if ind < self.frameCnt:
            self.label.configure(image=frame)
            self.master.after(10, self.update, ind)

def main():
    # Create the root window
    root = tk.Tk()
    root.title("Heart Counter")
    root.geometry("400x770")
    root.resizable(False, False)
    app = BPMRecorderApp(root)
    
    root.bind('<space>', app.on_space)

    root.mainloop()

if __name__ == "__main__":
    main()
