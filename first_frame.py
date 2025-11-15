import cv2
import os

# Create a folder for saving frames if it doesn't exist
output_folder = "frames"
os.makedirs(output_folder, exist_ok=True)

video_folder = "videos"
video_files=[f for f in os.listdir(video_folder) if f.endswith(".MOV")]

for video_file in video_files:
    video_path = os.path.join(video_folder, video_file)
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video file.")
        exit()
    print("Video opened successfully")
    success, frame = cap.read()
    if not success:
        print("Error: Could not read frame.")
        exit()
    
    output_name = video_file.replace(".MOV", "_first_frame.jpg")
    cv2.imwrite(os.path.join(output_folder, output_name), frame)

    cap.release()
    print(f"processed {video_file}")




