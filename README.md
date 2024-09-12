# GUI-based-Image-Manipulation-Application
 
# Load an Image
1.	Function Name:
              Load_Image()
2.	Approach:
This function allows users to browse and load an image using `filedialog.askopenfilename()`. Once a file path is selected, the `Image.open()` function from the PIL (Pillow) library is used to open the image. The loaded image is stored in the global variable `img` and displayed using `img.show()`.
3.	Demo Working and Screenshots

By clicking the Browse button, the user is allowed to navigate and select desired image.
![image](https://github.com/user-attachments/assets/b24beee3-cb9a-4e00-b699-279c8fb2c096)


The selected image is then displayed in a separate window.
 
![image](https://github.com/user-attachments/assets/50bc263f-16ed-4f49-bfcb-b89b5109a5cb)

# Save the image 
1.	Function Name:
save_image()
2.	Approach:
This function saves the currently loaded image in a user-specified format. It first checks if an image is loaded and if a format is selected via the `format_var`. Using `filedialog.asksaveasfilename()`, a save location and format are chosen. The image is then saved using the `img.save()` method, handling any exceptions to ensure error feedback is provided to the user.
3.	Demo Working and Screenshots

Loaded picture is this:
![image](https://github.com/user-attachments/assets/0d3901a4-4a0e-4291-9ee9-435332d3d20a)

Selected format is tiff:
 
![image](https://github.com/user-attachments/assets/49913226-5388-48e0-abcb-73e5aa775176)


Chosen Location is desktop:
![image](https://github.com/user-attachments/assets/3ba01807-00fa-4fff-b18a-fffb4b085a4f)


Image saved successfully as My Image.tiff on desktop
 
![image](https://github.com/user-attachments/assets/6b863bfe-da94-4bd2-9741-8ffa5b5cac37)

![image](https://github.com/user-attachments/assets/8db81615-4fb0-4dbe-a3ac-307b2a7f7c07)


# Image info:

1.	Function Name:
               show_image_info()
2.	Approach:
               This function extracts and displays details such as image width, height, format, and file size. The original file size is computed using the byte size of the image, and the compressed size is calculated by saving the image to a temporary in-memory file. The compression ratio is computed and displayed using a messagebox.
3.	Demo Working and Screenshots

After loading the image, the Image Info button is clicked that displays the desired results in a messagebox.

![image](https://github.com/user-attachments/assets/ab91ba5c-7e0b-4c79-a95d-2b40447549e3)


# Grayscale image to black and white conversion:

1.	Function Name:
              convert_to_black_and_white()

2.	Approach:

This function converts a grayscale image to black and white by applying a threshold value. The `point()` method is used with a lambda function to map pixel values. Pixels above the threshold are set to 255 (white), and those below are set to 0 (black). The converted image is then displayed.
3.	Demo Working and Screenshots

Loaded Grayscale Image:

![image](https://github.com/user-attachments/assets/4a7e0ee0-aabd-4f20-9399-61291b3dcd2c)


Black and White Image:

•	When threshold is set to 240
 
 ![image](https://github.com/user-attachments/assets/ff96ef7a-1693-4bca-afc5-bf1899c75712)

![image](https://github.com/user-attachments/assets/a92ee4ed-830d-49f5-a788-7672cb5833f8)

•	When threshold is set to  101:
 
![image](https://github.com/user-attachments/assets/b8acb7b7-44af-422a-9215-9c4f2803e379)

![image](https://github.com/user-attachments/assets/da1f4c14-d9b5-4655-8867-860151c55de3)
 

# Crop the image

1.	Function Name:
              crop_image()
2.	Approach:
              This function crops the loaded image using user-defined coordinates. The crop dimensions (left, top, right, bottom) are validated to ensure they're within image bounds. The `img.crop()` method is used to perform the cropping operation, and the cropped image is displayed along with the new dimensions
3.	Demo Working and Screenshots

Original Image 
 
![image](https://github.com/user-attachments/assets/cc7fda3d-f4e1-4a72-9e8e-f87acbb50eb8)

Cropped Image:
 
![image](https://github.com/user-attachments/assets/d3b8524f-6c1e-4d9b-9af3-bbfb777c6fed)
 
![image](https://github.com/user-attachments/assets/04e17bcd-7235-4287-ab08-597c88b6351d)

![image](https://github.com/user-attachments/assets/2af1177a-51b3-4316-ad2e-568d128882d0)


# Resize the image:

1.	Function Name:
              resize_image()
2.	Approach:
              This function resizes the image based on user-provided width and height values. It first validates the input and then uses `img.resize()` to resize the image. The resized image is displayed using the `Image.show()` method.
3.	Demo Working and Screenshots

Resizing the previously cropped image:
 
![image](https://github.com/user-attachments/assets/d8b5061d-f0a5-44b4-bc36-851532c84489)

![image](https://github.com/user-attachments/assets/1afc0f95-2e6b-418e-8831-8d99145a681e)

# Flipping the image horizontally

1.	Function Name:
               flip_horizontal()
2.	Approach:
The function flips the image horizontally using the `transpose()` method with `Image.FLIP_LEFT_RIGHT`. The flipped image is displayed afterward.
3.	Demo Working and Screenshots

Original Image:
![image](https://github.com/user-attachments/assets/2877d84b-d258-4a2c-a26e-d71796a46f72)


Horizontally Flipped Image:

![image](https://github.com/user-attachments/assets/a5e22b1f-32bf-4750-b8cc-7c36932940bb)
 
![image](https://github.com/user-attachments/assets/6aa7592e-4558-48d1-9180-79e2fe5f3018)

 

# Flipping the Image Vertically:


1.	Function Name:
               flip_vertical()
2.	Approach:
              This function flips the image vertically by calling `transpose()` with `Image.FLIP_TOP_BOTTOM`. The result is displayed using the Pillow library's `show()` method.
3.	Demo Working and Screenshots
Loaded image:
 
![image](https://github.com/user-attachments/assets/45e1bc27-c179-4d63-84d9-ed2063576578)
Flipping the image vertically.


![image](https://github.com/user-attachments/assets/46854a4a-6223-435c-857e-71da6c8c1a5f)

![image](https://github.com/user-attachments/assets/5d9c9ca8-7b76-4e86-a4c9-eb9c4bb23eb5)
 

# Images combined side-by-side

1.	Function Name: 
               combine_side_by_side()
2.	Approach:
              This function loads a second image and resizes it to match the height of the first image. The two images are then combined side-by-side by creating a new blank image with sufficient width using `Image.new()` and pasting both images onto the canvas using `paste()`. The combined image is then displayed.
3.	Demo Working and Screenshots
![image](https://github.com/user-attachments/assets/0a76370c-208f-495e-a082-d1e326ab5c80)

 
Combined 2 images side by side
 
![image](https://github.com/user-attachments/assets/09328fb9-f22d-4e81-8f79-ec77c07277d0)

# Overlay images

1.	Function Name:
              overlay_images()
2.	Approach:
              This function overlays two images by blending them using `Image.blend()`. The second image is resized to match the dimensions of the first image, and a blend factor (0.4) is applied to adjust the transparency of the second image over the first. The overlay is then displayed.
3.	Demo Working and Screenshots
![image](https://github.com/user-attachments/assets/733a7569-ffdc-4d60-8316-9ef9ce553c26)

 
Overlayed 2 images 
![image](https://github.com/user-attachments/assets/e527affd-dd6a-44c2-83f0-1bbb2e9adba5)

# Challenges faced:
Following are a few challenges I faced during the implementation of this GUI based Image Manipulation Application:
•	Getting familiar with new libraries like `PIL`, `tkinter`, and `TkinterDnD`.
•	Handling different image formats (JPG, PNG, BMP, etc.) and ensuring compatibility withrespect to sizing for overlaying images, etc.
•	 Implementing precise coordinate-based operations for cropping and resizing.



