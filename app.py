import streamlit as st
import sqlite3
import random

def create_profile():
    st.header("Create your profile")
    name = st.text_input("Name")
    avatar = st.file_uploader("Avatar")
    if st.button("Create"):
        conn = sqlite3.connect("confidence_booster.db")
        c = conn.cursor()
        c.execute("INSERT INTO users (name, avatar, trophies) VALUES (?, ?, 0)", (name, avatar.read()))
        user_id = c.lastrowid
        conn.commit()
        conn.close()
        st.session_state["user_id"] = user_id
        st.success("Profile created successfully!")
        st.experimental_rerun()

def answer_questions():
    st.header("Answer some questions")
    fear = st.text_input("What's your biggest fear?")
    weakness = st.text_input("What's your biggest weakness?")
    strength = st.text_input("What's your biggest strength?")
    if st.button("Save"):
        conn = sqlite3.connect("confidence_booster.db")
        c = conn.cursor()
        c.execute("UPDATE users SET fear=?, weakness=?, strength=? WHERE id=?", (fear, weakness, strength, st.session_state["user_id"]))
        conn.commit()
        conn.close()
        st.success("Questions saved successfully!")
        st.experimental_rerun()

def challenges():
    st.header("Challenges")
    conn = sqlite3.connect("confidence_booster.db")
    c = conn.cursor()
    c.execute("SELECT * FROM challenges WHERE user_id=?", (st.session_state["user_id"],))
    challenges = c.fetchall()
    conn.close()
    if len(challenges) == 0:
        st.write("You have no challenges yet.")
    else:
        for challenge in challenges:
            if challenge[3] == "daily":
                challenge_text = challenge[2]
                if challenge[4] == "pending":
                    if st.button("Complete challenge"):
                        conn = sqlite3.connect("confidence_booster.db")
                        c = conn.cursor()
                        c.execute("UPDATE challenges SET status='completed' WHERE id=?", (challenge[0],))
                        conn.commit()
                        conn.close()
                        st.success("Challenge completed!")
                        st.experimental_rerun()
                else:
                    st.write(f"You have already completed this challenge: {challenge_text}")
            else:
                st.write("Unknown challenge type")

def generate_challenge():
    challenges = [
        "Compliment a stranger",
        "Try a new food",
        "Learn a new skill",
        "Take a risk",
        "Do something kind for someone else"
    ]
    return random.choice(challenges)

def daily_challenge():
    st.header("Daily Challenge")
    if "challenge_text" not in st.session_state:
        challenge_text = generate_challenge()
        st.session_state["challenge_text"] = challenge_text
    else:
        challenge_text = st.session_state["challenge_text"]
    st.write(challenge_text)
    if st.button("Accept challenge"):
        conn = sqlite3.connect("confidence_booster.db")
        c = conn.cursor()
        c.execute("INSERT INTO challenges (user_id, text, status, type)
# Liste des défis possibles pour chaque point faible
defis = {
    "confiance en soi": ["Faites un compliment à un(e) inconnu(e)", "Parlez de vos réussites à quelqu'un", "Faites une activité que vous aimez sans vous soucier du jugement des autres"],
    "timidité": ["Demandez de l'aide à un(e) inconnu(e)", "Parlez à un(e) inconnu(e) dans un lieu public", "Participez à une conversation de groupe"],
    "gestion du stress": ["Faites de la méditation pendant 10 minutes", "Faites une activité relaxante (yoga, lecture, etc.)", "Respirez profondément et comptez jusqu'à 10 avant de réagir à une situation stressante"]
}

# Fonction pour générer un défi aléatoire en fonction des points faibles de l'utilisateur
def generer_defi(points_faibles):
    defi = None
    # Choix d'un point faible aléatoire
    point_faible = random.choice(points_faibles)
    # Choix d'un défi aléatoire pour ce point faible
    if point_faible in defis:
        defi = random.choice(defis[point_faible])
    return defi

# Fonction pour valider un défi et ajouter des clés ou des trophées à l'utilisateur
def valider_defi(reussi, cle, trophee):
    if reussi:
        # Ajout des clés ou des trophées en fonction du type de récompense du défi
        if cle:
            utilisateur["cles"] += cle
        if trophee:
            # Ajout de trophées en fonction de la difficulté du défi
            if trophee == "facile":
                utilisateur["trophees"] += 1
            elif trophee == "moyen":
                utilisateur["trophees"] += 2
            elif trophee == "difficile":
                utilisateur["trophees"] += 3

# Fonction pour afficher un défi et récupérer la réponse de l'utilisateur
def afficher_defi():
    st.write(f"**Défi du jour :** {defi}")
    reussi = st.radio("Avez-vous réussi ce défi ?", options=["Oui", "Non"])
    # Si le défi est réussi, on ajoute des clés ou des trophées à l'utilisateur
    if reussi == "Oui":
        cle = random.choice([1, 2, 3, 4])
        trophee = None
        if cle == 4:
            trophee = random.choice(["facile", "moyen", "difficile"])
        valider_defi(True, cle, trophee)
        st.write("Bravo, vous avez réussi votre défi !")
    else:
        st.write("Pas de chance, vous pourrez retenter votre chance demain !")

# Fonction pour afficher la fenêtre de chat avec un(e) inconnu(e)
def afficher_chat():
    st.write("**Fenêtre de chat**")
    st.write("Vous êtes maintenant connecté(e) avec un(e) inconnu(e).")
    message = st.text_input("Entrez

