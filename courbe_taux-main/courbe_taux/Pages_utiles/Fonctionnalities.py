import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from datetime import datetime
import plotly.graph_objs as go 
from dateutil.relativedelta import relativedelta  # Pour le calcul précis des mois/jours
import time
#from Datas.data_link import data_dir
#path = data_dir('Tableau de suivi Emissions CEMAC au 10 avril 2025 (1).xlsx')

#df = pd.read_excel(path, sheet_name='BTA')


def fonctionnalities_load():
    
   

    # CSS personnalisé pour les conteneurs
    st.markdown("""
        <style>
        .block-container {
            background-color: #f5f5f5;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .stMetric {
            background-color: white;
            padding: 15px;
            border-radius: 8px;
        }
        </style>
        """, unsafe_allow_html=True)
    st.title("A PROPOS DE ISSEA ENDOWMENT FUND")
    
    