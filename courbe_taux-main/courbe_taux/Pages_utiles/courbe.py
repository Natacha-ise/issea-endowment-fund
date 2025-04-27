
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 🔵 Page Nelson-Siegel
def page_nelson_siegel():
    st.title("📈 ISSEA Endowment Fund - Courbe des taux Nelson-Siegel")

    # 🎨 Style CSS
    st.markdown("""
        <style>
            .main {
                background-color: #0f1117;
                color: white;
            }
            .stButton>button {
                background-color: #228B22;
                color: white;
            }
            .stSelectbox, .stSlider {
                background-color: #1c1e24;
            }
            h1, h2 {
                color: #32CD32;
            }
        </style>
        """, unsafe_allow_html=True)

    # 🔘 Sélection du pays
    pays = st.selectbox("Veuillez choisir le pays :", [
        "Cameroun", "Congo", "Gabon", "Tchad", "RCA", "Guinée Équatoriale"
    ])

    # 📆 Sélection année et mois
    annee = st.slider("Veuillez choisir l’année :", 2011, 2025, 2024)
    mois = st.selectbox("Veuillez choisir le mois :", [
        "Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
        "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"
    ])
    mois_index = [
        "Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
        "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"
    ].index(mois) + 1

    # 🔢 Données fictives
    maturite = np.array([0.25, 0.5, 1, 2, 3, 5, 7, 10])
    prix_strip = np.exp(-0.03 * maturite)  # Simule B
    taux_zero_coupon = -np.log(prix_strip) / maturite  # Simule R
    beta0, beta1, beta2, tau = 0.03, -0.02, 0.01, 1.5

    # Fonction taux continu NS
    def taux_continu_ns(t):
        return beta0 + beta1 * (1 - np.exp(-t / tau)) / (t / tau) + beta2 * ((1 - np.exp(-t / tau)) / (t / tau) - np.exp(-t / tau))

    taux_continu = taux_continu_ns(maturite)

    # 📊 Affichage des résultats
    st.subheader(f"📊 Données pour {pays}, {mois} {annee}")
    st.write("**Prix des strips (B)** :", prix_strip)
    st.write("**Taux zéro coupon (R)** :", taux_zero_coupon)
    st.write("**Taux continus de maturité** :", taux_continu)

    # 📈 Tracé de la courbe
    fig, ax = plt.subplots()
    ax.plot(maturite, taux_continu, marker='o', color='#32CD32', label='Taux continu (Nelson-Siegel)')
    ax.set_title("Courbe de taux continue")
    ax.set_xlabel("Maturité (années)")
    ax.set_ylabel("Taux")
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.set_facecolor('#1c1e24')
    fig.patch.set_facecolor('#1c1e24')
    ax.tick_params(colors='white')
    ax.title.set_color('#32CD32')
    ax.yaxis.label.set_color('white')
    ax.xaxis.label.set_color('white')
    ax.legend(facecolor='#1c1e24', edgecolor='white')
    st.pyplot(fig)

    # 🔣 Paramètres Nelson-Siegel
    st.markdown("### 📌 Paramètres du modèle Nelson-Siegel")
    st.markdown(f"**Beta 0** = {beta0:.4f} ; **Beta 1** = {beta1:.4f} ; **Beta 2** = {beta2:.4f} ; **Tau** = {tau:.4f}")

