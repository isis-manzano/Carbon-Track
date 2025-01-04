import streamlit as st

def custom_css():
    st.markdown(
        """
        <style>
        /* Altera o fundo da área do header (Settings) */
        header[data-testid="stHeader"] {
            background-color: #efecd2; /* Mantém a cor original */
            border-bottom: 1px solid #ddd; /* Linha sutil para separar o header */
            padding: 10px 0;
        }

        /* Altera o fundo da barra lateral */
        section[data-testid="stSidebar"] {
            background-color: #b6af87; /* Mantém a cor original */
            border-right: 1px solid #ddd; /* Linha sutil de borda */
        }

        /* Altera o fundo geral da aplicação */
        .stApp {
            background-color: #efecd2; /* Mantém o fundo original */
        }

        /* Estilizando o container de conteúdo principal */
        .block-container {
            max-width: 1200px; /* Largura máxima ajustada */
            width: 100%;
            margin: 0 auto;
            padding: 20px;
        }

        /* Melhorando o layout das colunas para informações */
        .stColumns {
            display: flex;
            gap: 2rem; /* Mais espaço entre as colunas */
            flex-wrap: wrap; /* Adapta a coluna para dispositivos menores */
        }

        /* Botões com estilo mais clean e cores mais próximas ao padrão */
        .stButton>button {
            background-color: #b6af87; 
            color: white;
            font-size: 12px;
            padding: 12px 25px;
            border-radius: 6px;
            border: none;
            transition: background-color 0.3s ease;
            cursor: pointer;
            width: 100%; 
        }

        /* Personalizando as métricas de valores */
        .stMetric {
            background-color: #fff; /* Fundo branco */
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Sombra suave */
            margin-bottom: 15px;
        }

        .stMarkdown {
            font-family: 'Arial', sans-serif;
            color: #444; /* Cor neutra e fácil de ler */
        }

        /* Ajustes nas seções de "info" */
        .stInfo {
            background-color: #f7f7f7; /* Fundo suave para as seções informativas */
            border-radius: 8px;
            padding: 15px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
            margin-bottom: 20px;
        }

        /* Ajustando o conteúdo dos botões de salvar e limpar */
        .stButton>button[data-baseweb="button"] {
            background-color: #b6af87; /* Cor suave para o botão de salvar */
            border-radius: 8px;
            color: white;
        }

        .stButton>button[data-baseweb="button"]:hover {
            background-color: #9e9a70 !important; /* Cor de fundo escura */
        }

        /* Estilo para o rodapé no centro inferior */
        .footer {
            position: fixed;
            bottom: 5px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 12px;
            color: #888;
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

