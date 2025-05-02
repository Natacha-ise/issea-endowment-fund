import streamlit as st
from PIL import Image
from Photos.photo_link import main_dir

def about_us_page():
    # 🎨 Style CSS global pour fond et textes
    st.markdown("""
    <style>
        body {
            background-color: #f0f2f6;
        }
        .main {
            background-color: #f0f2f6;
            padding: 2rem;
            border-radius: 10px;
        }
        .title {
            color: #2E8B57;
            text-align: center;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-size: 42px;
            margin-bottom: 20px;
        }
        .subsection {
            background-color: white;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
        .member-name {
            font-size: 26px;
            font-weight: bold;
            color: #003366;
            margin-bottom: 10px;
        }
        .contact-info {
            font-size: 18px;
            line-height: 1.8;
            color: #333;
        }
    </style>
    """, unsafe_allow_html=True)

    # 🏛️ Titre principal
    st.markdown("<h1 class='title'>À propos de nous</h1>", unsafe_allow_html=True)

    st.markdown("<div class='subsection'>", unsafe_allow_html=True)
    st.write("""
    Nous sommes un **comité de deux étudiants** accompagnés de **trois enseignants**, dans le cadre du 
    **mémoire en groupe de travail (GT)**.  
    Notre mission est de combiner **rigueur scientifique**, **innovation technologique** et **engagement économique** au service du développement de la CEMAC.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('---')

    # 👩‍🎓 Affichage d'un membre
    mpolah = Image.open(main_dir("mpolah.jpg"))
    mpolah = mpolah.resize((200, 300))

    st.markdown("<div class='subsection'>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(mpolah, use_column_width=False)

    with col2:
         st.markdown(
        f"""
        - 📧 Email:  <fortunempolah@gmail.com>
        - Linkedin:  http://www.linkedin.com/in/flaire-natacha-mpolah-soh-75b324268
        """,
        unsafe_allow_html=True,
    )
    st.markdown('---')
    st.markdown('---')
