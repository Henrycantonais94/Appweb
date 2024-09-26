import streamlit as st
st.title ("Mon formulaire")

#texte
st.write ("Ceci est un formulaire de contact")

#Champ de saisi
user_input = st.text_input ("Tapez votre texte :")

st.write (user_input)

#Image
st.image ("https://www.livreshebdo.fr/sites/default/files/styles/article_principal/public/2022-06/Berserk.png?itok=hw6ZYicJ")

#sidebar
st.sidebar.title ("Majorel Henry-Christian")

#Vidéo dans la sidebar
st.sidebar.video ("https://youtu.be/s6saVUobqGM?si=D2paJJM5xFIMrst_")

#Select bare
student_grade = st.selectbox("Selectionnez votre niveau d'étude, ["Bac", "Bac +2", "Bac +5"])

#Select slider
age = st.select_slider("Quel est votre age ?", range(0; 99))
