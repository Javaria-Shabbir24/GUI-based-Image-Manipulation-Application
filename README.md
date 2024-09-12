﻿# GUI-based-Image-Manipulation-Application
 
Load an Image
1.	Function Name:
              Load_Image()
2.	Approach:
This function allows users to browse and load an image using `filedialog.askopenfilename()`. Once a file path is selected, the `Image.open()` function from the PIL (Pillow) library is used to open the image. The loaded image is stored in the global variable `img` and displayed using `img.show()`.
3.	Demo Working and Screenshots

By clicking the Browse button, the user is allowed to navigate and select desired image.
 

The selected image is then displayed in a separate window.
 

Save the image 
1.	Function Name:
save_image()
2.	Approach:
This function saves the currently loaded image in a user-specified format. It first checks if an image is loaded and if a format is selected via the `format_var`. Using `filedialog.asksaveasfilename()`, a save location and format are chosen. The image is then saved using the `img.save()` method, handling any exceptions to ensure error feedback is provided to the user.
3.	Demo Working and Screenshots

Loaded picture is this:
 
Selected format is tiff:
 









Chosen Location is desktop:
 

Image saved successfully as My Image.tiff on desktop
 

 

Image info:

1.	Function Name:
               show_image_info()
2.	Approach:
               This function extracts and displays details such as image width, height, format, and file size. The original file size is computed using the byte size of the image, and the compressed size is calculated by saving the image to a temporary in-memory file. The compression ratio is computed and displayed using a messagebox.
3.	Demo Working and Screenshots

After loading the image, the Image Info button is clicked that displays the desired results in a messagebox.
 

Grayscale image to black and white conversion:

1.	Function Name:
              convert_to_black_and_white()

2.	Approach:

This function converts a grayscale image to black and white by applying a threshold value. The `point()` method is used with a lambda function to map pixel values. Pixels above the threshold are set to 255 (white), and those below are set to 0 (black). The converted image is then displayed.
3.	Demo Working and Screenshots

Loaded Grayscale Image:

 

Black and White Image:

•	When threshold is set to 240
 
 

•	When threshold is set to  101:
 

 

Crop the image

1.	Function Name:
              crop_image()
2.	Approach:
              This function crops the loaded image using user-defined coordinates. The crop dimensions (left, top, right, bottom) are validated to ensure they're within image bounds. The `img.crop()` method is used to perform the cropping operation, and the cropped image is displayed along with the new dimensions
3.	Demo Working and Screenshots

Original Image 
 

Cropped Image:
 
 

 

Resize the image:

1.	Function Name:
              resize_image()
2.	Approach:
              This function resizes the image based on user-provided width and height values. It first validates the input and then uses `img.resize()` to resize the image. The resized image is displayed using the `Image.show()` method.
3.	Demo Working and Screenshots

Resizing the previously cropped image:
 
 

Flipping the image horizontally

1.	Function Name:
               flip_horizontal()
2.	Approach:
The function flips the image horizontally using the `transpose()` method with `Image.FLIP_LEFT_RIGHT`. The flipped image is displayed afterward.
3.	Demo Working and Screenshots

Original Image:
 

Horizontally Flipped Image:

 

 

Flipping the Image Vertically:

1.	Function Name:
               flip_vertical()
2.	Approach:
              This function flips the image vertically by calling `transpose()` with `Image.FLIP_TOP_BOTTOM`. The result is displayed using the Pillow library's `show()` method.
3.	Demo Working and Screenshots
Loaded image:
 


Flipping the image vertically.

 

 

Images combined side-by-side

1.	Function Name: 
               combine_side_by_side()
2.	Approach:
              This function loads a second image and resizes it to match the height of the first image. The two images are then combined side-by-side by creating a new blank image with sufficient width using `Image.new()` and pasting both images onto the canvas using `paste()`. The combined image is then displayed.
3.	Demo Working and Screenshots

 
Combined 2 images side by side
 

Overlay images

1.	Function Name:
              overlay_images()
2.	Approach:
              This function overlays two images by blending them using `Image.blend()`. The second image is resized to match the dimensions of the first image, and a blend factor (0.4) is applied to adjust the transparency of the second image over the first. The overlay is then displayed.
3.	Demo Working and Screenshots

 
Overlayed 2 images 
 
Challenges faced:
Following are a few challenges I faced during the implementation of this GUI based Image Manipulation Application:
•	Getting familiar with new libraries like `PIL`, `tkinter`, and `TkinterDnD`.
•	Handling different image formats (JPG, PNG, BMP, etc.) and ensuring compatibility withrespect to sizing for overlaying images, etc.
•	 Implementing precise coordinate-based operations for cropping and resizing.



