from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from PIL import Image

st.title('Fntech')

def load_img(uploaded_img):
   image = Image.open(uploaded_img)
   return img

uploaded_img = st.file_uploader("Choose a file", type=["png","jpg","jpeg"])
if uploaded_img is not None:
   st.image(load_img, caption='AIOutput')


#Input (uploaded_img , 2- uploaded_imgg)
#AI 
#Output (image)
