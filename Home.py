from src import *
from PIL import Image
from streamlit.components.v1 import html
import base64

text_html  ="<h1 style='text-align: center;'>Animal Crossing New Horizons Dashboard</h1>"
st.markdown(text_html, unsafe_allow_html=True)

image_url = "https://media.tenor.com/PeegDtyzXS0AAAAC/animal-crossing-animal-crossing-new-horizons.gif"

image_html = f'''
<p align="center">
  <img width="600" height="370" style="border-radius:2%;box-shadow: rgba(149, 157, 165, 0.3) 0px 8px 24px" src="{image_url}">
</p>
'''
st.markdown(image_html, unsafe_allow_html=True)
