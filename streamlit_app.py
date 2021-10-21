from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from PIL import Image

st.title('Fntech')



uploaded_img = st.file_uploader("Choose a file", type=["png","jpg","jpeg"])
if uploaded_img is not None:



#Input (uploaded_img , 2- uploaded_imgg)
#AI 
#Output (image)


   image = Image.open(uploaded_img)
   st.image(image, width=250, height=250)
