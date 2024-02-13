# YOLOv3 Person Detection for Traffic Monitoring

This project utilizes the YOLOv3 algorithm for real-time person detection in video frames. The primary goal is to monitor traffic by detecting the presence of people in the frame and providing an alert if there are more than 45 people detected, indicating heavy traffic.

## Overview
The YOLOv3 (You Only Look Once) algorithm is a state-of-the-art deep learning model for object detection. In this project, we specifically use a pre-trained YOLOv3 model to detect persons in video frames. The model has been trained on a large dataset of annotated images and is capable of accurately detecting persons in various settings and poses.

## Usage
To use this project:
1. Install the required dependencies listed in `requirements.txt`.
2. Download the pre-trained YOLOv3 weights.
3. Run the detection script on your video feed.
4. Monitor the output for alerts indicating heavy traffic.

## Alert Mechanism
When the number of detected persons in a frame exceeds 45, the system triggers an alert. This alert can be customized to suit your specific requirements, such as sending an email notification or activating an alarm.

## Results

![drive link](https://drive.google.com/drive/u/0/folders/1ccoJ0Qtf5bnAqCKKhjPRBw2sg8FE6FZ_)

## References
- YOLOv3 Paper: [https://arxiv.org/abs/1804.02767](https://arxiv.org/abs/1804.02767)

Feel free to modify and enhance this README file according to your project's specific details and requirements.
