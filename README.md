# Face Detection with Screenshot Capture

This project implements a real-time face detection system using OpenCV and MediaPipe, with the added functionality of capturing screenshots at regular intervals.

## Features

- Real-time face detection using a webcam
- Bounding box display around detected faces
- Confidence score display for each detection
- Automatic screenshot capture every 5 seconds

## Screenshot

![Face Detection Demo](path/to/your/screenshot.png)

*Caption: Face detection in action, showing bounding boxes and confidence scores.*

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- MediaPipe
- NumPy

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/face-detection-project.git
   cd face-detection-project
   ```

2. Install the required packages:
   ```
   pip install opencv-python mediapipe numpy
   ```

## Usage

Run the script using Python:

```
python face_detection.py
```

- The program will access your webcam and start detecting faces in real-time.
- Detected faces will be outlined with a purple bounding box, along with a confidence score.
- Screenshots will be saved every 5 seconds in the `screenshots` directory.
- Press 'q' to quit the program.

## Code Overview

The main script performs the following actions:

1. Sets up a directory for storing screenshots
2. Initializes the webcam capture
3. Enters a loop to continuously process frames:
   - Detects faces in each frame
   - Draws bounding boxes and confidence scores for detected faces
   - Captures and saves a screenshot every 5 seconds
   - Displays the processed frame
4. Cleans up resources when the user exits the program

## Customization

- To change the screenshot interval, modify the `screenshot_interval` variable (currently set to 5 seconds).
- The `screenshots` directory is created in the same location as the script. You can change this by modifying the `screenshot_dir` variable.

## License

[Include your chosen license here]

## Contributing

[Include guidelines for contributing to your project]

## Contact

[Your Name] - [your.email@example.com]

Project Link: [https://github.com/yourusername/face-detection-project](https://github.com/yourusername/face-detection-project)
