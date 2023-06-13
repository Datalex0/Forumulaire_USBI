import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from PIL import Image


#Configuration des dimensions & affichage de la page
st.set_page_config(page_title="Inscription USBI",
                   #page_icon=":soccer:",
                   page_icon="SRC/logo.jpg",
                   layout='wide')



# Affichage logo
image = Image.open("SRC/logo.jpg")
st.image(image, width=150)

# Affichage Titre
st.title("Formulaire d'inscription")

# Choix Catégorie
choix = st.radio(
        "Dans quelle catégorie allez vous jouer ?",
        ('Foot animation (U6-U13)', 'Adulte'))



if choix == 'Foot animation (U6-U13)' :

    with st.form("formulaire"):
        st.write("Veuillez remplir les champs suivants :")
        #formulaire = st.form("my_form")
        Nom = st.text_input('Nom')
        Prénom = st.text_input('Prénom')
        Adresse = st.text_input('Adresse complète')
        Mail = st.text_input('Adresse mail')
        Santé = st.text_input('Infos santé à connaître')
        # Menu déroulant des différentes catégories
        liste_ages =['2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011','Autre']
        age = st.selectbox('En quelle année est né votre enfant ?', liste_ages)
        dico_age = {'2018':'U6', '2017':'U7', '2016':'U8', '2015':'U9', '2014':'U10', '2013':'U11', '2012':'U12', '2011':'U13', 'Autre':'Autre'}
        Catégorie = dico_age[age]
        # Parents
        Père = st.text_input('Père : Nom, Prénom, Tél')
        whatsapp_papa = st.selectbox("Avez-vous l'application Whatsapp ?", ['Oui', 'Non'])
        Mère = st.text_input('Mère : Nom, Prénom, Tél ')
        whatsapp_maman = st.selectbox("Avez-vous l'application Whatsapp ? ", ['Oui', 'Non'])
        liste_soutiens = ['Tenue de la buvette','Arbitrage','Administratif','Je ne peux pas soutenir le club']
        Soutien = st.selectbox('Comment pourriez-vous soutenir le club ?', liste_soutiens)
        Contact = st.text_input("Personne à appeler en cas d'urgence (nom + tél)")
        Médecin = st.text_input("Médecin")
        ACCLEA = st.selectbox("Votre enfant va-t-il à l'ACCLEA ?", ['Oui', 'Non'])

        # Now add a submit button to the form:
        #formulaire.form_submit_button("Envoyer")

        submitted = st.form_submit_button("Envoyer")
        if submitted:
            st.write("Merci !")

    dico_form = {
        'Nom':[Nom],
        'Prenom':[Prénom],
        'Adresse':[Adresse],
        'Mail':[Mail],
        'Sante':[Santé],
        'Categorie':[Catégorie],
        'Pere':[Père],
        'whatsapp_papa':[whatsapp_papa],
        'Mere':[Mère],
        'whatsapp_maman':[whatsapp_maman],
        'Soutien':[Soutien],
        'Contact':[Contact],
        'Medecin':[Médecin],
        'ACCLEA':[ACCLEA]
    }

    old_df = pd.read_csv('SRC/formulaire_enfants.csv')
    df = pd.DataFrame(dico_form)
    new_df = pd.concat([old_df, df])
    #df.set_index('Nom')
    #df.to_csv('formulaire.csv',index=False)
    #new_df.drop('Unnamed: 0', axis=1)
    new_df.to_csv('SRC/formulaire_enfants.csv', index=False)
    new_df.to_excel('SRC/formulaire_enfants.xlsx', index=False)





if choix == 'Adulte' :

    with st.form("formulaire"):
        st.write("Veuillez remplir les champs suivants :")
        #formulaire = st.form("my_form")
        Nom = st.text_input('Nom')
        Prénom = st.text_input('Prénom')
        Adresse = st.text_input('Adresse complète')
        Numéro = st.text_input('Numéro de téléphone')
        Mail = st.text_input('Adresse mail')
        Contact = st.text_input("Personne à appeler en cas d'urgence (nom + tél)")
        Santé = st.text_input('Infos santé à connaître')
        


        # Now add a submit button to the form:
        #formulaire.form_submit_button("Envoyer")

        submitted = st.form_submit_button("Envoyer")
        if submitted:
            st.write("Merci !")

    dico_form = {
        'Nom':[Nom],
        'Prenom':[Prénom],
        'Adresse':[Adresse],
        'Numero':[Numéro],
        'Mail':[Mail],
        'Contact':[Contact],
        'Sante':[Santé]
    }

    old_df = pd.read_csv('SRC/formulaire.csv')
    df = pd.DataFrame(dico_form)
    new_df = pd.concat([old_df, df])
    #df.set_index('Nom')
    #df.to_csv('formulaire.csv',index=False)
    #new_df.drop('Unnamed: 0', axis=1)
    new_df.to_csv('SRC/formulaire_adultes.csv', index=False)
    new_df.to_excel('SRC/formulaire_adultes.xlsx', index=False)
