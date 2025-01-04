import streamlit as st
from streamlit_folium import st_folium
import pandas as pd
import altair as alt
from utils import calcular_emissao, obter_rotas, geocode_address, create_map, calcular_combustivel_diesel, calcular_custo_combustivel, salvar_dados_em_csv, calcular_combustivel_hibrido, calcular_energia_eletrica, calcular_custo_combustivel_hibrido, calcular_custo_eletrico, calcular_emissao_hibrido, calcular_emissao_eletrico
from styles.styles_calcular import custom_css
from urllib.parse import quote_plus
import locale
from dotenv import load_dotenv
import os

load_dotenv()
google_maps_key = os.getenv("GOOGLE_MAPS_API_KEY")

# Configurar o locale para o formato brasileiro
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def app():
    custom_css()

    # Mostrando a imagem com largura total
    st.image("./assets/topag.png")  

    # Título e outros conteúdos
    st.title("Cálculo de Emissões e Geração de Rotas")
    st.write("Para continuar, vamos precisar de algumas informações, ok?")

    # Inicializar estado da sessão
    if 'rotas' not in st.session_state:
        st.session_state['rotas'] = None
    if 'dados_rotas' not in st.session_state:
        st.session_state['dados_rotas'] = None

    # Entradas de dados
    origem = st.text_input('Endereço de Origem', key='origem_input')
    destino = st.text_input('Endereço de Destino', key='destino_input')
    peso = st.number_input('Peso do Caminhão (Ton)', min_value=0.0, step=0.1, key='peso_input')
    input_preco = st.number_input('Preço do Diesel (R$)', min_value=0.0, step=0.01, key='preco_input')

    # Verificar se o nome e o número de whatsapp já estão no session state
    if 'nome_motorista' not in st.session_state:
        st.session_state['nome_motorista'] = ''
    if 'whatsapp_motorista' not in st.session_state:
        st.session_state['whatsapp_motorista'] = ''

    # Entradas para o nome e WhatsApp do motorista
    nome_motorista = st.text_input("Nome do Motorista", value=st.session_state['nome_motorista'])
    whatsapp_motorista = st.text_input("Número de WhatsApp", value=st.session_state['whatsapp_motorista'])

    # Atualizando o session state com os valores digitados
    st.session_state['nome_motorista'] = nome_motorista
    st.session_state['whatsapp_motorista'] = whatsapp_motorista

    # Adicionar botões lado a lado
    col1, col2, col3, col4 = st.columns([1.8, 5.5, 2, 2])  
    with col1:
        calcular = st.button('Calcular')

    with col2:
        limpar = st.button('Limpar Dados')
    
    with col3:
        salvar = st.button('Salvar Todas as Rotas')

    with col4:
        enviar_rota = st.button('Enviar Rota')

        if enviar_rota:
            if st.session_state.get('rotas') and st.session_state.get('indice_menor_emissao') is not None:
                    melhor_rota = st.session_state['rotas'][st.session_state['indice_menor_emissao']]

                    # Gerar link limpo para Google Maps
                    origem_encoded = quote_plus(origem)
                    destino_encoded = quote_plus(destino)
                    link_melhor_rota = f"https://www.google.com/maps/dir/?api=1&origin={origem_encoded}&destination={destino_encoded}"

                    # Montar a mensagem
                    mensagem = (
                        f"Olá {nome_motorista}, a melhor rota para sua viagem é:\n\n"
                        f"Origem: {origem}\n"
                        f"Destino: {destino}\n"
                        f"Distância: {melhor_rota['distancia']:.2f} km\n"
                        f"Tempo estimado: {melhor_rota['tempo']}\n"
                        f"Emissão de CO2 Diesel: {st.session_state['dados_rotas'][st.session_state['indice_menor_emissao']]['Emissão de CO2 Diesel (Kg)']:.2f} kg\n\n"
                        f"Veja a rota no Google Maps: {link_melhor_rota}"
                    )

                    # Gerar link para WhatsApp
                    mensagem_encoded = quote_plus(mensagem)
                    link_whatsapp = f"https://wa.me/{whatsapp_motorista}?text={mensagem_encoded}"

                    st.markdown(f"[Enviar pelo WhatsApp]({link_whatsapp})", unsafe_allow_html=True)
            else:
                    st.warning("Nenhuma rota disponível para envio.")


    # Lógica para limpar os dados
    if limpar:
        # Limpar variáveis de sessão
        st.session_state.clear()  # Limpa todos os dados armazenados na sessão
        st.success("Todos os dados foram limpos. Insira novas informações para continuar.")

    # Lógica para calcular rotas
    if calcular and origem and destino and peso:
        # Resetar dados anteriores ao iniciar nova consulta
        st.session_state['rotas'] = None
        st.session_state['dados_rotas'] = None

        # Obter novas rotas
        rotas = obter_rotas(origem, destino, google_maps_key)
        if rotas:
            # Garantir que sempre há 3 rotas
            while len(rotas) < 3:
                rotas.append(rotas[-1])  # Duplica a última rota, se necessário
            st.session_state['rotas'] = rotas
        else:
            st.error("Não foi possível obter rotas alternativas.")

    st.markdown("---")

    # Exibir rotas salvas
    if st.session_state.get('rotas'):
        origem_coords = geocode_address(origem)
        destino_coords = geocode_address(destino)

        if not origem_coords or not destino_coords:
            st.error("Inicie uma nova simulação")
        else:
            st.subheader("Resumo das Rotas")
            cols = st.columns(3)  # Sempre criar exatamente 3 colunas para as rotas

            # Calcular métricas se ainda não calculadas
            if not st.session_state['dados_rotas']:
                rotas_data = []
                menor_emissao = float('inf')
                indice_menor_emissao = -1

                for i, rota in enumerate(st.session_state['rotas']):
                    emissao_diesel = calcular_emissao(rota['distancia'], peso)
                    emissao_hibrido = calcular_emissao_hibrido(rota['distancia'], peso)
                    emissao_eletrico = calcular_emissao_eletrico(rota['distancia'], peso)
                    combustivel = calcular_combustivel_diesel(rota['distancia'], peso)
                    custo_combustivel = calcular_custo_combustivel(rota['distancia'], peso, input_preco)
                    custo_hibrido = calcular_combustivel_hibrido(rota['distancia'], peso)
                    custo_eletrico = calcular_energia_eletrica(rota['distancia'], peso)
                    consumo_hibrido = calcular_custo_combustivel_hibrido(rota['distancia'], peso, input_preco)
                    consumo_eletrico = calcular_custo_eletrico(rota['distancia'], peso)

                    # Armazenar a menor emissão de carbono
                    if emissao_diesel < menor_emissao:
                        menor_emissao = emissao_diesel
                        indice_menor_emissao = i

                    rotas_data.append({
                        "Rota": f"Rota {i+1}",
                        "Distância (km)": round(rota['distancia'], 2),
                        "Tempo (h)": rota['tempo'],
                        "Emissão de CO2 Diesel (Kg)": round(emissao_diesel, 2),
                        "Emissão de CO2 Hibrido (kg)": round(emissao_hibrido, 2),
                        "Emissão de CO2 Eletrico (kg)": round(emissao_eletrico, 2),
                        "Combustível (L)": round(combustivel, 2),
                        "Consumo Hibrido (L)": round(consumo_hibrido, 2),
                        "Consumo Eletrico (W/km)": round(consumo_eletrico, 2),
                        "Custo do Combustível (R$)": round(custo_combustivel, 2),
                        "Custo Hibrido (R$)": round(custo_hibrido, 2),
                        "Custo Eletrico (R$)": round(custo_eletrico, 2)
                    })

                st.session_state['dados_rotas'] = rotas_data
                st.session_state['indice_menor_emissao'] = indice_menor_emissao

            # Exibir mapas e métricas
            for i, rota in enumerate(st.session_state['rotas']):
                rotas_data = st.session_state['dados_rotas'][i]
                destaque_classe = "highlight" if i == st.session_state['indice_menor_emissao'] else "no-highlight"
                mapa = create_map(origem_coords, destino_coords, rota['overview_polyline'])
                
                with cols[i]:
                    st.markdown(f"<div class='{destaque_classe}'>", unsafe_allow_html=True)
                    st.markdown(f"<h3>Rota {i+1} {'🏆' if i == st.session_state['indice_menor_emissao'] else ''}</h3>", unsafe_allow_html=True)
                    st_folium(mapa, width=500, key=f"mapa_{i}")

                    st.markdown('<div class="spacing"></div>', unsafe_allow_html=True)
                    st.metric(label="Distância (km)", value=f"{rotas_data['Distância (km)']:.2f} km")
                    st.metric(label="Tempo", value=rotas_data['Tempo (h)'])

                    st.markdown("---")
                    st.caption("Diesel")
                    st.metric(label="Emissão de CO2 Diesel (Kg)", value=f"{rotas_data['Emissão de CO2 Diesel (Kg)']:.2f} kg")
                    st.metric(label="Custo do Combustível (R$)", value=f"R$ {rotas_data['Custo do Combustível (R$)']:.2f}")
                    
                    st.markdown("---")
                    st.caption("Híbrido")
                    st.metric(label="Emissão de CO2 Híbrido (kg)", value=f"{rotas_data['Emissão de CO2 Hibrido (kg)']:.2f} kg")
                    st.metric(label="Custo Híbrido (R$)", value=f"R$ {rotas_data['Custo Hibrido (R$)']:.2f}")
                    
                    st.markdown("---")
                    st.caption("Elétricos")
                    st.metric(label="Emissão de CO2 Elétrico (kg)", value=f"{rotas_data['Emissão de CO2 Eletrico (kg)']:.2f} kg")
                    st.metric(label="Custo Elétrico (R$)", value=f"R$ {rotas_data['Custo Eletrico (R$)']:.2f}")
                    
                    st.markdown("---")
                    st.markdown("</div>", unsafe_allow_html=True)

        if salvar:
            if st.session_state.get('dados_rotas'):
                # Salvar todas as rotas no CSV
                salvar_dados_em_csv(st.session_state['dados_rotas'], origem, destino, peso, input_preco)
                st.success("Dados salvos com sucesso!")
            else:
                st.warning("Nenhum dado para salvar. Calcule as rotas primeiro.")
        
# Instrução para iniciar o app no Streamlit
if __name__ == "__main__":
    app()