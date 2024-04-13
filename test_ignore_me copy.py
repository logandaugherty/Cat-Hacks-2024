import tkinter as tk
from PIL import Image, ImageTk
from GUI_3p import BPMRecorderApp
import BPM_Monitor

class ImageSwitcherApp:
    def __init__(self, master):
        self.master = master
        self.current_image_index = 0

        # Load images
        self.images = [
            Image.open("1.png"), 
            Image.open("3.png"), 
            Image.open("5.png")
        ]
        self.image_labels = []

        # Create image labels
        for image in self.images:
            image = image.resize((480, 800))
            photo = ImageTk.PhotoImage(image)
            label = tk.Label(master, image=photo)
            label.image = photo  # Keep a reference to prevent garbage collection
            self.image_labels.append(label)

        # Display initial image
        self.current_image_label = self.image_labels[self.current_image_index]
        self.current_image_label.pack()

        # Create entry widgets for age and type
        self.age_entry = tk.Entry(master)

        # Create dropdown menu for type
        self.type_var = tk.StringVar(master)
        self.type_var.set("Moving")  # Set default value
        self.type_menu = tk.OptionMenu(master, self.type_var, "Moving", "Resting")

        self.bpmAppInitialized = False

        # Bind space bar key to switch image
        master.bind("<space>", self.press_input)

        # Dictionary to store entered data
        self.data = {"age": None, "type": None}

    def press_input(self,event):

        if self.current_image_index == 1 and not self.bpmAppInitialized:
            self.bpmAppInitialized = True
            self.bpmApp = BPMRecorderApp(self.master)

        elif self.current_image_index == 1 and self.bpmApp.completed:
            self.switch_image(event)
            self.bpmApp.hide()
            self.bpmAppInitialized = False

        elif self.current_image_index == 1:
            self.bpmApp.on_click(event)
        else:
            self.switch_image(event)


    def switch_image(self, event):
        print("Switching image...")  # Debug statement
        print("Current image index before:", self.current_image_index)  # Debug statement

        if self.current_image_index < len(self.images) - 1:
            # Save entered data before switching the image
            if self.current_image_index == 1:
                self.data["age"] = self.age_entry.get()
                self.data["type"] = self.type_var.get()

            # Increment current image index
            self.current_image_index += 1

            # Update image label
            self.current_image_label.pack_forget()
            self.current_image_label = self.image_labels[self.current_image_index]
            self.current_image_label.pack()

            # Show entry widgets only on the second image
            if self.current_image_index == 1:
                self.age_entry.place(x=54, y=225)
                self.type_menu.place(x=240, y=220)
            else:  # Hide entry widgets on other images
                self.age_entry.place_forget()
                self.type_menu.place_forget()

            # Print debug statement to terminal when switching to the fourth page
            print("Current image index after:", self.current_image_index)  # Debug statement
            if self.current_image_index == 2:  # Change the condition here
                newBPM = self.bpmApp.getBPM()
                # Print collected data
                print("Collected data:")
                print("Age:", self.data["age"])
                print("Type:", self.data["type"])
                BPM_Monitor.determine_heart_cond(self.data["age"], self.data["type"], newBPM)

        else:
            # Reset current image index to cycle through images again
            self.current_image_index = 0

            # Update image label
            self.current_image_label.pack_forget()
            self.current_image_label = self.image_labels[self.current_image_index]
            self.current_image_label.pack()



def main():
    root = tk.Tk()
    root.title("Heart Counter")
    root.geometry("400x770")
    root.resizable(False, False)  # Set window size fixed (not resizable)
    app = ImageSwitcherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
