# Malaria Detection Application

This application is designed to facilitate the detection of malaria from blood smear images using a deep learning-based image classification model. It provides an intuitive interface to upload images and receive predictions, making it accessible for medical practitioners and researchers.

## Features

### Automated Malaria Detection
- Utilizes a pre-trained Convolutional Neural Network (CNN) for classifying blood smear images.
- Outputs the prediction as "Saine" (Uninfected) or "Parasitée" (Parasitized) with high accuracy.

### User-Friendly Web Interface
- Built with Flask, providing a seamless image upload feature.
- Displays classification results directly on the interface.

### Preprocessing
- Automatically resizes uploaded images to the model's input size (130x130 pixels).
- Normalizes pixel values for improved prediction accuracy.

## How to Use

### Locally

1. **Clone the repository:**
    ```bash
    git clone https://github.com/simbouch/malaria_detection
    cd malaria_detection
    ```

2. **Set up the virtual environment and install dependencies:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. **Run the application:**
    ```bash
    python main.py
    ```

4. **Access the application in your browser at `http://127.0.0.1:5000`.**

### Using the Application
1. Navigate to the upload page.
2. Upload an image file of a blood smear (JPEG, PNG formats supported).
3. Submit the image and wait for the classification result to be displayed.

## Directory Structure

- **app/**: Contains the core Flask application files.
  - **routes.py**: Handles routing and rendering of templates.
  - **utils.py**: Preprocessing functions for image handling.
  - **models.py**: Placeholder for future database integration.
- **templates/**: HTML templates for the web interface.
- **static/**: Static files like CSS for styling.
- **models/**: Directory containing the trained CNN model (`cnn_model.h5`).
- **notebooks/**: Includes Jupyter notebooks for model training and testing.
- **requirements.txt**: Lists all dependencies for the application.

## Technologies Used
- **Flask**: Backend web framework for handling requests and rendering results.
- **TensorFlow**: Used for building and loading the CNN model.
- **HTML/CSS**: For the web interface design.

## Use Cases
- **Healthcare**: Assists medical practitioners in malaria diagnosis.
- **Research**: Facilitates experimentation in image-based medical diagnostics.
- **Education**: Demonstrates the application of machine learning in healthcare.
