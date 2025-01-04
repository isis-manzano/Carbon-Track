import streamlit as st
import pandas as pd
import os
import locale
import seaborn as sns
import matplotlib.pyplot as plt
from styles.styles_analise import custom_css

# Configurar o locale para o formato brasileiro
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def formatar_brasileiro(valor):
    """Formata um número para o padrão brasileiro."""
    if isinstance(valor, (float, int)):  # Verifica se o valor é numérico
        return locale.format_string('%.2f', valor, grouping=True)
    return valor

def carregar_dados():
    try:
        # Ajustar o separador decimal para vírgula
        data = pd.read_csv("dados_rotas.csv")
        return data
    except FileNotFoundError:
        st.sidebar.error("Arquivo 'dados_rotas.csv' não encontrado. Por favor, inicie uma nova simulação.")
        return pd.DataFrame()

def app():
    custom_css()

    # Mostrando a imagem com largura total
    st.image("./assets/topag.png")

    # Título e introdução
    st.title("📈 Análise de Rotas")
    st.write("Bem-vindo à Página de Análises de Rotas!!")
    st.write("Utilize as abas de filtros para uma melhor experiência.")
    # Carregar os dados do CSV
    data = carregar_dados()

    if data.empty:
        # Se os dados estiverem vazios (por causa do erro de arquivo não encontrado), não continua a execução
        return

    # Filtros por origem e destino
    st.sidebar.header("Filtros")
    
    # Valores padrão para os filtros
    default_origem = "Todas"
    default_destino = "Todos"
    default_tipo_rota = "Todas as rotas"

    # Filtros interativos
    origem = st.sidebar.selectbox("Selecione a origem", options=[default_origem] + list(data["Origem"].unique()))
    destino = st.sidebar.selectbox("Selecione o destino", options=[default_destino] + list(data["Destino"].unique()))
    tipo_rota = st.sidebar.selectbox("Selecione o tipo de rota", options=[default_tipo_rota, "Melhor rota"])

    # Botão para limpar filtros
    if st.sidebar.button("Limpar filtros"):
        origem = default_origem
        destino = default_destino
        tipo_rota = default_tipo_rota

    # Filtrar dados com base nos filtros de origem e destino
    if origem != default_origem and destino != default_destino:
        filtered_data = data[(data["Origem"] == origem) & (data["Destino"] == destino)]
    elif origem != default_origem:
        filtered_data = data[data["Origem"] == origem]
    elif destino != default_destino:
        filtered_data = data[data["Destino"] == destino]
    else:
        filtered_data = data

    # Se a opção for "Melhor rota", filtrar pela melhor rota para o destino específico
    if tipo_rota == "Melhor rota":
        best_routes = filtered_data.loc[filtered_data.groupby('Destino')["Emissão de CO2 Diesel (Kg)"].idxmin()]
        filtered_data = best_routes

    # Verificar se há dados filtrados
    if not filtered_data.empty:
        # Subtítulo e visualização dos dados
        st.subheader(f"Rotas de {origem} para {destino}")
        st.dataframe(filtered_data)

        
        # Garantir que as colunas estão no formato correto
        numeric_columns = [
            "Distância (km)", "Emissão de CO2 Diesel (Kg)", 
            "Emissão de CO2 Híbrido (kg)", "Emissão de CO2 Elétrico (kg)",
            "Custo do Combustível Diesel (R$)", "Custo do Combustível Híbrido (R$)", 
            "Custo do Combustível Elétrico (R$)"
        ]

        # Remover pontos de separação de milhar e substituir vírgulas por pontos antes de converter para float
        for column in numeric_columns:
            filtered_data[column] = filtered_data[column].str.replace('.', '', regex=False).str.replace(',', '.', regex=False).astype(float)

        # Cálculos internos, mantendo como float para precisão
        total_km = filtered_data["Distância (km)"].sum()
        total_co2_diesel = filtered_data["Emissão de CO2 Diesel (Kg)"].sum()
        total_co2_hibrido = filtered_data["Emissão de CO2 Híbrido (kg)"].sum()
        total_co2_eletrico = filtered_data["Emissão de CO2 Elétrico (kg)"].sum()
        custo_total_diesel = filtered_data["Custo do Combustível Diesel (R$)"].sum()
        custo_total_hibrido = filtered_data["Custo do Combustível Híbrido (R$)"].sum()
        custo_total_eletrico = filtered_data["Custo do Combustível Elétrico (R$)"].sum()

        # Cálculo da economia de combustível e emissões
        economia_hibrido_emissoes = total_co2_diesel - total_co2_hibrido
        economia_eletrico_emissoes = total_co2_diesel - total_co2_eletrico
        economia_custo_hibrido = custo_total_diesel - custo_total_hibrido
        economia_custo_eletrico = custo_total_diesel - custo_total_eletrico


        # Criar 4 colunas
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.markdown(f"<div class='metric-box'><h1>{formatar_brasileiro(total_km)} km</h1><p>Total de Km Rodados</p></div>", unsafe_allow_html=True)

        with col2:
            st.markdown(f"<div class='metric-box'><h1>{formatar_brasileiro(total_co2_diesel)} kg</h1><p>Emissão de CO² Diesel</p></div>", unsafe_allow_html=True)

        with col3:
            st.markdown(f"<div class='metric-box'><h1>{formatar_brasileiro(total_co2_hibrido)} kg</h1><p>Emissão de CO² Híbrido</p></div>", unsafe_allow_html=True)

        with col4:
            st.markdown(f"<div class='metric-box'><h1>{formatar_brasileiro(total_co2_eletrico)} kg</h1><p>Emissão de CO² Elétrico</p></div>", unsafe_allow_html=True)

        st.markdown("---")


        col1, col2 = st.columns(2)

        with col1: 
            st.subheader("Economia de CO² ao escolher:")
            st.markdown(f"**Híbrido:** {formatar_brasileiro(economia_hibrido_emissoes)} kg")
            st.markdown(f"**Elétrico:** {formatar_brasileiro(economia_eletrico_emissoes)} kg")

        with col2:
            st.subheader("Economia R$ ao escolher:")
            st.markdown(f"**Híbrido:** {formatar_brasileiro(economia_custo_hibrido)} R$")     
            st.markdown(f"**Elétrico:** {formatar_brasileiro(economia_custo_eletrico)} R$")   

        st.markdown("---")


        col1, col2 = st.columns(2)

        with col1:
            st.markdown("<h4 style='text-align: center;'>Emissões de CO² por Tipo de Veículo</h2>", unsafe_allow_html=True)            
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.lineplot(data=filtered_data, x="Distância (km)", y="Emissão de CO2 Diesel (Kg)", label="Diesel", ax=ax, marker='o')
            sns.lineplot(data=filtered_data, x="Distância (km)", y="Emissão de CO2 Híbrido (kg)", label="Híbrido", ax=ax, marker='o')
            sns.lineplot(data=filtered_data, x="Distância (km)", y="Emissão de CO2 Elétrico (kg)", label="Elétrico", ax=ax, marker='o')
            ax.set_xlabel("Distância (km)")
            ax.set_ylabel("Emissão de CO² (Kg)")
            
            for i in range(len(filtered_data)):
                ax.text(
                    filtered_data["Distância (km)"].iloc[i], 
                    filtered_data["Emissão de CO2 Diesel (Kg)"].iloc[i], 
                    f'{filtered_data["Emissão de CO2 Diesel (Kg)"].iloc[i]:.2f}', 
                    fontsize=8, ha='center', va='bottom', color='blue'
                )
                ax.text(
                    filtered_data["Distância (km)"].iloc[i], 
                    filtered_data["Emissão de CO2 Híbrido (kg)"].iloc[i], 
                    f'{filtered_data["Emissão de CO2 Híbrido (kg)"].iloc[i]:.2f}', 
                    fontsize=8, ha='center', va='bottom', color='red'
                )
                ax.text(
                    filtered_data["Distância (km)"].iloc[i], 
                    filtered_data["Emissão de CO2 Elétrico (kg)"].iloc[i], 
                    f'{filtered_data["Emissão de CO2 Elétrico (kg)"].iloc[i]:.2f}', 
                    fontsize=8, ha='center', va='bottom', color='green'
                )
            st.pyplot(fig)

        with col2:
        # Gráfico de Boxplot para Emissões de CO2 por Tipo de Veículo
            st.markdown("<h4 style='text-align: center;'>Distribuição das Emissões de CO² por Tipo de Veículo</h2>", unsafe_allow_html=True)
            plt.figure(figsize=(10, 6))
            sns.boxplot(data=filtered_data[["Emissão de CO2 Diesel (Kg)", "Emissão de CO2 Híbrido (kg)", "Emissão de CO2 Elétrico (kg)"]])
            plt.ylabel("Emissão de CO2 (kg)")
            st.pyplot(plt)
    else:
        st.warning("Nenhuma rota encontrada para os critérios selecionados.")


    # Botão para apagar o arquivo CSV
    if st.sidebar.button("Apagar CSV"):
        if os.path.exists("dados_rotas.csv"):
            os.remove("dados_rotas.csv")
            st.sidebar.success("Arquivo 'dados_rotas.csv' apagado com sucesso!")
        else:
            st.sidebar.error("O arquivo 'dados_rotas.csv' não foi encontrado. Por favor, inicie uma nova simulação.")
