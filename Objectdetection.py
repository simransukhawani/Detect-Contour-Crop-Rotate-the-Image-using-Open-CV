# %%
import cv2
import numpy as np
import os

# Input and output folder paths
input_folder = "Path to your input folder"
output_folder = "Path of your output folder"

# Function to process images in a folder
def process_images(input_folder, output_folder):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    # Initialize counter for numbering cropped images
    image_counter = 1
    angle_step = 10
    
    # Process each image in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            # Read the image
            input_image = cv2.imread(os.path.join(input_folder, filename), cv2.IMREAD_UNCHANGED)

            # Convert the image to grayscale
            gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

            # Apply Canny edge detection
            canny = cv2.Canny(gray_image, 50, 180)

            # Perform morphological operations to enhance the edges
            kernel = np.ones((5,5), np.uint8)
            dilated_image = cv2.dilate(canny, kernel, iterations=1)

            # Find contours
            contours, _ = cv2.findContours(dilated_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # Find the largest contour
            largest_contour = max(contours, key=cv2.contourArea)

            # Get the bounding box of the largest contour
            x, y, w, h = cv2.boundingRect(largest_contour)

            # Crop ROI from the given image
            output_image = input_image[y:y+h, x:x+w]
            # Resize cropped image to 500x500
            output_image = cv2.resize(output_image, (500, 500))

            # Save cropped image with sequential numbering
            output_path = os.path.join(output_folder, f"cropped_{image_counter}.png")
            cv2.imwrite(output_path, output_image)

            # Increment image counter
            image_counter += 1

            # Get the center of the image
            height, width = output_image.shape[:2]
            center = (width / 2, height / 2)
            scale = 0.8

            # Rotate the cropped image by steps of 'angle_step' degrees
            for angle in range(10, 370, angle_step):
                # Calculate the rotation matrix
                rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

                # Apply the rotation to the image
                rotated_image = cv2.warpAffine(output_image, rotation_matrix, (width, height))

                # Save rotated image
                rotated_output_path = os.path.join(output_folder, f"cropped_{image_counter-1}_rotated_{angle}.png")
                cv2.imwrite(rotated_output_path, rotated_image)

# Process images in the input folder and save output images in the output folder
process_images(input_folder, output_folder)



