Contour Crop & Rotate is a project designed to automate the process of detecting contours, cropping images around the largest contour, and rotating the cropped region in 10-degree increments. This project is useful for augmenting datasets and enhancing data for machine learning applications.

**Main Features**
**Contour Detection:** Identifies contours using Canny edge detection and selects the largest one.
**Region Cropping:** Crops the image around the largest contour.
**Image Rotation:** Rotates the cropped region in 10-degree steps, creating multiple versions.
**Background Color Change:** Allows you to set a specific background color for rotated images to avoid unwanted black borders.

**Requirements**
Ensure Python is installed along with the following packages:
>> pip install opencv-python numpy

**Usage Guide**
* Set input_folder to the directory with your source images.
* Set output_folder to the directory where the processed images will be saved.
* Run the script to create cropped and rotated images.

**Customization Options**
Rotation Step Size: Change the step size for image rotation by adjusting angle_step.
Background Color: Set a different background color by modifying background_color.

**Contributions**
Contributions are welcome! If you have suggestions for improvements or want to add new features, please submit a pull request.
