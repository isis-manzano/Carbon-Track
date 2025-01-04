import streamlit as st
from styles.styles_home import custom_css

def app():
    custom_css()

    st.sidebar.markdown("### Meios de Contato")

    # Usando HTML para combinar a imagem e o link
    st.sidebar.markdown("""
        <a href="https://www.linkedin.com/in/isis-tognolli-manzano-45330875/" style="margin-bottom: 15px; text-decoration: none; color: black;">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="30" style="vertical-align: middle;">
            LinkedIn
        </a>
    <br><br>
    """, unsafe_allow_html=True)


    st.sidebar.markdown("""
        <a href="https://github.com/isis-manzano" style="margin-bottom: 15px; text-decoration: none; color: black;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" width="30" style="vertical-align: middle;">
            GitHub
        </a>
    """, unsafe_allow_html=True)


    # Exibindo a imagem do projeto com maior destaque
    st.image("./assets/Logo.png",  use_container_width=True)  

    # Título do projeto
    st.markdown("---")
    st.title("Bem-vindo ao **Carbon-Track**")

    # Introdução e visão geral
    st.markdown("""
    O **Carbon-Track** é uma solução inovadora desenvolvida para a Coca-Cola Solar, com o objetivo de **monitorar e reduzir a pegada de carbono** nas operações logísticas e de produção da empresa.
    
    Este projeto não apenas avalia o impacto ambiental das rotas de transporte, mas também oferece **alternativas sustentáveis** por meio de análises comparativas entre diferentes tipos de veículos (diesel, híbrido e elétrico).
    """)

    st.markdown('<p style="color:green; font-size:20px; font-weight:bold;">🌿 Este projeto é um marco no caminho para um futuro mais sustentável, alinhando inovação e práticas responsáveis 🌿</p>', unsafe_allow_html=True)


    # Seção de Objetivos
    st.markdown("---")
    st.header("Objetivos do Projeto:")

    st.markdown("""
    O **Carbon-Track** tem como objetivos principais:
    - **Monitorar e Reduzir as Emissões de CO2**: Acompanhar as emissões de carbono nas rotas de transporte.
    - **Calcular Consumo de Combustível**: Avaliar o consumo de combustível dos veículos em diversas rotas.
    - **Ajustar as Rotas para Alternativas Sustentáveis**: Identificar rotas com menor impacto ambiental e custos mais baixos.
    - **Promover Transparência e Rastreabilidade**: Disponibilizar informações claras sobre emissões, custos e escolhas sustentáveis.
    - **Realizar Análises Comparativas**: Comparar os impactos de diferentes tipos de veículos para tomar decisões mais ecológicas.
    """)

    st.markdown("---")
    st.header("Documentação:")
    st.subheader("Estrutura de Implementação")

    st.markdown("""
    O **Carbon-Track** foi desenvolvido com uma estrutura eficiente para garantir que todas as etapas, desde o cálculo até a análise dos dados, sejam realizadas com precisão. Abaixo estão os principais componentes do sistema:
    1. **Input de Dados**: O sistema coleta informações sobre origem, destino, peso do veículo e preço do combustível.
    2. **Cálculo das Rotas**: Utiliza a API do Google Maps para obter rotas alternativas e calcular distâncias e tempos de viagem.
    3. **Análise de Emissões e Consumo**: O sistema calcula a emissão de CO2 e o consumo de combustível (diesel, híbrido e elétrico) para cada rota.
    4. **Exibição dos Resultados**: Apresenta gráficos, mapas e métricas para análise comparativa e visualização dos impactos ambientais e custos de cada rota.
    5. **Salvamento de Dados**: Permite que os dados das rotas calculadas sejam exportados em formato CSV para análise futura.
    """)

    st.subheader("Análise de Efetividade")
    st.markdown("""
    A análise de efetividade do **Carbon-Track** será focada nos seguintes pontos:
    - **Redução das Emissões de CO2**: Identificação de rotas com menor emissão de carbono e impacto ambiental.
    - **Economia de Combustível**: Comparação dos custos de combustível entre diferentes tipos de veículos (diesel, híbrido e elétrico).
    - **Facilidade de Adoção**: Avaliação da interface e usabilidade do sistema, para garantir fácil adoção pelas equipes operacionais.
    """)

    st.subheader("Tecnologias Utilizadas")
    st.markdown("""
    O **Carbon-Track** foi desenvolvido com base em tecnologias modernas que garantem precisão, interatividade e escalabilidade:
    - **Streamlit**: Framework usado para construir a interface interativa e os gráficos do projeto.
    - **Google Maps API**: Para obter rotas alternativas e informações sobre distâncias e tempos de viagem.
    - **Altair**: Biblioteca de visualização usada para criar gráficos comparativos de emissões de CO2 e consumo de combustível.
    - **Folium**: Usada para exibir mapas interativos das rotas calculadas.
    - **Pandas**: Para processamento de dados e exportação de informações em formato CSV.
    """)

    st.subheader("Indicadores de Sucesso")
    st.markdown("""
    O sucesso do projeto será medido com base nos seguintes indicadores:
    - **Redução das Emissões de CO2**: Percentual de redução de emissões entre as rotas e veículos.
    - **Economia no Custo de Combustível**: Análise da economia gerada pela escolha de rotas e veículos mais eficientes.
    - **Adoção e Satisfação**: Número de usuários ativos do sistema e a satisfação deles com a ferramenta.
    """)

    st.subheader("Escalabilidade do Projeto")
    st.markdown("""
    O **Carbon-Track** é uma solução escalável que pode ser facilmente integrada em diferentes contextos e expandida para outras áreas da empresa:
    - **Integração com Outros Sistemas**: O sistema pode ser integrado com plataformas de logística e transporte da empresa para fornecer análises em tempo real.
    - **Expansão para Outros Tipos de Veículos**: Pode ser adaptado para veículos de diferentes categorias, como caminhões de maior porte, ou até mesmo frotas de carros de passeio.
    - **Adaptação a Novas Tecnologias**: O sistema pode ser atualizado para incorporar novas tecnologias e fontes de energia renováveis.
    """)


# Chamar a função principal para rodar o app
if __name__ == "__main__":
    app()

