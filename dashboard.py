import streamlit as st
import numpy as np
import math
import plotly as plt 
import pandas as pd

# Utilisation de HTML et CSS pour placer le logo en haut à gauche
st.markdown(
    """
    <style>
    .main .block-container {
        padding-top: 0rem;
    }
    .sidebar .sidebar-content {
        position: absolute;
        top: 0;
        left: 0;
        padding: 0;
    }
    .sidebar .sidebar-content img {
        display: block;
        margin: 0 auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Afficher le logo en haut à gauche
st.sidebar.image("images/tours_logo.svg", use_column_width=True)  # Assurez-vous que le chemin vers le logo est correct

# Navigation des pages
st.sidebar.title("Navigation")
pages = st.sidebar.radio("Aller à", ["Accueil :crown: ", "Ratio Pelle Aviron 	:t-rex: ", "Calcul Pourcentage :medal: ", "Convertisseur Watt/500", "Es-tu Fort? :hatching_chick: "])

if pages == "Accueil :crown: ":
    # Page d'accueil
    st.title("Bienvenue sur mon site dédié aux rameurs :rowboat:")

    # Section d'introduction
    st.header("À propos de moi")
    st.write("""
    Bonjour ! Je suis Pierre Jean, un passionné d'aviron et un étudiant en dernière année de Master 2 Économiste d'Entreprise, spécialisé dans l'analyse économique et statistique. Je suis ravi de partager mes connaissances et mes outils avec vous pour vous aider à améliorer vos performances en aviron.
    """)

    col1, col2 = st.columns(2)

    # Affichez les images dans les colonnes respectives
    with col1:
        st.image("images/univ.jpg", width=200)
    with col2:
        st.image("images/4-.jpg", width=400)

    st.video("videos/8barre.mp4")
    st.video("videos/vidéo_famille.mp4")

    # Section sur vos études
    st.header("Me contacter")
    st.write("""
    Email : pierre.jean@etu.univ-tours.fr  
    LinkedIn : [linkedin.com/in/pierre---jean](https://www.linkedin.com/in/pierre---jean)
    """)

elif pages == "Ratio Pelle Aviron 	:t-rex: ":
    # Premier onglet : Ratio Pelle Aviron
    st.title('Outils pour coach d\'aviron')
    st.header("Ratio Pelle Aviron")
    
    # Créer des champs d'entrée de nombre
    nombre1 = st.number_input('Entrez la longueur de pelle', value=288)
    nombre2 = st.number_input('Entrez le levier intérieur', value=88)

    # Afficher les nombres entrés
    st.write(f'La longueur de pelle est de {nombre1}.')
    st.write(f'Le levier intérieur est de {nombre2}.')

    # Calculer le ratio des rames
    if nombre1 != 0:
        ratio = nombre2 / nombre1
        st.markdown(f'### **Le ratio des rames est de: {ratio:.4f}**', unsafe_allow_html=True)
    else:
        st.error("Erreur : La longueur de pelle ne peut pas être zéro pour calculer le ratio.")


elif pages == "Calcul Pourcentage :medal: ":
    # Deuxième onglet : Calcul Pourcentage
    st.title('Outils pour coach d\'aviron')
 # Définition des records par catégorie et sexe
    records = {
        "J14": {
            "Homme": {
                "4x+": "3:14",
                "8x+": "3:00",
            },
            "Femme": {
                "4x+": "3:38",
                "8x+": "3:26",
            },
            "Mixte": {
                "2x": "3:32",
                "4x+": "3:26",
            },
        },
        "J16": {
            "Homme": {
                "1x": "5:20",
                "2x": "4:53",
                "4x": "4:33",
                "2-": "5:05",
                "4+": "4:48",
                "8+": "4:25"
            },
            "Femme": {
                "1x": "5:50",
                "2x": "5:21",
                "4x": "5:03",
                "2-": "5:35",
                "4+": "5:18",
                "8+": "4:51"
            },
            "Mixte": {
                "4x": "4:48",
            },
        },
        "J18": {
            "Homme": {
                "1x": "6:45",
                "2x": "6:12",
                "4x": "5:44",
                "2-": "6:22",
                "4-": "5:49",
                "8+": "5:29"
            },
            "Femme": {
                "1x": "7:22",
                "2x": "6:51",
                "4x": "6:20",
                "2-": "7:04",
                "4-": "6:22",
                "8+": "6:07"
            },"Mixte": {
                "4x": "6:02",
            },
        },
        "Senior": {
            "Mixte": {
                "4x": "5:47",
                "8+": "5:34"
            },
            "Homme": {
                "Toutes Catégories": {
                    "1x": "6:30",
                    "2x": "5:57",
                    "4x": "5:30",
                    "2-": "6:08",
                    "4-": "5:36",
                    "4+": "5:49",
                    "8+": "5:17"
                },
                "Poids Léger": {
                    "1x": "6:38",
                    "2x": "6:04",
                    "4x": "5:37"
                }
            },
            "Femme": {
                "Toutes Catégories": {
                    "1x": "7:05",
                    "2x": "6:34",
                    "4x": "6:05",
                    "2-": "6:47",
                    "4-": "6:12",
                    "4+": "6:29",
                    "8+": "5:51"
                },
                "Poids Léger": {
                    "1x": "7:22",
                    "2x": "6:40",
                    "4x": "6:12"
                }
            }
        }
    }

    # Fonction pour convertir un temps en secondes
    def temps_en_secondes(temps):
        minutes, secondes = map(int, temps.split(':'))
        return minutes * 60 + secondes

    # Fonction pour calculer le pourcentage par rapport au record
    def calcul_pourcentage(temps_rameur, temps_record):
        temps_rameur_sec = temps_en_secondes(temps_rameur)
        temps_record_sec = temps_en_secondes(temps_record)
        pourcentage = (temps_record_sec / temps_rameur_sec) * 100
        return pourcentage

    # Titre de l'application
    st.title("Calcul de pourcentage par rapport au record du monde")

    # Sélection de la catégorie d'âge
    categorie_age = st.selectbox("Choisissez une catégorie d'âge 	:beaver: ", list(records.keys()))

    # Sélection du sexe
    sexe = st.selectbox("Choisissez le sexe", list(records[categorie_age].keys()))

    # Si Senior est sélectionné, permettre le choix du type de poids
    if categorie_age == "Senior" and sexe != "Mixte":
        categorie_poids = st.selectbox("Choisissez la catégorie de poids", list(records[categorie_age][sexe].keys()))
        categorie = st.selectbox("Choisissez la catégorie", list(records[categorie_age][sexe][categorie_poids].keys()))
        temps_record = records[categorie_age][sexe][categorie_poids][categorie]
    else:
        categorie = st.selectbox("Choisissez la catégorie", list(records[categorie_age][sexe].keys()))
        temps_record = records[categorie_age][sexe][categorie]

    # Entrée du temps du rameur
    st.title('veuillez entrer le temps de la pige')
    temps_rameur = st.text_input("Entrez le temps du rameur (ex: 8:00)")

    # Calcul et affichage du pourcentage
    if st.button("Calculer"):
        if temps_rameur:
            try:
                pourcentage = calcul_pourcentage(temps_rameur, temps_record)
                if categorie_age == "Senior" and sexe != "Mixte":
                    st.write(f"Le pourcentage par rapport au record du monde pour la catégorie {categorie_age} {categorie_poids} {categorie} est de : {pourcentage:.2f}%")
                else:
                    st.write(f"Le pourcentage par rapport au record du monde pour la catégorie {categorie_age} {categorie} est de : {pourcentage:.2f}%")
            except ValueError:
                st.error("Veuillez entrer un temps valide au format MM:SS.")
        else:
            st.error("Veuillez entrer un temps.")

elif pages == "Convertisseur Watt/500":
    st.title("convertisseur ergomètre")
            # Sélectionner le mode de calcul
    mode = st.selectbox("Choisissez le mode de calcul", ["Calculer le temps pour 500 mètres à partir des watts", "Calculer les watts à partir du temps pour 500 mètres"])

    if mode == "Calculer le temps pour 500 mètres à partir des watts":
        # Entrée utilisateur pour les watts
        watts = st.number_input('Entrez la puissance (watts)', value=203, min_value=1, step=1)
        
        # Calcul du temps pour parcourir 500 mètres
        pace = (2.80 / watts) ** (1/3)
        time_seconds = 500 * pace
        
        # Conversion en format minutes:secondes.dixièmes
        minutes = int(time_seconds // 60)
        seconds = int(time_seconds % 60)
        tenths = int((time_seconds - int(time_seconds)) * 10)
        
        # Affichage du résultat
        st.write(f"Avec une puissance de {watts} watts, le temps pour parcourir 500 mètres est de {minutes} minutes, {seconds} secondes et {tenths} dixièmes.")
        
    else:
        # Entrée utilisateur pour le temps en minutes, secondes et dixièmes
        minutes2 = st.number_input('Entrez les minutes', value=2, min_value=0, format="%d")
        seconds2 = st.number_input('Entrez les secondes', value=5, min_value=0, max_value=59, format="%d")
        tenths2 = st.number_input('Entrez les dixièmes de seconde', value=0, min_value=0, max_value=9, format="%d")
        
        # Calcul du temps total en secondes avec les dixièmes
        time_seconds2 = minutes2 * 60 + seconds2 + tenths2 / 10
        
        # Calcul du rythme (pace) en secondes/mètre
        pace2 = time_seconds2 / 500
        
        # Calcul des watts
        watts2 = math.ceil(2.80 / (pace2 ** 3))  # Arrondi vers le haut pour obtenir un entier
        
        # Affichage du résultat
        st.write(f"Avec un temps de {minutes2} minutes, {seconds2} secondes et {tenths2} dixièmes pour parcourir 500 mètres, la puissance calculée est de **{watts2}** watts.")

elif pages == "Es-tu Fort? :hatching_chick: ":
    # Quatrième onglet : Es-tu Fort?
    st.title('Outils pour coach d\'aviron')
    st.header("Es-tu Fort? :lion_face: ")
    # Afficher la description de l'outil "Es-tu Fort?"
    st.write("Cet outil vous permet d'évaluer votre force relative en fonction de vos performances et de votre poids.")
    #convertisseur rapport poids puissance
    st.title("test ergo 2k")
    minutestesterg = st.number_input('Entrez les minutes de votre test ergo', value=7, min_value=0,max_value=59, format="%d")
    secondstesterg = st.number_input('Entrez les secondes de votre test ergo', value=30, min_value=0, max_value=59, format="%d")
    tenthstesterg = st.number_input('Entrez les dixièmes de seconde de votre test ergo', value=0, min_value=0, max_value=9, format="%d")
    st.title("poids en KG")
    poidskg = st.number_input('Entrez vos kg', value=70, min_value=0,max_value=250, format="%d")
    poidshg = st.number_input('Entrez vos hg', value=0, min_value=0, max_value=9, format="%d")

    #fonction
    time_secondsrpp = (minutestesterg * 60 + secondstesterg + tenthstesterg / 10)/4
    poidsrpp = poidskg + (poidshg)/10
    pacerpp = time_secondsrpp / 500
    wattsrpp = math.ceil(2.80 / (pacerpp ** 3)) 
    rppking = wattsrpp/poidsrpp


    st.write(f"Avec un temps de {minutestesterg} minutes, {secondstesterg} secondes et {tenthstesterg} dixièmes pour parcourir 500 mètres, la puissance calculée est de {wattsrpp} watts en moyenne.")
    st.title(f"Ton rapport poids puissance est de {rppking:.2f} RPP")
