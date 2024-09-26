import streamlit as st

st.title ("Dall-e3")

#champ de saisi
user_input : st.text_input ("Open IA")
st.write(user_input)
recherche_input : ("Votre texte")
st.write(recherche_input)

#clé
from openai import OpenAI
st.sidebar
client = OpenAI(api_key=OpenAIKEY)
prompt = "A cute baby sea otter"
image = client.images.generate(
    model="dall-e-2",
    prompt=user_input,
    size="512x512",
    quality="standard",
    n=1,
)
image_url = image.data[0].url
print(image_url)
