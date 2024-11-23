import streamlit as st

st.title(":blue[CURRENCY]")

st.markdown('''
### Monnaie

Il glissa son bras autour d’elle. Délicieusement
 torturée, elle en suivit les gestes lents. Elle attendait – elle
 ne savait trop quoi – haletante, les lèvres sèches et
 brûlantes, le cœur bondissant, une fièvre dans les veines.
 Doucement, d’un mouvement infiniment caressant, le
 bras remonta et l’attira vers lui. Elle n’attendit plus. Avec
 un grand soupir las, elle laissa tomber sa tête sur la
 poitrine de Martin ; il se pencha, tendant vers elle ses
 lèvres, et celles de Ruth firent la moitié du chemin 
 
 ### Type de monnaie
 
  Lorsque l’IMF a mesuré ses écarts et calculé l’impact 
sur la rentabilité d’une certaine évolution des taux 
d’intérêt, elle peut comparer cet impact avec ses 
prévisions de rentabilité pour décider de l’arbitrage 
risque-gain à opérer. Cela peut être exprimé en 
pourcentage du bénéfice ou pourcentage des produits, 
ou encore en mois de bénéfice ou de produits.
 
 
  
 ''')

colonne_1, colonne_2, colonne_3 = st.columns([1,2,3])
with colonne_1 :
    st.image("dollar.png")
with colonne_2 :
    st.image("livre.png", width = 70)
with colonne_3 :
    st.image("euro.png", width = 100)
