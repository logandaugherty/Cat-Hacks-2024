from tkinter import *

root = Tk()
canvas_width = 280
canvas_height = 50

w = Canvas(root, width=canvas_width, height=canvas_height)
w.pack()

# Load the frames from the GIF file (replace 'mygif.gif' with your actual file path)
frameCnt = 12
frames = [PhotoImage(file='heartBeat.gif', format='gif -index %i' % i) for i in range(frameCnt)]

def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(100, update, ind)

label = Label(root)
label.pack()

# Start the animation
update(0)

root.mainloop()
