from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
   # To read file as bytes:
   bytes_data = uploaded_file.getvalue()  
   st.write(bytes_data)
   # To convert to a string based IO:
   stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
   st.write(stringio)

   # To read file as string:
   string_data = stringio.read()
   st.write(string_data)
   # Can be used wherever a "file-like" object is accepted:
   dataframe = pd.read_csv(uploaded_file)
   st.write(dataframe)
