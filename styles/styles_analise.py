import streamlit as st

def custom_css():
    st.markdown(
        """
        <style>
        /* Altera o fundo da área do header (Settings) */
        header[data-testid="stHeader"] {
            background-color: #efecd2; /* Cor desejada */
        }

        /* Altera o fundo da barra lateral */
        section[data-testid="stSidebar"] {
            background-color: #b6af87; /* Cor desejada */
        }

        /* Altera a cor de fundo geral da página */
        .stApp {
            background-color: #efecd2;
        }

        /* Centraliza o conteúdo principal */
        .main {
            display: flex;
            justify-content: center;
            align-items: flex-start;
            padding: 1rem;
            width: 100%;
            box-sizing: border-box;
        }

        /* Ajusta a largura do container de conteúdo para ser maior */
        .block-container {
            max-width: 1200px; /* Aumenta a largura máxima para 1200px ou o valor desejado */
            width: 100%; /* Permite que o conteúdo ocupe a largura disponível até o máximo */
            margin: 0 auto; /* Centraliza o conteúdo */
        }

        /* Evita que o container de conteúdo seja redimensionado para ocupar o espaço da sidebar minimizada */
        @media (max-width: 1400px) {
            .block-container {
                margin: 0 auto; /* Garante que o conteúdo permaneça centralizado */
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )
