import os
import csv
import cv2

# Define the root directory
root_dir = 'Frames'
question = "Describe the image concisely. Include the bounding box for each mentioned object."

# Open the CSV file in write mode
with open('dataset_urls.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(["url", "cls", "video", "frame", "question", "answer"])

    # Traverse through the root directory
    for class_dir in os.listdir(root_dir):
        class_path = os.path.join(root_dir, class_dir)
        if os.path.isdir(class_path):
            # Traverse through each class directory
            for video_dir in os.listdir(class_path):
                video_path = os.path.join(class_path, video_dir)
                if os.path.isdir(video_path):
                    # Traverse through each video directory
                    for video_file in os.listdir(video_path):
                        video_file_path = os.path.join(video_path, video_file)
                        if os.path.isfile(video_file_path) and video_file.endswith('.mp4'):  # assuming videos are mp4
                            # Read the video file
                            vidcap = cv2.VideoCapture(video_file_path)
                            success, image = vidcap.read()
                            count = 0
                            while success:
                                # Save each frame to the video directory
                                frame_file = f"frame{count}.jpg"
                                frame_path = os.path.join(video_path, frame_file)
                                cv2.imwrite(frame_path, image)
                                success, image = vidcap.read()
                                count += 1
                                # Write the frame URL, class, and video name to the CSV file
                                writer.writerow([frame_path, class_dir, video_dir, frame_file, question, ''])
