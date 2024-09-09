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
root.resizable(False, False) # window resizing disabled

# Add the browse button to load image
browse_button = tk.Button(root, text="Browse", command=Load_Image)
browse_button.pack()

root.mainloop()
