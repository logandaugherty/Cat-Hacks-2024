import tkinter as tk
from PIL import Image, ImageTk

class ImageSwitcherApp:
    def __init__(self, master):
        self.master = master
        self.current_image_index = 0

        # Load images
        self.images = [
            Image.open("1.png"), 
            Image.open("2.png"), 
            Image.open("background.png"), 
            Image.open("2.png")
        ]
        self.image_labels = []

        # Create image labels
        for image in self.images:
            image = image.resize((480, 800), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            label = tk.Label(master, image=photo)
            label.image = photo  # Keep a reference to prevent garbage collection
            self.image_labels.append(label)

        # Display initial image
        self.current_image_label = self.image_labels[self.current_image_index]
        self.current_image_label.pack()

        # Create entry widgets for age and gender
        self.age_label = tk.Label(master, text="Age:")
        self.age_entry = tk.Entry(master)

        self.gender_label = tk.Label(master, text="Gender (M/F):")
        self.gender_entry = tk.Entry(master)

        # Bind space bar key to switch image
        master.bind("<space>", self.switch_image)

        # Dictionary to store entered data
        self.data = {"age": None, "gender": None}

    def switch_image(self, event):
        print("Switching image...")  # Debug statement
        print("Current image index before:", self.current_image_index)  # Debug statement
        if self.current_image_index < len(self.images) - 1:
            # Save entered data before switching the image
            if self.current_image_index == 1:
                self.data["age"] = self.age_entry.get()
                self.data["gender"] = self.gender_entry.get()

            # Increment current image index
            self.current_image_index += 1

            # Update image label
            self.current_image_label.pack_forget()
            self.current_image_label = self.image_labels[self.current_image_index]
            self.current_image_label.pack()

            # Show entry widgets only on the second image
            if self.current_image_index == 1:
                self.age_label.place(x=50, y=400)
                self.age_entry.place(x=150, y=400)
                self.gender_label.place(x=50, y=430)
                self.gender_entry.place(x=150, y=430)
            else:  # Hide entry widgets on other images
                self.age_label.place_forget()
                self.age_entry.place_forget()
                self.gender_label.place_forget()
                self.gender_entry.place_forget()
        else:
            # Reset current image index to cycle through images again
            self.current_image_index = 0

            # Update image label
            self.current_image_label.pack_forget()
            self.current_image_label = self.image_labels[self.current_image_index]
            self.current_image_label.pack()

            # Print debug statement to terminal when switching to the fourth page
            print("Current image index after:", self.current_image_index)  # Debug statement
            if self.current_image_index == 0:  # Change the condition here
                print("Switched to the fourth page")
                # Print collected data
                print("Collected data:")
                print("Age:", self.data["age"])
                print("Gender:", self.data["gender"])

def main():
    root = tk.Tk()
    root.title("Heart Counter")
    root.geometry("400x770")
    root.resizable(False, False)  # Set window size fixed (not resizable)
    app = ImageSwitcherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
