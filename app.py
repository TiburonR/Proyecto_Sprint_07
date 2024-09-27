import streamlit as st      # Importa Streamlit y lo llama "st" para abreviar
import pandas as pd         # Importa Pandas y lo llama "pd" para abreviar
import plotly.express as px # Importa Plotly Express y lo llama "px" para abreviar

car_data = pd.read_csv('vehicles_us.csv')

st.header('Análisis de Datos de Vehículos')

# Casilla para el histograma
show_histogram = st.checkbox('Mostrar Histograma de Kilometraje')
if show_histogram:
    st.write("Histograma de Kilometraje de los Vehículos")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig)

# Casilla para el gráfico de dispersión
show_scatter = st.checkbox('Mostrar Gráfico de Dispersión: Precio vs. Año')
if show_scatter:
    st.write("Gráfico de Dispersión: Precio vs. Año de los Vehículos")
    fig = px.scatter(car_data, x="model_year", y="price")
    st.plotly_chart(fig)