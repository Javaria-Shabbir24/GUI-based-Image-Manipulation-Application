import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import io

img = None  # loaded image
threshold = 128  # default threshold

root = tk.Tk()
root.title("Image Manipulation Application")

# Create a Canvas and a vertical scrollbar
canvas = tk.Canvas(root)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)

# Create a Frame to hold the content
content_frame = tk.Frame(canvas)

# Add the Frame to the Canvas
canvas.create_window((0, 0), window=content_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Pack the Canvas and Scrollbar
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Update the Scrollregion whenever the content changes
def update_scrollregion(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

canvas.bind("<Configure>", update_scrollregion)

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
    
    file_path = filedialog.asksaveasfilename(defaultextension=f".{format_var.get()}", filetypes=[("Image Files", format_var.get())])
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

    width, height = img.size
    format = img.format
    original_size = img.tobytes()
    original_file_size = len(original_size)

    with io.BytesIO() as temp_file:
        img.save(temp_file, format=format)
        compressed_size = len(temp_file.getvalue())

    compression_ratio = (compressed_size / original_file_size) if original_file_size > 0 else 0

    info = (
        f"Width: {width}px\n"
        f"Height: {height}px\n"
        f"Format: {format}\n"
        f"Original File Size: {original_file_size} bytes\n"
        f"Compressed File Size: {compressed_size} bytes\n"
        f"Compression Ratio: {compression_ratio:.2f}"
    )
    messagebox.showinfo("Image Info", info)

# Function to convert grayscale image to black and white
def convert_to_black_and_white():
    global img
    if img is None:
        messagebox.showerror("Error", "No image loaded to convert!")
        return

    bw_image = img.point(lambda p: 255 if p > threshold else 0)
    bw_image.show()

# Function to crop the image
def crop_image():
    global img
    if img is None:
        messagebox.showerror("Error", "No image loaded to crop!")
        return

    try:
        left = int(left_entry.get())
        top = int(top_entry.get())
        right = int(right_entry.get())
        bottom = int(bottom_entry.get())
        
        # Check if the coordinates are valid
        if left < 0 or top < 0 or right > img.width or bottom > img.height or left >= right or top >= bottom:
            messagebox.showerror("Error", "Invalid crop coordinates!")
            return
        
        # Perform the cropping
        cropped_image = img.crop((left, top, right, bottom))
        cropped_image.show()
        
        # Show success message with crop details
        cropped_width, cropped_height = cropped_image.size
        status_message = (f"Image cropped successfully!\n"
                          f"Cropping Coordinates: (left={left}, top={top}, right={right}, bottom={bottom})\n"
                          f"Cropped Image Size: {cropped_width}px x {cropped_height}px")
        messagebox.showinfo("Crop Status", status_message)
        
    except ValueError:
        messagebox.showerror("Error", "Invalid crop coordinates!")

# function to resize the image 
def resize_image():
    global img
    if img is None:
        messagebox.showerror("Error", "No image loaded to resize!")
        return

    try:
        width = int(width_entry.get())
        height = int(height_entry.get())
        resized_image = img.resize((width, height))
        resized_image.show()
    except ValueError:
        messagebox.showerror("Error", "Invalid width or height!")

# UI elements in the content frame

# Heading for browsing
heading_label = tk.Label(content_frame, text="Click to browse the images", font=("Arial", 14))
heading_label.pack(pady=20)

# Create the browse button
browse_button = tk.Button(content_frame, text="Browse", command=Load_Image)
browse_button.pack()

# label for the dropdown
format_label = tk.Label(content_frame, text="Select format to save the image:")
format_label.pack(pady=10)

# Dropdown list for formats
format_var = tk.StringVar(value="jpg")
format_dropdown = ttk.Combobox(content_frame, textvariable=format_var, values=["jpg", "png", "bmp", "tiff"], state="readonly")
format_dropdown.pack(pady=5)

# Save button to save the image in selected format
save_button = tk.Button(content_frame, text="Save Image", command=save_image)
save_button.pack(pady=20)

# label for the Image Info button
ImageInfo_label = tk.Label(content_frame, text="Click to find the information of the selected image:")
ImageInfo_label.pack(pady=10)

# Image Info button
info_button = tk.Button(content_frame, text="Image Info", command=show_image_info)
info_button.pack(pady=20)

# label for the conversion to black and white image
conversion_label = tk.Label(content_frame, text="Click to convert selected grayscale image to black and white:")
conversion_label.pack(pady=10)

# Slider to adjust threshold
threshold_slider = tk.Scale(content_frame, from_=0, to=255, orient=tk.HORIZONTAL, label="Threshold")
threshold_slider.set(threshold)
threshold_slider.pack(pady=10)

def update_threshold(value):
    global threshold
    threshold = int(value)

threshold_slider.bind("<Motion>", lambda event: update_threshold(threshold_slider.get()))

convert_button = tk.Button(content_frame, text="Convert to Black and White", command=convert_to_black_and_white)
convert_button.pack(pady=20)

# Label and entry fields for cropping
crop_label = tk.Label(content_frame, text="Crop Image (left, top, right, bottom):")
crop_label.pack(pady=10)

left_label = tk.Label(content_frame, text="Left:")
left_label.pack()
left_entry = tk.Entry(content_frame)
left_entry.pack()

top_label = tk.Label(content_frame, text="Top:")
top_label.pack()
top_entry = tk.Entry(content_frame)
top_entry.pack()

right_label = tk.Label(content_frame, text="Right:")
right_label.pack()
right_entry = tk.Entry(content_frame)
right_entry.pack()

bottom_label = tk.Label(content_frame, text="Bottom:")
bottom_label.pack()
bottom_entry = tk.Entry(content_frame)
bottom_entry.pack()

# Crop button
crop_button = tk.Button(content_frame, text="Crop Image", command=crop_image)
crop_button.pack(pady=20)

# Label for resizing
resize_label = tk.Label(root, text="Resize Image (width, height):")
resize_label.pack(pady=10)

# entry field for width
width_label = tk.Label(root, text="Width:")
width_label.pack()
width_entry = tk.Entry(root)
width_entry.pack()

# entry field for height
height_label = tk.Label(root, text="Height:")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()

# Resize button
resize_button = tk.Button(root, text="Resize Image", command=resize_image)
resize_button.pack(pady=20)

root.mainloop()
