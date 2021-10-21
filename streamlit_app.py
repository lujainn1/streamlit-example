from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from PIL import Image

st.title('Fntech')



uploaded_img = st.file_uploader("Choose a file", type=["png","jpg","jpeg"], key="1")

uploaded_imgg = st.file_uploaderr("Choose a file", type=["png","jpg","jpeg"], key="2")
if uploaded_imgg is not None:








   image = Image.open(uploaded_img)
   st.image(image, caption='AIOutput')
