from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from PIL import Image
#from__future__ import print_function

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

from PIL import Image
import matplotlib.pyplot as plt

import torchvision.transforms as transforms
import torchvision.models as models

import copy
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

imsize = 512 if torch.cuda.is_available() else 256  # use small size if no gpu

loader = transforms.Compose([
    transforms.Resize(imsize),  # scale imported image
    transforms.ToTensor()])  # transform it into a torch tensor

def image_loader(image_name):
    image = Image.open(image_name)
    # fake batch dimension required to fit network's input dimensions
    image = loader(image).unsqueeze(0)
    return image.to(device, torch.float)


st.title('Fntech')

st.subheader('Style')
uploaded_imgg = st.file_uploader("",type=["png","jpg","jpeg"])
#if uploaded_img is not None:
st.subheader('Content')
uploaded_img = st.file_uploader("", type=["png","jpg","jpeg"], key = "<uniquevalueofsomesort>")
#if uploaded_img is not None:


#Input (uploaded_img , uploaded_imgg)
#AI 
#Output (image)

image = Image.open(uploaded_imgg)
st.image(image, caption='AIOutput')
