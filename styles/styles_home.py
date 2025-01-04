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

        /* Estilo para o contador de visitas no canto inferior direito */
        .counter {
            position: fixed;
            bottom: 10px;
            right: 10px;
            background-color: #f1f1f1;
            padding: 8px 12px;
            border-radius: 12px;
            font-size: 12px;
            color: #333;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            border: 1px solid #ddd;
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

    # Função para contar visitas
    def count_visits():
        # Se 'visits' ainda não existe, inicializa a variável
        if 'visits' not in st.session_state:
            st.session_state.visits = 0
        # Incrementa a quantidade de visitas
        st.session_state.visits += 1
        return st.session_state.visits

    # Contador de visitas
    visits = count_visits()

    # HTML para o contador de visitas no canto inferior direito
    badge_html = f"""
        <div class="counter">
            Visitas: {visits}
        </div>
    """

    # HTML para o rodapé com o nome do autor
    footer_html = """
        <div class="footer">
            Feito por Isis Manzano
        </div>
    """

    # Exibe o contador de visitas no canto inferior direito
    st.markdown(badge_html, unsafe_allow_html=True)

    # Exibe o rodapé no centro inferior da página
    st.markdown(footer_html, unsafe_allow_html=True)
