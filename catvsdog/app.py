from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications import imagenet_utils
import os
import numpy as np
from tensorflow.keras.preprocessing import image # type: ignore
from tensorflow.keras.applications.vgg16 import preprocess_input # type: ignore

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necessary for session management

# Load your trained model
MODEL_PATH = 'model/cat-vs-dog.h5'
model = load_model(MODEL_PATH)

# Create the uploads directory if it does not exist
UPLOAD_FOLDER = 'static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Helper function to prepare image for model prediction
def prepare_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))  # Adjust target size as per your model
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    img_array = img_array / 255.0  # If your model was trained with normalized images
    return img_array

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            session['img_path'] = file_path  # Store the image path in the session
            return redirect(url_for('predict'))
    return render_template('index.html', img_path=None)

@app.route('/predict')
def predict():
    img_path = session.get('img_path')  # Retrieve the image path from the session
    if img_path:
        img_array = prepare_image(img_path)
        prediction = model.predict(img_array)
        predicted_class = np.argmax(prediction, axis=1)
        translate= {0:"cat", 1:"dog"}
        finale= translate[predicted_class[0]]
        print(finale)
        return render_template('prediction.html', result=finale, img_path=img_path)
    return redirect(url_for('index'))

@app.route('/uploads/<filename>')
def send_uploaded_file(filename=""):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
