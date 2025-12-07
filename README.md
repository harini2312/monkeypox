# Installation & How to Run the Project

Follow these steps to install and run the Monkeypox Detection Streamlit app.

1️)Install Python (if not already installed)

Use Python 3.10 or Python 3.11 (TensorFlow is not compatible with Python 3.12).

2️) Create and activate a virtual environment

    python -m venv tfenv2


Activate it:

Windows

    tfenv2\Scripts\activate

3️) Install required libraries

Inside the activated environment, run:

    pip install tensorflow keras streamlit pillow numpy matplotlib

4️) Run the Streamlit application

Navigate to your project folder:

    cd path/to/your/project


Then run:

    python -m streamlit run app.py

5️) Upload an image to get prediction

The browser will open automatically → upload any skin lesion image → model will predict:

Monkeypox, or

Non-Monkeypox
