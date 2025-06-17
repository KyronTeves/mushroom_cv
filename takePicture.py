from picamera2 import Picamera2
from datetime import datetime
import os
import time
import cv2
import subprocess  

# Set folder to save images
save_folder = "/home/kyron/Documents/dataset_images"
os.makedirs(save_folder, exist_ok=True)

# Initialize camera
picam2 = Picamera2()
camera_config = picam2.create_still_configuration()
picam2.configure(camera_config)
picam2.start()

# Enable autofocus <-- may be useless
picam2.set_controls({"AfMode": 2})  # Auto focus mode
time.sleep(0.5)  # Let the camera adjust first
picam2.set_controls({"AfTrigger": 0})  # Start autofocus scan
time.sleep(1)  # Wait for focus to adjust

# OpenCV Preview window
while True:
    frame = picam2.capture_array()  # Get current frame
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Fix color issue
    cv2.imshow("Camera Preview", frame)  # Show live feed
    if cv2.waitKey(1) == ord('q'):  # Press 'q' to exit preview
        break

cv2.destroyAllWindows()  # Close preview window

# # Countdown before capturing
# countdown_time = 3
# for i in range(countdown_time, 0, -1):
#     print(f"Capturing in {i}...")
#     time.sleep(1)

# Capture the image
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"dataset_{timestamp}.jpg"
file_path = os.path.join(save_folder, filename)
picam2.capture_file(file_path)

# Stop camera
picam2.stop()

# Open the saved image in the default image viewer
subprocess.run(["xdg-open", file_path])

print(f"Image saved and opened: {file_path}")