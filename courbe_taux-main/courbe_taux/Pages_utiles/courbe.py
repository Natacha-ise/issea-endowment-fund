
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from Datas.data_link import data_dir
path=data_dir("tableau de suivi Emissions CEMAC au 10 avril 2025 (1) - Copy.xlsm")
data=pd.read_excel(path, sheet_name='Data', engine='openpyxl', header=0)
# 🔵 Page Nelson-Siegel
def page_nelson_siegel():
    st.markdown("""
    <h1 style='text-align: center; color: #2E86C1;'>
    📈 ISSEA Endowment Fund<br>Courbe des taux Nelson-Siegel
    </h1>
    """, unsafe_allow_html=True)
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

    # === Chargement des données ===
    # Fonction pour charger et filtrer les colonnes à partir de AA
    def load_xlsm(file):
        # Lire le fichier xlsm avec pandas
        df = pd.read_excel(file, sheet_name='Data', engine='openpyxl', header=0)
    
        # Sélectionner les colonnes à partir de 'AA'
        df = df.copy()
    
        return df

    # === Chargement du fichier ===
    uploaded_file = st.file_uploader("Tableau de suivi Emissions CEMAC au 10 avril 2025 (1) - Copy.xlsm", type=["xlsm", "csv"])

    if uploaded_file is not None:
    # Vérifier l'extension du fichier
        if uploaded_file.name.endswith('.xlsm'):
            # Charger le fichier et filtrer les colonnes
            df = load_xlsm(uploaded_file)
            # Afficher le DataFrame filtré
            st.dataframe(df)
        else:
            st.warning("Veuillez télécharger un fichier .xlsm")
        # Renommer les colonnes pour standardisation
        df = df.rename(columns={
            "Maturité_annee": "maturité",
            "Taux de coupon(Taux de Rendement Moyen Pondéré)": "rendement"
     })
    else:
        df = data.copy()
        df = df.rename(columns={
            "Maturité_annee": "maturité",
            "Taux de coupon(Taux de Rendement Moyen Pondéré)": "rendement"})
    # Conversion de la colonne 'Date' si elle existe
    if 'Date_d_adjudication' in df.columns:
        df['Date'] = pd.to_datetime(df['Date_d_adjudication'], errors='coerce')
        df['Année'] = df['Date'].dt.year
        df['Mois'] = df['Date'].dt.month
    elif 'Année' in df.columns and 'Mois' in df.columns:
        pass  # Données déjà prêtes
    else:
        st.error("Les colonnes 'Date' ou 'Année' et 'Mois' sont requises pour le filtrage.")
        st.stop()

    # === Filtres interactifs ===
    années = sorted(df['Année'].dropna().unique())
    mois = sorted(df['Mois'].dropna().unique())
    pays = sorted(df['Pays'].dropna().unique()) if 'Pays' in df.columns else []
    types = sorted(df['Titre'].dropna().unique()) if 'Titre' in df.columns else []

    # Option "Tout sélectionner"
    tout_selectionner = "Tout sélectionner"

    # Filtres interactifs
    st.markdown("<span style='color: white;'>Choisir l’année :</span>", unsafe_allow_html=True)
    année_selection = st.selectbox("", [tout_selectionner] + années)

    st.markdown("<span style='color: white;'>Choisir le mois :</span>", unsafe_allow_html=True)
    mois_selection = st.selectbox("", [tout_selectionner] + mois)

    st.markdown("<span style='color: white;'>Choisir le(s) pays :</span>", unsafe_allow_html=True)
    pays_selection = st.multiselect("", [tout_selectionner] + pays, default=pays)

    st.markdown("<span style='color: white;'>Choisir le(s) type(s) d’obligation :</span>", unsafe_allow_html=True)
    type_selection = st.multiselect("", [tout_selectionner] + types, default=types)

    # Gestion des sélections
    if année_selection == tout_selectionner:
        année_selection = années
    else:
        année_selection = [année_selection]

    if mois_selection == tout_selectionner:
        mois_selection = mois
    else:
        mois_selection = [mois_selection]

    if pays_selection == [tout_selectionner]:
        pays_selection = pays

    if type_selection == [tout_selectionner]:
        type_selection = types

    # Application des filtres
    df_filtré = df[
        (df['Année'].isin(année_selection)) &
        (df['Mois'].isin(mois_selection)) &
        (df['Pays'].isin(pays_selection)) &
        (df['Titre'].isin(type_selection))
    ]

    # === Affichage des données filtrées ===
    st.subheader("Données filtrées")
    st.dataframe(df_filtré)

    if df_filtré.empty:
        st.warning("Aucune donnée pour cette sélection.")
        st.stop()

    # === Modèle de Nelson-Siegel ===
    def nelson_siegel(params, maturities):
        beta0, beta1, beta2, tau = params
        m = maturities
        term1 = beta0
        term2 = beta1 * (1 - np.exp(-m / tau)) / (m / tau)
        term3 = beta2 * ((1 - np.exp(-m / tau)) / (m / tau) - np.exp(-m / tau))
        return term1 + term2 + term3

    def objective_function(params, maturities, yields):
        return np.sum((nelson_siegel(params, maturities) - yields) ** 2)

    def fit_nelson_siegel(maturities, yields):
        initial_params = [0.02, -0.02, 0.02, 1.0]
        bounds = [(-10, 10)] * 4
        result = minimize(objective_function, initial_params, args=(maturities, yields), bounds=bounds)
        return result.x

    # === Tracer les courbes ===
    plt.figure(figsize=(10, 6))
    couleurs = {'BTA': 'blue', 'OTA': 'green'}
    titres = df_filtré["Titre"].unique()
    
    
    for titre in titres:
        sous_df = df_filtré[df_filtré["Titre"] == titre]
        if sous_df.empty:
            continue

        maturities = sous_df["maturité"].astype(float).values
        yields = sous_df["rendement"].astype(float).values

        if len(maturities) < 3:
            continue

        params = fit_nelson_siegel(maturities, yields)
        x_vals = np.linspace(0.1, max(maturities) + 1, 100)
        y_vals = nelson_siegel(params, x_vals)

        plt.plot(x_vals, y_vals, label=f"Courbe {titre}", color=couleurs.get(titre, 'gray'))
        plt.scatter(maturities, yields, color=couleurs.get(titre, 'gray'), alpha=0.6)

    plt.title(f"Courbes estimées")
    plt.xlabel("Maturité (années)")
    plt.ylabel("Rendement (%)")
    plt.legend()
    plt.grid(True)

    st.subheader("Courbes estimées")
    st.pyplot(plt)
