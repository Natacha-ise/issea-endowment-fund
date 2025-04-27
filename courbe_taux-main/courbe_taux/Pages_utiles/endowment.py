import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 🟢 Page Endowment Fund
def page_endowment():
    st.title("🏛️ Présentation du ISSEA Endowment Fund")

    st.markdown("""
    <style>
        .main {
            background-color: #0f1117;
            color: white;
        }
        h1, h2, h3 {
            color: #32CD32;
        }
    </style>
    """, unsafe_allow_html=True)

    st.header("🔹 Qu'est-ce que l'ISSEA Endowment Fund ?")
    st.write("""
    L'**ISSEA Endowment Fund** est un fonds d’investissement stratégique créé pour soutenir 
    l'excellence académique, la recherche appliquée et le développement économique en Afrique Centrale, 
    en particulier dans la zone CEMAC.

    Il vise à mobiliser des ressources financières pérennes afin de financer durablement :
    - Les programmes d'enseignement supérieur
    - Les projets de recherche innovants
    - Les infrastructures éducatives de l'ISSEA
    - Le rayonnement scientifique et technologique de la région
    """)

    st.header("🎯 Missions principales")
    st.write("""
    - **Assurer la stabilité financière** de l'ISSEA à long terme
    - **Financer des bourses** pour les étudiants talentueux issus de milieux modestes
    - **Investir dans la recherche scientifique** répondant aux défis économiques et sociaux
    - **Accompagner l'innovation** et l'entrepreneuriat en Afrique Centrale
    """)

    st.header("🌍 Objectifs stratégiques")
    st.write("""
    - Devenir un levier majeur de financement de l'enseignement supérieur africain
    - Contribuer à la **réduction de la pauvreté** par l'éducation et la formation de haute qualité
    - Soutenir la **transition économique** vers une économie du savoir dans la région CEMAC
    - Promouvoir des investissements éthiques, responsables et à impact social
    """)

    st.success("Le ISSEA Endowment Fund, un investissement pour l'avenir de l'Afrique !")
