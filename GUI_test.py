import tkinter as tk
from PIL import ImageTk, Image

def on_click(event):
    global counter
    counter += 1
    counter_text.config(text=str(counter))

def on_space(event):
    on_click(event)

# Initialize variables
counter = 0

# Create the root window
root = tk.Tk()
root.title("Heart Counter")
root.geometry("500x400")

# Add background image
background_img = Image.open("background.png")
background_img = background_img.resize((480, 800), Image.ANTIALIAS)
background_photo = ImageTk.PhotoImage(background_img)
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a label for counter
counter_label = tk.Label(root, text="Click the heart or press spacebar to increment:", font=("Arial", 10), bg="white")
counter_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

# Create a round button with heart icon
round_button = tk.Canvas(root, width=200, height=200, highlightthickness=0, bd=0, bg="white")
heart_img = Image.open("heart.jpg")
heart_img = heart_img.resize((180, 180), Image.ANTIALIAS)
heart_icon = ImageTk.PhotoImage(heart_img)
round_button.create_image(100, 100, image=heart_icon)

# Display counter text
counter_text = round_button.create_text(60, 90, text=str(counter), font=("Arial", 24))

# Other text
#text_label = tk.Label(root, text="Hello, world!", font=("Arial", 24), fg="blue", bg="white", justify="center")
#text_label.pack(pady=20)  # Adjust padding as needed

# Bind events
round_button.bind('<Button-1>', on_click)
root.bind('<space>', on_space)

# Place the round button
round_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Start the GUI event loop
root.mainloop()
