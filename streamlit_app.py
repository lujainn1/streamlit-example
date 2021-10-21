from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from PIL import Image

st.title('Fntech')

st.header('Style')
uploaded_imgg = st.file_uploader(type=["png","jpg","jpeg"])
#if uploaded_img is not None:
st.header('Content')
uploaded_img = st.file_uploader("Content", type=["png","jpg","jpeg"], key = "<uniquevalueofsomesort>")
#if uploaded_img is not None:


#Input (uploaded_img , uploaded_imgg)
#AI 
#Output (image)

image = Image.open(uploaded_imgg)
st.image(image, caption='AIOutput')
