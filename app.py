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
        c.execute("INSERT INTO challenges (user_id, text, status, type) VALUES (?, ?, 'pending', 'daily')", (st.session_state["user_id"], challenge_text))
        conn.commit()
        conn.close()
        st.success("Challenge accepted!")
        st.experimental_rerun()

menu = ["Home", "Create Profile", "Answer Questions", "Challenges", "Daily Challenge"]
choice = st.sidebar.selectbox("Select an option", menu)

if choice == "Home":
    st.title
