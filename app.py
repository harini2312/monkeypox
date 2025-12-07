import numpy as np
import streamlit as st
from PIL import Image
import keras.preprocessing.image as image
from tensorflow.keras import models
from PIL import Image

# Define utility functions
def load_saved_model(model_path):
    saved_model = models.load_model(model_path, custom_objects={"accuracy": "accuracy"})
    return saved_model

def preprocess_uploaded_image(image_file, desired_size=128):
    image_data = image_file.resize((desired_size, desired_size), resample=Image.LANCZOS)
    #image_data = np.array(image_data) / 255.0  # Normalize pixel values
    image_data = np.expand_dims(image_data, axis=0)  # Add batch dimension
    return image_data

def resize_image(image_file, desired_size=254):
    resized_image = image_file.resize((desired_size, desired_size))
    return resized_image

def generate_custom_footer():
    custom_footer_html = """
    <div style="background-color:#F8F9FA;padding:10px;border-radius:10px;">
    <p style="text-align:center;">Developed by: Your Name</p>
    </div>
    """
    return custom_footer_html

# Main Streamlit code
highlight_prediction_colors = ["red", "orange"]
disease_types = [
    'MonkeyPox',
   'Non Monkeypox'

]



def format_highlighted_prediction(disease_types, idx):
    formatted_disease_types = disease_types.copy()
    highlighted_prediction_html = f'''<span style="color:{highlight_prediction_colors[idx]}; font-size: larger">**{disease_types[idx]}**</span>'''
    formatted_disease_types[idx] = highlighted_prediction_html
    return '<br>'.join(formatted_disease_types)

if __name__ == '__main__':
    st.set_page_config(page_title="MonkeyPox Detection", page_icon="")
    st.markdown("<style>footer{visibility:hidden;}</style>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: black;'>"
                "<center>&emsp;&emsp;MonkeyPox Detection</center></h1>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload a Monkey Pox Skin image...", type=["jpg"])
    
    if uploaded_file is not None:
        img_in = Image.open(uploaded_file)
        resized_img_in = resize_image(img_in)  # Resize uploaded image
        img_in_processed = preprocess_uploaded_image(resized_img_in)  # Preprocess for prediction

        col1, col2 = st.columns(2)
        col1.image(resized_img_in)
        st.write("Uploaded Image")

        model = load_saved_model('Trained_Models/LastModel.h5')
        prediction = model.predict(img_in_processed)
        predicted_idx = np.argmax(prediction)
        col2.markdown("### Predicted Type")
        
        col2.markdown(format_highlighted_prediction(disease_types, predicted_idx), unsafe_allow_html=True)

    #st.markdown(generate_custom_footer(), unsafe_allow_html=True)
