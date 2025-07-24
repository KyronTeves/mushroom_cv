# Mushroom Detection with YOLO and Raspberry Pi

This project enables real-time detection and classification of mushrooms using a Raspberry Pi camera and a YOLO deep learning model. The main script (`cam.py`) captures images from the Pi camera, runs inference using a trained YOLO model, and displays the results with bounding boxes and class labels.

## Key Files and Directories

- `cam.py`: Main script for live mushroom detection and visualization.
- `models/best.pt`: Trained YOLO model weights for mushroom detection.
- `mushroom.txt`: List of class labels corresponding to detected mushrooms.
- `requirements.txt`: Python dependencies for running the project.
- `dataset_images/`: Directory for storing images used for training or testing.
- `yolov8_object_detection_on_custom_dataset.ipynb`: Jupyter notebook for model training and experimentation.

## Getting Started

This repository is in early development. For setup, see `requirements.txt` and run the main script on a Raspberry Pi with a connected camera. Further instructions and documentation will be added as the project evolves.
