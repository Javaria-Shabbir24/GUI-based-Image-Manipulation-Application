# GUI based image manipulation application
#library for creating GUI apps
import tkinter as tk 
# for file selections dialogs and pop-up messages
from tkinter import filedialog, messagebox ,ttk
# for working with images
from PIL import Image, ImageTk, ImageOps
import os
import io

img = None #loaded image
root = tk.Tk()
root.title("Image Manipulation Application")
root.geometry("400x300")  #window size fixed
format_var = tk.StringVar(value="jpg")# to hold the value of selected format

# function to load an image
def Load_Image(): 
    global img
    file_path = filedialog.askopenfilename()
    if file_path:
        img = Image.open(file_path)

# function to save the image
def save_image():
    global img
    if img is None:
        messagebox.showerror("Error", "No image loaded to save!")
        return
    
    if not format_var.get():
        messagebox.showerror("Error", "No format selected!")
        return
    
    # Ask the user where to save the file
    file_path = filedialog.asksaveasfilename(defaultextension=f".{format_var.get()}", filetypes=[("Image Files", {format_var.get()})])
    if file_path:
        try:
            img.save(file_path, format=format_var.get().upper())
            messagebox.showinfo("Success", "Image saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save image: {e}")

# Function to display image information
def show_image_info():
    global img
    if img is None:
        messagebox.showerror("Error", "No image loaded to display information!")
        return

    # Get image details
    width, height = img.size
    format = img.format
    original_size = img.tobytes()  # Converting image to bytes
    original_file_size = len(original_size)  # Size in bytes

    # Image temporarily saved to get compressed size
    with io.BytesIO() as temp_file: #enables working with binary data without creating actual file on hard disk
        img.save(temp_file, format=format)
        compressed_size = len(temp_file.getvalue())  # Compressed size in bytes

    # Calculation of compression ratio
    compression_ratio = (compressed_size / original_file_size) if original_file_size > 0 else 0

    # Display image details
    info = (
        f"Width: {width}px\n"
        f"Height: {height}px\n"
        f"Format: {format}\n"
        f"Original File Size: {original_file_size} bytes\n"
        f"Compressed File Size: {compressed_size} bytes\n"
        f"Compression Ratio: {compression_ratio:.2f}"
    )
    messagebox.showinfo("Image Info", info)



# Heading for browsing
heading_label = tk.Label(root, text="Click to browse the images", font=("Arial", 14))
heading_label.pack(pady=20)  # vertical padding

# Create the browse button
browse_button = tk.Button(root, text="Browse", command=Load_Image)
browse_button.pack()  

# label for the dropdown
format_label = tk.Label(root, text="Select format to save the image:")
format_label.pack(pady=10)

# Dropdown list for formats
format_dropdown = ttk.Combobox(root, textvariable=format_var, values=["jpg", "png", "bmp", "tiff"], state="readonly")
format_dropdown.pack(pady=5)

#save button to save the image in selected format
save_button = tk.Button(root, text="Save Image", command=save_image)
save_button.pack(pady=20)  # Vertical padding

# label for the Image Info button
format_label = tk.Label(root, text="Click to find the information of the selected image:")
format_label.pack(pady=10)

# Image Info button
info_button = tk.Button(root, text="Image Info", command=show_image_info)
info_button.pack(pady=20)  # Vertical padding
root.mainloop()
