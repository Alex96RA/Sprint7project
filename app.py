import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.title('Proyecto Sprint 7')#

# Inicializa los valores si no existen
if "hist_check" not in st.session_state:
    st.session_state.hist_check = False
if "disp_check" not in st.session_state:
    st.session_state.disp_check = False

# Mostrar los checkbox y capturar su estado actual
hist_check = st.checkbox('Histograma', value=st.session_state.hist_check)
disp_check = st.checkbox('Diagrama de dispersión', value=st.session_state.disp_check)

if hist_check and not st.session_state.hist_check:
    st.session_state.hist_check = True
    st.session_state.disp_check = False
elif disp_check and not st.session_state.disp_check:
    st.session_state.disp_check = True
    st.session_state.hist_check = False

gen_button = st.button('Construir gráfico') # crear un botón

if st.session_state.hist_check:
    st.header('Histograma')
    if gen_button: # al hacer clic en el botón
        # escribir un mensaje
        st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
        # crear un histograma
        fig = px.histogram(car_data, x="odometer")
        # mostrar un gráfico Plotly interactivo
        st.plotly_chart(fig, use_container_width=True)

elif st.session_state.disp_check:
    st.header('Diagrama de dispersión')
    if gen_button: # al hacer clic en el botón
        # escribir un mensaje
        st.write('Creación de un gráfico de dispersión entre de para el conjunto de datos de anuncios de venta de coches')
        # crear un gráfico de dispersión
        fig = px.scatter(car_data, x="odometer", y="price")
        # mostrar un gráfico Plotly interactivo
        st.plotly_chart(fig, use_container_width=True)
else:
    st.write('Selecciona el gráfico que deseas')

