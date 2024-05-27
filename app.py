import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')  # lendo os dados

st.header('Vendas de carros')  # criando um cabeçalho

# criar uma caixa de seleção
build_histogram = st.checkbox('Criar um histograma')


if build_histogram:  # se a caixa de seleção for selecionada
    st.write('Criando um histograma para a coluna odometer')

if build_histogram:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.histogram(car_data, x="odometer",
                       title='Histograma do Ôdometro dos Veículos')

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

build_graphic = st.checkbox('Criar um gráfico de dispersão')

if build_graphic:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

    # criar um gráfico
    fig2 = px.scatter(car_data, x="odometer", y="price",
                      title='Avaliação de Valor dos Veículos')

    st.plotly_chart(fig2, use_container_width=True)
