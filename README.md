#Object Detection using OpenCV
This project showcases the implementation of object detection using OpenCV, a powerful computer vision library in Python. The main objective is to detect and extract objects from images, specifically targeting Arduino boards.

Features
Image Processing: Utilizes various techniques such as edge detection, contour finding, and morphological operations to enhance object boundaries.
Object Cropping: Identifies the largest contour in each image and extracts the object of interest.
Image Rotation: Provides rotational variations for each cropped object, enhancing dataset diversity.
Efficient Processing: Processes images in a specified input folder and saves the results in an output folder.
Usage
Input Images: Place the images to be processed in the specified input folder (input_folder).
Run Script: Execute the provided Python script to process the images and save the results in the output folder (output_folder).
Output: Processed images will be saved in the output folder with sequential numbering and rotation variations.
