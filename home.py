import streamlit as st
st.title ("Mon formulaire")

#texte
st.write ("Ceci est un formulaire de contact")

#Champ de saisi
user_input = st.text_input ("Tapez votre texte :")

st.write (user_input)

#Image
st.image ("https://www.livreshebdo.fr/sites/default/files/styles/article_principal/public/2022-06/Berserk.png?itok=hw6ZYicJ")

#sidebarre
st.sidebar.title (Majorel Henry-Christian)
