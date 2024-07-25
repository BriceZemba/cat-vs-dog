# Cat or Dog Classification Application

## Overview

This is a web-based application that classifies uploaded images as either a cat or a dog using a pre-trained deep learning model.

## Features

- Upload an image for classification.
- Preview the uploaded image.
- Display the predicted class of the image (Cat or Dog).
- Uses a pre-trained deep learning model for prediction.

## Technologies Used

- Flask (Python web framework)
- TensorFlow/Keras (Deep learning framework)
- Bootstrap (CSS framework for styling)
- HTML/CSS/JavaScript

## Setup and Installation

### Prerequisites

- Python 3.7+
- Pip (Python package installer)
- Virtualenv (optional but recommended)

### Installation Steps

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/cat-or-dog-classification.git
    cd cat-or-dog-classification
    ```

2. **Create a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Ensure the `uploads` directory exists:**

    ```bash
    mkdir -p static/uploads
    ```

5. **Download the pre-trained model and place it in the `model` directory:**

    - Ensure the model file is named `mobile.h5` and located in the `model` directory.

### Running the Application

1. **Start the Flask application:**

    ```bash
    python app.py
    ```

2. **Open your web browser and go to:**

    ```
    http://127.0.0.1:5000
    ```

## Project Structure

```
cat-or-dog-classification/
│
├── app.py                    # Main Flask application
├── requirements.txt          # List of Python packages
├── templates/
│   ├── index.html            # Upload page template
│   └── prediction.html       # Prediction result page template
├── static/
│   ├── css/
│   │   └── styles.css        # Custom CSS styles
│   └── uploads/              # Directory for uploaded images
├── model/
│   └── mobile.h5             # Pre-trained model file
└── README.md                 # Project README file
```

## Usage

1. **Upload an Image:**
    - Navigate to the home page.
    - Click on the "Choose File" button to upload an image.
    - The uploaded image will be previewed on the page.

2. **Classify the Image:**
    - Click on the "Submit" button to classify the uploaded image.
    - The prediction result (Cat or Dog) will be displayed on a new page.

## Contributing

1. **Fork the repository**
2. **Create a new branch:**

    ```bash
    git checkout -b feature/your-feature-name
    ```

3. **Commit your changes:**

    ```bash
    git commit -m 'Add some feature'
    ```

4. **Push to the branch:**

    ```bash
    git push origin feature/your-feature-name
    ```

5. **Create a pull request**
