import streamlit as st

# Titre de l'application
st.title("Mon application de jeu")
st.image("image3.png", caption="Une image pour vous inspirer")

# Section pour la création de compte et l'identification
st.header("Création de compte et identification")
st.write("Pour jouer, vous devez créer un compte et vous identifier.")
nom_utilisateur = st.text_input("Entrez votre nom d'utilisateur")
mot_de_passe = st.text_input("Entrez votre mot de passe", type="password")
if st.button("Créer un compte"):
    st.write("Compte créé avec succès ! Vous pouvez maintenant vous identifier.")
if st.button("S'identifier"):
    st.write("Identification réussie ! Bienvenue", nom_utilisateur, "!")

# Formulaire pour obtenir les informations de l'utilisateur
st.header("Informations sur l'utilisateur")
age_utilisateur = st.number_input("Entrez votre âge")
niveau_anxiete = st.selectbox("À quel point vous sentez-vous anxieux en général ?", ["Pas du tout", "Un peu", "Assez", "Très"])

# Affichage des informations de l'utilisateur
st.write("Vous avez", age_utilisateur, "ans et vous vous sentez", niveau_anxiete, "anxieux en général.")

# Définition des défis en fonction du niveau d'anxiété de l'utilisateur
if niveau_anxiete == "Pas du tout":
    defi_facile = "Défi facile : dessinez une image de vous-même"
    defi_moyen = "Défi moyen : écrivez un paragraphe sur votre plus grande peur"
    defi_difficile = "Défi difficile : contactez quelqu'un que vous n'avez pas parlé depuis longtemps"
    defi_tres_difficile = "Défi très difficile : donnez un discours en public"
elif niveau_anxiete == "Un peu":
    defi_facile = "Défi facile : dessinez une image de vous-même"
    defi_moyen = "Défi moyen : écrivez un paragraphe sur votre plus grande peur"
    defi_difficile = "Défi difficile : contactez quelqu'un que vous n'avez pas parlé depuis longtemps"
    defi_tres_difficile = "Défi très difficile : donnez un discours en public" 
elif niveau_anxiete == "Assez":
    defi_facile = "Défi facile : dessinez une image de vous-même"
    defi_moyen = "Défi moyen : écrivez un paragraphe sur votre plus grande peur"
    defi_difficile = "Défi difficile : contactez quelqu'un que vous n'avez pas parlé depuis longtemps"
    defi_tres_difficile = "Défi très difficile : donnez un discours en public"
else:
    defi_facile = "Défi facile : dessinez une image de vous-même"
    defi_moyen = "Défi moyen : écrivez un paragraphe sur votre plus grande peur"
    defi_difficile = "Défi difficile : contactez quelqu'un que vous n'avez pas parlé depuis longtemps"
    defi_tres_difficile = "Défi très difficile : donnez un discours en public"

# Section pour les défis
st.write("Choisissez le défi que vous voulez relever :")
defi_choisi = st.selectbox("", [defi_facile, defi_moyen, defi_difficile, defi_tres_difficile])
if st.button("Relever le défi"):
st.write("Défi relevé avec succès ! Bravo !")
Section pour les scores
st.header("Scores")
score_total = 0
score_total += 10 # Pour avoir créé un compte
score_total += 20 # Pour s'être identifié
score_total += age_utilisateur
if niveau_anxiete == "Un peu":
score_total += 20
elif niveau_anxiete == "Assez":
score_total += 30
elif niveau_anxiete == "Très":
score_total += 50
st.write("Votre score total est de", score_total, "points.")

Section pour les options de l'application
st.sidebar.header("Options de l'application")
option_1 = st.sidebar.checkbox("Option 1")
option_2 = st.sidebar.checkbox("Option 2")
option_3 = st.sidebar.checkbox("Option 3")
if st.sidebar.button("Sauvegarder les options"):
st.sidebar.write("Options sauvegardées avec succès !")





