from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os
model=load_model('animal_classifier.h5')
def classifier(url):
    img_path=url
    img=load_img(img_path,target_size=(224,224))
    img_array=img_to_array(img)
    img_array=np.expand_dims(img_array,axis=0)
    img_array /=255.0
    predictions=model.predict(img_array)
    max_idx=np.argmax(predictions)
    finames=os.listdir('dataset/animals')
    return finames[max_idx]
