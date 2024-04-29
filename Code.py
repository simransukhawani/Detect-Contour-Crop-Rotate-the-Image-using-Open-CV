import cv2
import numpy as np
import os

# paths of input folder and output folder
input_folder = "Path to your Input Folder"
output_folder = "Path to your Input Folder"

# defined function to change the background color of the rotated images
def change_background_color(image, new_color):
    # Define the mask for black pixels
    mask = np.all(image == [0, 0, 0], axis=-1)

    # Change black pixels to the new color
    image[mask] = new_color

    return image

# Function to process images in a folder
def process_images(input_folder, output_folder):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    # Initialize counter for numbering cropped images
    image_counter = 1
    angle_step = 10
    
    # Define the desired background color (148, 153, 155)
    background_color = np.array([146, 150, 153], dtype=np.uint8)


    # Process each image in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            # Read the input image
            input_image = cv2.imread(os.path.join(input_folder, filename), cv2.IMREAD_UNCHANGED)

            # Resize the input image
            resized_image = cv2.resize(input_image, (800, 600))  # Resize to desired dimensions (800x600 in this case)

            # Convert the resized image to grayscale
            gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

            # Apply Canny edge detection method
            canny = cv2.Canny(gray_image, 50, 180)

            # Perform morphological operations to enhance the edges
            kernel = np.ones((5,5), np.uint8)
            dilated_image = cv2.dilate(canny, kernel, iterations=1)

            # Find contours
            contours, _ = cv2.findContours(dilated_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # Find the largest contour
            largest_contour = max(contours, key=cv2.contourArea)

            # Find out the bounding box of the largest contour
            x, y, w, h = cv2.boundingRect(largest_contour)
            
            # determine the size of the square to crop
            crop_size = min(resized_image.shape[0], resized_image.shape[1])

            # Calculate the center of the image
            center = (x + w // 2, y + h // 2)

            # Calculate the rotation boundaries
            max_dim = max(w+75, h+75)
            start_x = max(center[0] - max_dim // 2, 0)
            start_y = max(center[1] - max_dim // 2, 0)
            end_x = min(start_x + max_dim, resized_image.shape[1])
            end_y = min(start_y + max_dim, resized_image.shape[0])

            # Crop ROI from the resized image, ensuring coordinates are within bounds
            output_image = resized_image[start_y:end_y, start_x:end_x]

            # Save cropped image win sequential manner
            output_path = os.path.join(output_folder, f"cropped_{image_counter}.png")
            cv2.imwrite(output_path, output_image)

            # Increment image counter
            image_counter += 1

            # Get the center of the image
            height, width = output_image.shape[:2]
            center = (width / 2, height / 2)
            scale = 1

            # Rotate the cropped image by steps of 'angle_step' degrees
            for angle in range(10, 370, angle_step):
                # Calculate the rotation matrix
                rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
                
                # Rotate the image
                rotated_image = cv2.warpAffine(output_image, rotation_matrix, (width, height))
                
                # Change the background color of the rotated image
                rotated_image = change_background_color(rotated_image, background_color)

                # Save rotated image
                rotated_output_path = os.path.join(output_folder, f"cropped_{image_counter-1}_rotated_{angle}.png")
                cv2.imwrite(rotated_output_path, rotated_image)

# Process images in the input folder and save output images in the output folder
process_images(input_folder, output_folder)
