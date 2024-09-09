# GUI based image manipulation application
#library for creating GUI apps
import tkinter as tk 
# for file selections dialogs and pop-up messages
from tkinter import filedialog, messagebox 
# for working with images
from PIL import Image, ImageTk
# function to load an image
def Load_Image():
    file_path = filedialog.askopenfilename()
    if file_path:
        img = Image.open(file_path)
        img.show()  # Display the image in a separate window for now

# function to save an image 
def save_image():
    pass  # We will implement this later

root = tk.Tk()
root.title("Image Manipulation Application")

root.geometry("400x300")  #window size fixed

# Heading for browsing
heading_label = tk.Label(root, text="Click to browse the images", font=("Arial", 14))
heading_label.pack(pady=20)  # vertical padding

# Create the browse button
browse_button = tk.Button(root, text="Browse", command=Load_Image)
browse_button.pack()  

root.mainloop()
