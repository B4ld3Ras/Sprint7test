import pandas as pd
import streamlit as st
import plotly.express as px

cars = pd.read_csv('vehicles_us.csv') #leer datos

st.header('Graficos')

hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.histogram(cars, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)
            
            st.write("Diagrama dispersion")
            fig = px.scatter(cars, x="odometer", y="price")
            st.plotly_chart(fig,use_container_width=True)
            
