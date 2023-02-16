import streamlit as st
from PIL import Image

st.title('さぷーアプリ')
st.caption('これはさぷーの動画用のテストアプリです')

image = Image.open('./data/lucky.jpg')
st.image(image, width=200)
