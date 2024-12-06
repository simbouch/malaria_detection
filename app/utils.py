import numpy as np
import tensorflow as tf
from PIL import Image

# Load the saved model
MODEL_PATH = 'models/cnn_model.h5'
model = tf.keras.models.load_model(MODEL_PATH)

def preprocess_image(file):
    """
    Preprocess an uploaded image file for prediction.
    - Resize to (130, 130)
    - Normalize pixel values to [0, 1]
    """
    image = Image.open(file).convert('RGB')  # Ensure the image has 3 channels
    image = image.resize((130, 130))  # Resize to the model's input size
    image = np.array(image) / 255.0  # Normalize pixel values
    return np.expand_dims(image, axis=0)  # Add batch dimension

def predict(file):
    """
    Preprocess the image and return prediction.
    """
    processed_image = preprocess_image(file)
    prediction = model.predict(processed_image)
    return "Parasitée" if prediction[0][0] < 0.5 else "Saine"
