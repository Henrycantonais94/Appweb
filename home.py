import streamlit as st
st.title ("Mon formulaire")

#texte
st.write ("Ceci est un formulaire de contact")

#Champ de saisi
user_input = st.text_input ("Tapez votre texte :")

st.write (user_input)

#Image
st.image ("https://www.manga-city.fr/wp-content/uploads/2023/03/berserk-10.jpg")
