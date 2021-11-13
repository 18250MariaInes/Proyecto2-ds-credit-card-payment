#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Graficador interactivo general

streamlit run proyecto_Interactivo.py

@author: Maria Ines Vasquez Figueroa, Diana Ximena de Leon Figueroa, Maria Jose Castro Lemus, Paula Camila Gonzalez Ortega
"""

# Importar librerías

import numpy as np
import pandas as pd
import base64
import datetime
import streamlit as st
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go



def download_link(object_to_download, download_filename, download_link_text):
    """
    Generates a link to download the given object_to_download.

    object_to_download (str, pd.DataFrame):  The object to be downloaded.
    download_filename (str): filename and extension of file. e.g. mydata.csv, some_txt_output.txt
    download_link_text (str): Text to display for download link.

    Examples:
    download_link(YOUR_DF, 'YOUR_DF.csv', 'Click here to download data!')
    download_link(YOUR_STRING, 'YOUR_STRING.txt', 'Click here to download your text!')
    
    Tomado de:  https://discuss.streamlit.io/t/heres-a-download-function-that-works-for-dataframes-and-txt/4052

    """
    if isinstance(object_to_download,pd.DataFrame):
        object_to_download = object_to_download.to_csv(index=False)

    # some strings <-> bytes conversions necessary here
    b64 = base64.b64encode(object_to_download.encode()).decode()

    return f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{download_link_text}</a>'


# Funciones básicas para nombrar y describir el dashboard


st.title("Acerca del incumplimiento de Credit Card")
st.sidebar.image('./header.jpeg', width = 300)

# Leer el archivo de datos

archivo = st.sidebar.text_input("Ingrese el nombre del archivo de datos .csv")
datos = pd.read_csv(archivo)

#if archivo.endswith((".csv", ".CSV")):
#    datos = pd.read_csv(archivo)
#elif archivo.endswith((".xslx", "XLSX", ".xls", ".XLS")):
#    datos = pd.read_excel(archivo, sheet_name=None)



#  Inicializar variables

columnas = list(datos)
 
st.sidebar.subheader("Datos")

# Ver si se desea obtener un subconjunto de los datos

options = ["no", "si"]

sub_conjunto = st.selectbox("Desea trabajar con un sub-conjunto de los datos?", options)
if sub_conjunto == "si":
    campo_filtro = st.selectbox('Seleccione una variable para usar como filtro', options = columnas)
    valores_filtro = datos[campo_filtro].unique()
    valores_sele = st.multiselect('Seleccione uno, o más valores', options = valores_filtro)
    mask_valores = datos[campo_filtro].isin(valores_sele)

    datos_uso = datos[mask_valores]
    
else:
    datos_uso = datos.copy()
    campo_filtro = []
    valores_sele = []

#  Dar las opciones a seleccionar

#  Dar la opción a ver y descargar los datos

if st.sidebar.checkbox("Ver datos originales"):
    st.write(datos_uso)
    tmp_download_link = download_link(datos_uso, 'datos_uso.csv', 'Presione acá para descargar los datos!')
    st.markdown(tmp_download_link, unsafe_allow_html=True)





# Sección de generación de gráficas

st.sidebar.subheader("Gráficas interactivas")

if st.sidebar.checkbox("Gráfica de líneas (Line)"):
    st.write("Gráfica de líneas - Seleccione las variables a graficar")
    eje_X = st.selectbox('Seleccione una variable para el eje X', options = columnas)
    eje_Y = st.multiselect('Seleccione una, o más variables - eje Y', options = columnas)
    if campo_filtro != []:
        line_graph = px.line(datos_uso, x = eje_X, y = eje_Y, color = campo_filtro,
                         title = f"{valores_sele} - {eje_Y}",
                         height = 400
                         )
    else:
       line_graph = px.line(datos_uso, x = eje_X, y = eje_Y,
                         title = f"{valores_sele} - {eje_Y}",
                         height = 400
                         ) 
    
    line_graph.update_xaxes(rangeslider_visible=True)
    
    st.plotly_chart(line_graph)
    
    
if st.sidebar.checkbox("Histograma"):
    st.write("Histograma - Selecciones la variable a graficar")
    eje_X = st.selectbox('Variable para el eje X?', options = columnas)
    if campo_filtro != []:
        histo_graph = px.histogram(datos_uso, x = eje_X, color = campo_filtro,
                         title = f"{eje_X} - Conteo",
                         height = 400
                         )
    else:
        histo_graph = px.histogram(datos_uso, x = eje_X,
                         title = f"{eje_X} - Conteo",
                         height = 400
                         )
    
    st.plotly_chart(histo_graph)
    
if st.sidebar.checkbox("Gráfica de barras (Bar)"):
    st.write("Gráfica de barras - Seleccione las variables a graficar")
    eje_X = st.selectbox('Seleccione una variable para el eje X', options = columnas)
    eje_Y = st.multiselect('Seleccione una, o más variables - eje Y', options = columnas)
    if campo_filtro != []:
        bar_graph = px.bar(datos_uso, x = eje_X, y = eje_Y, color = campo_filtro,
                         title = f"{valores_sele} - {eje_Y}",
                         height = 400
                         )
    else:
        bar_graph = px.bar(datos_uso, x = eje_X, y = eje_Y,
                         title = f"{valores_sele} - {eje_Y}",
                         height = 400
                         )
      
    st.plotly_chart(bar_graph)
    
    
  
if  st.sidebar.checkbox("Gráfica de dispersión (Scatter)"):
    st.write("Gráfica de dispersión - Seleccione las variables a graficar")
    eje_X = st.selectbox('Seleccione una variable - eje horizontal', options = columnas) 
    eje_Y = st.selectbox('Seleccione una variable - eje vertical', options = columnas)
    datos_extra = st.multiselect('Seleccione una o más variables - a mostrar por punto', options = columnas)
    if campo_filtro != []:
        scatter_graph = px.scatter(data_frame=datos_uso
                       , x = eje_X
                       , y = eje_Y
                       , hover_data = datos_extra
                       , color = campo_filtro
                       , title = f"{valores_sele} - {eje_Y} vrs {eje_X}"
                       , template='presentation'
                       )
    else:
       scatter_graph = px.scatter(data_frame=datos_uso
                       , x = eje_X
                       , y = eje_Y
                       , title = f"{valores_sele} - {eje_Y} vrs {eje_X}"
                       , template='presentation'
                       ) 

    st.plotly_chart(scatter_graph)
    
      


if  st.sidebar.checkbox("Gráfica de cajas (Box)"):
    st.write("Gráfica de cajas - Seleccione las variables a graficar")    
    eje_Y = st.selectbox('Seleccione una variable', options = columnas)        
    box_graph = px.box(data_frame=datos_uso
                       , x = campo_filtro
                       , y = eje_Y
                       , notched = True
                       , title = f"Distribución de {eje_Y}"
                       , template='presentation'
                       )

    st.plotly_chart(box_graph)
    
    
    
  

