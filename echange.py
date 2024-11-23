import streamlit as st
import pandas as pd

st.header("Interface d'échange monnaie")

#list_monnaie = st.selectbox("Votre monnaie : ", ["Franc CFA", "Dollar américain", "Euro", "Livre Sterling"])
#choix_1 = st.multiselect('Selection', ["Franc CFA", "Dollar américain", "Euro", "Livre Sterling"])
#choix_2 = st.multiselect('Converti en ', ["Franc CFA", "Dollar américain", "Euro", "Livre Sterling"])


monnaie1 = st.text_input("Monnaie")
monnaie2 = st.text_input("Echange")

if monnaie1 == 'Franc CFA' and monnaie2 == 'Euro' :
    st.write("Un euro équivaut à 655 FCFA")
else :
    st.write("Inconnue")