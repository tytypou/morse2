import streamlit as st
import random 

st.title("Ceci est la première énigme")
st.write("Vous devez réussir cette énigme pour passer à la suivante.")

# Dictionnaire de correspondance lettre -> Morse
morse_code_dict = {
    'A': '·−', 'B': '−···', 'C': '−·−·', 'D': '−··', 'E': '·', 'F': '··−·',
    'G': '−−·', 'H': '····', 'I': '··', 'J': '·−−−', 'K': '−·−', 'L': '·−··',
    'M': '−−', 'N': '−·', 'O': '−−−', 'P': '·−−·', 'Q': '−−·−', 'R': '·−·',
    'S': '···', 'T': '−', 'U': '··−', 'V': '···−', 'W': '·−−', 'X': '−··−',
    'Y': '−·−−', 'Z': '−−··'
}

# Fonction pour convertir un texte en Morse
def texte_to_morse(texte):
    return "  @ ".join(morse_code_dict.get(char.upper(), char) for char in texte)

# Liste des mots possibles
mots = ["LUNE", "SOLEIL", "ECLIPSE", "NUIT", "JOUR", "PLUIE", "TONNERRE", "ORAGE", "RAYON", "OBSCURITE", "LUMIERE"]

# Stocker le mot en session pour qu'il ne change pas après chaque erreur
if "mot_a_deviner" not in st.session_state:
    st.session_state["mot_a_deviner"] = random.choice(mots)

choisir_mots = st.session_state["mot_a_deviner"]
mots_en_morse = texte_to_morse(choisir_mots)

# Initialiser la variable d'état pour la progression

if 'can_proceed' not in st.session_state:
    st.session_state.can_proceed = False

st.write(f"Mot à déchiffrer : {mots_en_morse}")
st.write("Attention, il change à chaque mauvaise réponse !")

# Entrée utilisateur
reponse = st.text_input("Votre réponse (en majuscules) :")

if reponse:
    if reponse.upper() == st.session_state.choisir_mots:
        st.success("Bravo, c'est correct !")
    st.session_state.can_proceed = True
else:
    st.error("Mauvaise réponse. Essayez encore !")
    st.session_state.can_proceed = False

