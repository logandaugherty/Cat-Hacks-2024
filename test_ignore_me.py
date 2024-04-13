import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import os

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self, width=500, height=500)
        self.canvas.pack()

        # Load the gif
        self.image = Image.open("heart_beat.gif")
        self.frames = [ImageTk.PhotoImage(frame.copy().convert('RGBA')) for frame in ImageSequence.Iterator(self.image)]

        # Center the gif
        self.x = (500 - self.frames[0].width()) // 2
        self.y = (500 - self.frames[0].height()) // 2

        # Bind space bar to the display_image function
        self.master.bind('<space>', self.display_image)

    def display_image(self, event):
        # Draw the gif centered when space bar is pressed
        for frame in self.frames:
            self.canvas.create_image(self.x, self.y, image=frame)
            self.canvas.update()

root = tk.Tk()
app = Application(master=root)
app.mainloop()
