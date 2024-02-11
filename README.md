# Face Detection Model

This is a Streamlit app that utilizes OpenCV's Haar cascades for face and eye detection in images. Users can upload an image, and the app will detect faces and eyes in the image, displaying the processed image with bounding boxes around the detected faces and eyes.

## Features

- **Image Upload**: Users can upload an image file (supported formats: jpg, png).
- **Face Detection**: The app uses OpenCV's Haar cascades to detect faces in the uploaded image.
- **Eye Detection**: Additionally, the app detects eyes within the detected faces.
- **Visual Feedback**: The processed image is displayed with bounding boxes around the detected faces and eyes.
- **Information Display**: The app provides information on the number of faces detected in the image.

## Setup

1. Clone this repository to your local machine.
2. Install the required dependencies by running:
   ```
   pip install -r requirements.txt
   ```
3. Run the Streamlit app with the following command:
   ```
   streamlit run app.py
   ```

## Demo
[Live Demo](https://face-detection-model-jb.streamlit.app/)

## Usage

1. Once the app is running locally, visit the provided URL in your web browser.
2. Click on the "Choose a image" button and select an image file.
3. Wait for the app to process the image. Once processed, the uploaded image will be displayed with bounding boxes around the detected faces and eyes.
4. Information about the number of faces detected will be displayed below the processed image.

## Dependencies

- Python 3.x
- Streamlit
- OpenCV

