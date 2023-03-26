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
    st.write("Défi facile : dessinez une image de vous-même")
    st.write("Défi moyen : écrivez un paragraphe sur votre plus grande peur")
    st.write("Défi difficile : contactez quelqu'un que vous n'avez pas parlé depuis longtemps")
    st.write("Défi très difficile : donnez un discours en public")
elif niveau_anxiete == "Un peu":
    st.write("Défi facile : dessinez une image de vous-même")
    st.write("Défi moyen : écrivez un paragraphe sur votre plus grande peur")
    st.write("Défi difficile : contactez quelqu'un que vous n'avez pas parlé depuis longtemps")
    st.write("Défi très difficile : donnez un discours en public")
elif niveau_anxiete == "Assez":
    st.write("Défi facile : dessinez une image de vous-même")
    st.write("Défi moyen : écrivez un paragraphe sur votre plus grande peur")
    st.write("Défi difficile : contactez quelqu'un que vous n'avez pas parlé depuis longtemps")
    st.write("Défi très difficile : donnez un discours en public")
else:
    st.write("Défi facile : dessinez une image de vous-même")
    st.write("Défi moyen : écrivez un paragraphe sur votre plus grande peur")
    st.write("Défi difficile : contactez quelqu'un que vous n'avez pas parlé depuis longtemps")
    st.write("Défi très difficile : donnez un discours en public")
