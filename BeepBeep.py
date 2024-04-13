import tkinter as tk
import pygame.mixer

def on_click(event):
    # Your function logic here
    print("Spacebar pressed!")

def play_beep():
    # Initialize Pygame mixer
    pygame.mixer.init()
    # Load and play the beep sound
    pygame.mixer.music.load("beep.mp3")
    pygame.mixer.music.play()

def beep_on_space(event):
    # Trigger on_click function when spacebar is pressed
    on_click(event)
    # Play the beep sound
    play_beep()

# Create the root window
root = tk.Tk()
root.title("Beep on Spacebar")

# Bind spacebar key to beep_on_space function
root.bind("<space>", beep_on_space)

# Start the Tkinter event loop
root.mainloop()
