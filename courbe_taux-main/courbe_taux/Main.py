import streamlit as st
from PIL import Image
import base64

# Configuration de la page
st.set_page_config(
    page_title="ISSEA ENDOWMENT FUND - YIELD CURVE",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Import de tes modules
from Photos.photo_link import main_dir
from Pages_utiles.About_us import about_us_page
from Pages_utiles.endowment import page_endowment
from Pages_utiles.courbe import page_nelson_siegel
from Pages_utiles.methodologie import page_methodologie
from Pages_utiles.ChatBlood import chat_load
from Pages_utiles.Fonctionnalities import fonctionnalities_load

# Chargement des images
logo_path = main_dir("CEMAC.png")
logo = Image.open(logo_path)
coeur_path = main_dir("CEMAC-DR.jpg")
coeur = Image.open(coeur_path)
qr_path = main_dir("issea endowment fund - yield curve.png")
qr_code = Image.open(qr_path)
page_icon_path = main_dir("yield_curve_icon.png")
page_icon = Image.open(page_icon_path)
issea_path = main_dir("logo_issea.jpg")
issea = Image.open(issea_path)
Endow_path = main_dir("ISSEA ENDOWMENT FUND.jpg")
Endow = Image.open(Endow_path)

# Style CSS
st.markdown("""
    <style>
        .header-box {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            border: 3px solid #2E8B57;
            margin-bottom: 20px;
        }
        .header-title {
            font-size: 28px;
            font-weight: bold;
            color: #003366;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            text-align: center;
            margin-top: 10px;
        }
        .logo-container {
            display: flex;
            justify-content: center;
            gap: 40px;
            margin-bottom: 10px;
            flex-wrap: wrap;
        }
        img.logo {
            height: 70px;
        }
    </style>
""", unsafe_allow_html=True)

# Initialisation de l'état de session
if "auth_status" not in st.session_state:
    st.session_state.auth_status = False  # False = non connecté
if "username" not in st.session_state:
    st.session_state.username = ""

# Page d'accueil
if not st.session_state.auth_status:
    with st.sidebar:
        st.title('🏠 Accueil')
        st.sidebar.markdown('---')
        st.sidebar.image(coeur, use_column_width=True)
        st.sidebar.markdown('---')
        st.sidebar.image(qr_code, use_column_width=True)

    with st.container():
    # 🎨 Style CSS pour embellir le banner
        st.markdown("""
        <style>
            .banner {
                background: linear-gradient(90deg, #003366 0%, #005b96 100%);
                padding: 20px;
                border-radius: 15px;
                box-shadow: 0px 4px 12px rgba(0,0,0,0.25);
                margin-bottom: 20px;
            }
            .banner-title {
                text-align: center;
                font-size: 40px;
                font-weight: bold;
                : white;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                margin-top: 20px;
            }
            .logo-img {
                display: flex;
                justify-content: center;
                align-items: center;
            }
            img {
                border-radius: 10px;
            }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='banner'>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 6, 1])

    with col1:
        st.markdown("<div class='logo-img'>", unsafe_allow_html=True)
        st.image(Endow, width=100)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<h1 class='banner-title'>ISSEA ENDOWMENT FUND</h1>", unsafe_allow_html=True)

    with col3:
        st.markdown("<div class='logo-img'>", unsafe_allow_html=True)
        st.image(issea, width=100)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


    st.image(logo, use_column_width=True)
    st.markdown('---')
    
    st.markdown("""
    <style>
        .intro-text {
            font-size: 22px;
            font-weight: bold;
            color: #003366;
            text-align: center;
            margin-top: 20px;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
        }
        .intro-text span {
            color: #2E8B57; /* Couleur verte */
            font-weight: bold;
        }
    </style>
    <div class="intro-text">
        Bienvenue sur l'application interactive de suivi des courbes de taux des obligations de la zone <span>CEMAC</span>.
        <br><br>
        Explorez nos fonctionnalités pour une analyse complète et dynamique des taux d'intérêt de la région.
    </div>
""", unsafe_allow_html=True)

    
    st.markdown('---')
if "auth_status" not in st.session_state:
    st.session_state.auth_status = False  # Est-ce que l'utilisateur est connecté ?

if "auth_page" not in st.session_state:
    st.session_state.auth_page = False  # Est-ce que l'utilisateur est sur la page de login ?

if "username" not in st.session_state:
    st.session_state.username = ""  # Stockage du nom d'utilisateur après connexion

# Si PAS connecté
if not st.session_state.auth_status:

    # Et si PAS encore cliqué sur "Accéder aux fonctionnalités"
    if not st.session_state.auth_page:

        # Alors afficher ton super bloc d'accueil :
        st.markdown("""
            <style>
                .section-title { font-size: 28px; font-weight: bold; color: #003366; text-align: center; margin-bottom: 20px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
                .features-section { display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; margin-top: 10px; }
                .feature-card { background-color: #f0f8ff; padding: 20px; border-radius: 12px; text-align: center; box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.1); transition: all 0.3s ease; }
                .feature-card:hover { background-color: #e3f2f1; transform: translateY(-5px); box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.2); }
                .feature-card .icon { font-size: 40px; color: #2E8B57; margin-bottom: 10px; }
                .feature-card .title { font-size: 18px; font-weight: bold; color: #003366; }
                .feature-card .description { font-size: 14px; color: #555555; }
            </style>
        """, unsafe_allow_html=True)

        st.markdown("<h2 class='section-title'>Fonctionnalités du tableau de bord</h2>", unsafe_allow_html=True)
        st.markdown("<div class='features-section'>", unsafe_allow_html=True)

        st.markdown("""
            <div class='feature-card'>
                <div class='icon'>🏛️</div>
                <div class='title'>A PROPOS DE ISSEA ENDOWMENT FUND</div>
                <div class='description'>Découvrez le fonds et son impact sur la région.</div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class='feature-card'>
                <div class='icon'>📊</div>
                <div class='title'>COURBES DE TAUX</div>
                <div class='description'>Suivi des taux des obligations CEMAC.</div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class='feature-card'>
                <div class='icon'>🔬</div>
                <div class='title'>MÉTHODOLOGIE</div>
                <div class='description'>Explication du modèle Nelson-Siegel.</div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class='feature-card'>
                <div class='icon'>🤖</div>
                <div class='title'>ASSISTANT IA</div>
                <div class='description'>Analyse assistée par intelligence artificielle.</div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class='feature-card'>
                <div class='icon'>ℹ️</div>
                <div class='title'>PRÉSENTATION DE L'ÉQUIPE</div>
                <div class='description'>Rencontrez les membres du projet.</div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

st.markdown('---')

# Seulement afficher ce bloc si l'utilisateur n'est PAS connecté et PAS encore en train de se connecter
if not st.session_state.auth_status and not st.session_state.auth_page:
    st.markdown("### 🌍 Explorez les fonctionnalités dès maintenant !")
    if st.button("Accéder aux Fonctionnalités"):
        st.session_state.auth_page = True

# Interface d'authentification
if "auth_page" in st.session_state and st.session_state.auth_page:
    with st.container():
        colg, colc, cold = st.columns([1, 2, 1])
        with colc:
            with st.form(key="login_form"):
                st.subheader("Connexion 🔒")
                username = st.text_input("Nom d'utilisateur 👤", help="Entrez : admin")
                password = st.text_input("Mot de passe 🔑", type="password", help="Entrez : 12")

                submit_button = st.form_submit_button("✅ Valider")
                if submit_button:
                    if username == "admin" and password == "12":
                        st.session_state.auth_status = True
                        st.session_state.username = username
                        st.session_state.auth_page = False
                        st.rerun()
                    else:
                        st.error("❌ Identifiants incorrects. Veuillez réessayer.")

# Interface après connexion (avec Sidebar)
if st.session_state.auth_status:
    st.sidebar.title(f"Bienvenue, {st.session_state.username} 👋")
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Aller à :", [
        "Présentation Endowment Fund",
        "Courbes de Taux",
        "Méthodologie Nelson-Siegel",
        "Assistant IA",
        "Présentation de l'équipe"
    ])

    if page == "Présentation Endowment Fund":
        page_endowment()
    elif page == "Courbes de Taux":
        page_nelson_siegel()
    elif page == "Méthodologie Nelson-Siegel":
        page_methodologie()
    elif page == "Assistant IA":
        chat_load()
    elif page == "Présentation de l'équipe":
        about_us_page()
    else:
        fonctionnalities_load()

    if st.sidebar.button("Se déconnecter"):
        del st.session_state["auth_status"]
        del st.session_state["username"]
        st.rerun()
