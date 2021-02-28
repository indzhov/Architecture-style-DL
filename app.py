from flask import Flask, render_template, request
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
# from tensorflow.keras.applications.inception_v3 import preprocess_input
from tensorflow.keras.applications.resnet50 import preprocess_input
import cv2
import h5py
import os
from werkzeug.utils import secure_filename
import wikipedia


app = Flask(__name__)


MODEL_PATH ='resnet.hdf5'

# Load your trained model
model = load_model(MODEL_PATH)

# Function to load and prepare the image in right shape
def read_image(filename):

    size = 224
    imgSize = (size, size)
    img = cv2.imread(filename)
    img = cv2.resize(img, imgSize)
    img = preprocess_input(img)
    img = np.array(img)
    img = np.expand_dims(img,axis=0)
    return img

@app.route("/", methods=['GET', 'POST'])
def home():

    return render_template('home.html')

@app.route("/predict", methods = ['GET','POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(filename)

        img = read_image(filename)
        preds = model.predict(img)
        preds=np.argmax(preds, axis=1)
        if preds==0:
            style="Achaemenid architecture"
            image="static/images/Achaemenid_architecture.png"
            page=wikipedia.page(style).content
        elif preds==1:
            style="American craftsman style"
            image="static/images/American_craftsman_style.jpg"
            page=wikipedia.page(style).content
        elif preds==2:
            style="American Foursquare architecture"
            image="static/images/American_Foursquare_architecture.jpg"
            page=wikipedia.page(style).content
        elif preds==3:
            style="Ancient Egyptian architecture"
            image="static/images/Ancient_Egyptian_architecture.jpg"
            page=wikipedia.page(style).content
        elif preds==4:
            style="Art Deco architecture"
            image="static/images/Art_Deco_architecture.jpg"
            page=wikipedia.page(style).content
        elif preds==5:
            style="Art Nouveau architecture"
            image="static/images/Art_Nouveau_architecture.jpg"
            page=wikipedia.page(style).content
        elif preds==6:
            style="Baroque architecture"
            image="static/images/Baroque_architecture.jpg"
            page=wikipedia.page(style).content
        elif preds==7:
            style="Bauhaus architecture"
            image="static/images/Bauhaus_architecture.jpeg"
            page=wikipedia.page(style).content
        elif preds==8:
            style="Beaux-Arts architecture"
            image="static/images/Beaux-Arts_architecture.jpg"
            page=wikipedia.page(style).content
        elif preds==9:
            style="Byzantine architecture"
            image="static/images/Byzantine_architecture.jpg"
            page=wikipedia.page(style).content
        elif preds==10:
            style="Chicago school architecture"
            image="static/images/Chicago_school_architecture.jpg"
            page=wikipedia.page(style).content
        elif preds==11:
            style="Colonial architecture"
            image="static/images/Colonial_architecture.jpg"
            page=wikipedia.page(style).content
        elif preds==12:
            style="Deconstructivism"
            image="static/images/Deconstructivism.jpg"
            page=wikipedia.page(style).content
        elif preds==13:
            style="Edwardian architecture"
            image="static/images/Edwardian_architecture.jpg"
            page=wikipedia.page(style).content
        elif preds==14:
            style="Georgian architecture"
            image="static/images/Georgian_architecture.jpg"
            page=wikipedia.page(style).content
        elif preds==15:
            style="Gothic architecture"
            image="static/images/Georgian_architecture.jpg"
            page=wikipedia.page(style).content
        elif preds==16:
            style="Greek Revival architecture"
            image="static/images/Greek_Revival_architecture.jpg"
            page=wikipedia.page(style).content
        elif preds==17:
            style="International style"
            image="static/images/International_style.jpg"
            page=wikipedia.page(style).content
        elif preds==18:
            style="Novelty architecture"
            image="static/images/Novelty_architecture.jpeg"
            page=wikipedia.page(style).content
        elif preds==19:
            style="Palladian architecture"
            image="static/images/Palladian_architecture.jpg"
            page=wikipedia.page(style).content
        elif preds==20:
            style="Postmodern architecture"
            image="static/images/Postmodern_architecture.jpg"
            page=wikipedia.page(style).content
        elif preds==21:
            style="Queen Anne architecture"
            image="static/images/Queen_Anne_architecture.jpg"
            page=wikipedia.page(style).content
        elif preds==22:
            style="Romanesque architecture"
            image="static/images/Romanesque_architecture.jpg"
            page=wikipedia.page(style).content
        elif preds==23:
            style="Russian Revival architecture"
            image="static/images/Russian_Revival_architecture.jpg"
            page=wikipedia.page(style).content
        elif preds==24:
            style="Tudor Revival architecture"
            image="static/images/Tudor_Revival_architecture.JPG"
            page=wikipedia.page(style).content
        return render_template('predict.html', product = style, image = image, page=page)

    return render_template('predict.html')

if __name__ == "__main__":
    init()
    app.run()