import streamlit as st
import pandas as pd
from PIL import Image
from src import model

st.set_page_config(
    page_title="Sentiment Analysis",
    # page_icon="FB",
    # layout="wide",
    initial_sidebar_state="expanded",
)

# Add title, descriptions and image
st.title('Sentiment Analysis')
st.markdown('''
- The data is obtained from [Kaggle](https://www.kaggle.com/austinreese/craigslist-carstrucks-data),
and they were scraped from the Craigslist platform, which has a very large collection of listings of 
used vehicles that are being sold by people in United States.
- In this web app, machine learning is used to predict used car prices based on various
attributes such as the year of the vehicle, the location (latitude and longitude) of the listing and so on.


- App built by [Anson](https://www.linkedin.com/in/ansonnn07/)
- Built with `Python`, using `streamlit`, `sklearn`, `pandas`, `numpy`

**Links**: [GitHub](https://github.com/ansonnn07/Used-Car-Price-Prediction), 
[LinkedIn](https://www.linkedin.com/in/ansonnn07/),
[Kaggle](https://www.kaggle.com/ansonnn/code)
''')

st.markdown('---')

st.image(Image.open('bmw-x4.jpg'))
