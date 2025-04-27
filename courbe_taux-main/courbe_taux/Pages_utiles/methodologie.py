import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 🧠 Page Méthodologie Nelson-Siegel
def page_methodologie():
    st.title("📚 Méthodologie du modèle Nelson-Siegel")

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

    st.header("🧩 Introduction")
    st.write("""
    Le modèle **Nelson-Siegel** est largement utilisé pour modéliser la **courbe des taux d'intérêt**. 
    Il propose une structure fonctionnelle simple et flexible pour décrire la relation entre les taux 
    d'intérêt et la maturité.
    """)

    st.header("🔹 Formule mathématique")
    st.latex(r"""
    y(\tau) = \beta_0 + \beta_1 \frac{1 - e^{-\tau/\lambda}}{\tau/\lambda} + \beta_2 \left( \frac{1 - e^{-\tau/\lambda}}{\tau/\lambda} - e^{-\tau/\lambda} \right)
    """)

    st.write("""
    où :
    - \\( y(\\tau) \\) est le taux d'intérêt pour une échéance \\( \\tau \\),
    - \\( \\beta_0 \\) : Niveau de long terme,
    - \\( \\beta_1 \\) : Effet de court terme,
    - \\( \\beta_2 \\) : Effet de moyen terme (courbure),
    - \\( \\lambda \\) (ou \\( \\tau \\)) : Paramètre d'ajustement de la rapidité de variation.
    """)

    st.header("🔹 Interprétation économique des paramètres")
    st.write("""
    - **β₀ (niveau)** : capture le niveau de taux d'intérêt à long terme. Plus β₀ est élevé, plus les taux longs sont élevés.
    - **β₁ (pente)** : capte l'effet de court terme. Généralement négatif, il traduit la prime pour l'échéance courte.
    - **β₂ (courbure)** : ajuste la convexité ou la forme de la courbe (par exemple, bombement au milieu).
    - **λ (ou τ)** : détermine où se situe le maximum de la courbure.
    """)

    st.success("La flexibilité du modèle Nelson-Siegel permet de modéliser différentes formes de courbe de taux : croissante, décroissante, en cloche, etc.")
