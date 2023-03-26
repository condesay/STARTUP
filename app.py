import streamlit as st
import sqlite3
import hashlib

# connexion à la base de données
conn = sqlite3.connect('data.db')
c = conn.cursor()

# création des tables dans la base de données
c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, email TEXT UNIQUE, password TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS categories (id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT UNIQUE)''')
c.execute('''CREATE TABLE IF NOT EXISTS problems (id INTEGER PRIMARY KEY AUTOINCREMENT, category_id INTEGER, problem TEXT, anxiety_level TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS challenges (id INTEGER PRIMARY KEY AUTOINCREMENT, problem_id INTEGER, challenge TEXT, difficulty TEXT)''')

# ajout des données initiales dans les tables
c.execute("INSERT OR IGNORE INTO categories (category) VALUES ('Communication')")
c.execute("INSERT OR IGNORE INTO categories (category) VALUES ('Créativité')")
c.execute("INSERT OR IGNORE INTO categories (category) VALUES ('Prise de décision')")
c.execute("INSERT OR IGNORE INTO problems (category_id, problem, anxiety_level) VALUES (?, ?, ?)", (1, "Prise de parole difficile", "un peu"))
c.execute("INSERT OR IGNORE INTO problems (category_id, problem, anxiety_level) VALUES (?, ?, ?)", (1, "Communication avec les inconnus", "assez"))
c.execute("INSERT OR IGNORE INTO problems (category_id, problem, anxiety_level) VALUES (?, ?, ?)", (2, "Trouver des idées originales", "beaucoup"))
c.execute("INSERT OR IGNORE INTO problems (category_id, problem, anxiety_level) VALUES (?, ?, ?)", (2, "Sortir de sa zone de confort", "assez"))
c.execute("INSERT OR IGNORE INTO problems (category_id, problem, anxiety_level) VALUES (?, ?, ?)", (3, "Prendre une décision importante", "beaucoup"))
c.execute("INSERT OR IGNORE INTO problems (category_id, problem, anxiety_level) VALUES (?, ?, ?)", (3, "Gérer son stress en situation de pression", "assez"))
c.execute("INSERT OR IGNORE INTO challenges (problem_id, challenge, difficulty) VALUES (?, ?, ?)", (1, "Parler en public devant un petit groupe", "Facile"))
c.execute("INSERT OR IGNORE INTO challenges (problem_id, challenge, difficulty) VALUES (?, ?, ?)", (1, "Faire une présentation PowerPoint", "Moyen"))
c.execute("INSERT OR IGNORE INTO challenges (problem_id, challenge, difficulty) VALUES (?, ?, ?)", (1, "Participer à une réunion en ligne", "Difficile"))
c.execute("INSERT OR IGNORE INTO challenges (problem_id, challenge, difficulty) VALUES (?, ?, ?)", (2, "Demander des indications à un passant", "Facile"))
c.execute("INSERT OR IGNORE INTO challenges (problem_id, challenge, difficulty) VALUES (?, ?, ?)", (2, "Demander l'heure à un étranger", "Moyen"))
c.execute("INSERT OR IGNORE INTO challenges (problem_id, challenge, difficulty) VALUES (?, ?, ?)", (2, "Demander de l'aide à un collègue", "Difficile"))
c.execute("INSERT OR IGNORE INTO challenges (problem_id, challenge, difficulty) VALUES (?, ?, ?)", (3, "Trouver 5 idées originales pour un projet", "Facile"))
