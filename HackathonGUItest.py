import tkinter as tk
from PIL import ImageTk, Image

class RoundButton(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(width=120, height=120, highlightthickness=0, bd=0)
        self.bind('<Button-1>', self.on_click)
        self.bind('<space>', self.on_click)

        self.counter = 0

        # Load and display heart icon
        self.heart_img = Image.open("heart.jpg")
        self.heart_img = self.heart_img.resize((200, 200), Image.ANTIALIAS)
        self.heart_icon = ImageTk.PhotoImage(self.heart_img)
        self.create_image(60, 60, image=self.heart_icon)

        # Display counter text
        self.counter_text = self.create_text(60, 90, text=str(self.counter), font=("Arial", 24))

    def on_click(self, event):
        self.counter += 1
        self.itemconfig(self.counter_text, text=str(self.counter))

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Heart Counter")
        self.geometry("500x400")

        # Add background image
        self.background_img = Image.open("background.png")
        self.background_img = self.background_img.resize((480, 800), Image.ANTIALIAS)
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.background_label = tk.Label(self, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.counter_label = tk.Label(self, text="Click the heart or press spacebar to increment:", font=("Arial", 10))
        self.counter_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        self.round_button = RoundButton(self, bg="white")
        self.round_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

if __name__ == "__main__":
    app = App()
    app.mainloop()
