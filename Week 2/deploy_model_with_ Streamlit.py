import numpy as np
import streamlit as st
from PIL import Image
from keras.models import load_model
from keras.preprocessing import image
import time


model = load_model('MobileNetV2_best.keras')
class_names = ['CaS', 'CoS', 'Gum', 'MC', 'OC', 'OLP', 'OT']

def read_image(uploaded_file):
    img = Image.open(uploaded_file)
    img = img.resize((96, 96))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img /= 255.0
    return img


# Streamlit app function
def streamlit_App():
    st.set_page_config(page_title="Teeth Classification", page_icon="🦷", layout="centered")

    # Styles
    st.markdown("""
            <div class="header">
                <h2>Teeth Classification ML Prediction</h2>
            </div>
            <style>
                .header {
                    background-color: #4CAF50;
                    padding: 10px;
                    text-align: center;
                }
                .stButton > button {
                    background-color: #4CAF50;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    padding: 10px 20px;
                    font-size: 16px;
                    cursor: pointer;
                }
                .stButton > button:hover {
                    background-color: #36763A;
                }
                .stExpander {
                    border-radius: 5px;
                    border: 1px solid #4CAF50;
                }
            </style>
        """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display uploaded image
        st.image(uploaded_file, use_column_width=True)

        st.write("Image Uploaded Successfully ✅", unsafe_allow_html=True)
        st.write("Press 'Predict' To Classify The Disease ! 🚀")

        # Prediction button
        if st.button("Predict"):
            with st.spinner('Classifying...'):
                time.sleep(1)  # Adding delay..
                img = read_image(uploaded_file)
                pred = model.predict(img)
                pred_index = np.argmax(pred, axis=1)[0]
                pred_class = class_names[pred_index]
                st.success(f'**Disease Prediction:** {pred_class}')
                st.success(f'**Confidence Score:** {np.max(pred):.2f}')

    else:
        st.info("Please Upload An Image..")

    # Checkbox model summary
    if st.checkbox("Show Model Summary"):
        st.write(f"**Model Name:** Mobile Net V2")
        model_summary = []
        model.summary(print_fn=lambda x: model_summary.append(x))
        st.text("\n".join(model_summary))

    # Expander information about the classes
    with st.expander("About The Classes"):
        st.write("""
        - **CaS:** Candidiasis
        - **CoS:** Caries
        - **Gum:** Gingivitis
        - **MC:** Mucosal Changes
        - **OC:** Oral Cancer
        - **OLP:** Oral Lichen Planus
        - **OT:** Other Teeth Conditions
        """)

# Run the app
streamlit_App()
