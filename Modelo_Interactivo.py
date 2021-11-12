# https://streamlit.io/
# https://docs.streamlit.io/library/api-reference/widgets/st.radio
"""
Modelo Interactivo

Proyecto final Data science

streamlit run Modelo_Interactivo.py

@authors: Maria Ines Vasquez Figueroa, Diana Ximena de Leon Figueroa, Maria Jose Castro Lemus, Paula Camila Gonzalez Ortega
"""

# Importar librerías

import numpy as np
import pandas as pd

import streamlit as st

from tensorflow.keras.models import load_model
import joblib


modelo_cc = joblib.load("modelo_final_cc.h5")
escalador_cc = joblib.load("escalador_cc.pkl")

def devuelve_prediccion(modelo, escalador, muestra_json):
    
    caracteristicas = ['age', 'pay_sep_1', 'pay_sep_2', 'pay_sep_3', 'pay_sep_4', 'pay_sep_5',
       'pay_sep_6', 'pay_sep_7', 'pay_sep_8', 'pay_ago_0', 'pay_ago_1',
       'pay_ago_2', 'pay_ago_3', 'pay_ago_4', 'pay_ago_5', 'pay_ago_6',
       'pay_ago_7', 'pay_ago_8', 'pay_jul_0', 'pay_jul_1', 'pay_jul_2',
       'pay_jul_3', 'pay_jul_4', 'pay_jul_5', 'pay_jul_6', 'pay_jul_7',
       'pay_jul_8', 'pay_jun_1', 'pay_jun_2', 'pay_jun_3', 'pay_jun_4',
       'pay_jun_5', 'pay_jun_6', 'pay_jun_7', 'pay_jun_8', 'pay_may_2',
       'pay_may_3', 'pay_may_4', 'pay_may_5', 'pay_may_6', 'pay_may_7',
       'pay_may_8', 'pay_apr_2', 'pay_apr_3', 'pay_apr_4', 'pay_apr_5',
       'pay_apr_6', 'pay_apr_7', 'pay_apr_8', 'pay_amt_may','pay_amt_jun']
    
    data = []
    for i in caracteristicas:
        data.append(muestra_json[i])
    
    cliente = [data]
    cliente = escalador.transform(cliente)
    
    clases = np.array([0,1])

    
    clase_ind = np.argmax(modelo.predict(cliente), axis=-1)
    
    return clases[clase_ind]


def aceptar_datos_usuario():	
    age = st.number_input("Ingrese la edad: ")
    
    #st.write("\nLlene los siguientes datos con 1 para 'si' y  0 para 'no':")

    original_title = "<p style='color:Blue; font-size: 15px; font-weight:bold'>Llene los siguientes datos con 1 para 'si' y  0 para 'no'</p>"
    st.write(" ")
    st.markdown(original_title, unsafe_allow_html=True)

    pay_sep_1 = st.number_input("Estado de reembolso en septiembre de 2005 (1 mes de atraso): ")
    pay_sep_2 = st.number_input("Estado de reembolso en septiembre de 2005 (2 meses de atraso): ")
    pay_sep_3 = st.number_input("Estado de reembolso en septiembre de 2005 (3 meses de atraso): ")
    pay_sep_4 = st.number_input("Estado de reembolso en septiembre de 2005 (4 meses de atraso): ")
    pay_sep_5 = st.number_input("Estado de reembolso en septiembre de 2005 (5 meses de atraso): ")
    pay_sep_6 = st.number_input("Estado de reembolso en septiembre de 2005 (6 meses de atraso): ")
    pay_sep_7 = st.number_input("Estado de reembolso en septiembre de 2005 (7 meses de atraso): ")
    pay_sep_8 = st.number_input("Estado de reembolso en septiembre de 2005 (8 meses de atraso): ")
    
    pay_ago_0 = st.number_input("Estado de reembolso en agosto de 2005 (pagado sin atraso): ")
    pay_ago_1 = st.number_input("Estado de reembolso en agosto de 2005 (1 mes de atraso): ")
    pay_ago_2 = st.number_input("Estado de reembolso en agosto de 2005 (2 meses de atraso): ")
    pay_ago_3 = st.number_input("Estado de reembolso en agosto de 2005 (3 meses de atraso): ")
    pay_ago_4 = st.number_input("Estado de reembolso en agosto de 2005 (4 meses de atraso): ")
    pay_ago_5 = st.number_input("Estado de reembolso en agosto de 2005 (5 meses de atraso): ")
    pay_ago_6 = st.number_input("Estado de reembolso en agosto de 2005 (6 meses de atraso): ")
    pay_ago_7 = st.number_input("Estado de reembolso en agosto de 2005 (7 meses de atraso): ")
    pay_ago_8 = st.number_input("Estado de reembolso en agosto de 2005 (8 meses de atraso): ")

    pay_jul_0 = st.number_input("Estado de reembolso en julio de 2005 (pagado sin atraso): ")
    pay_jul_1 = st.number_input("Estado de reembolso en julio de 2005 (1 mes de atraso): ")
    pay_jul_2 = st.number_input("Estado de reembolso en julio de 2005 (2 meses de atraso): ")
    pay_jul_3 = st.number_input("Estado de reembolso en julio de 2005 (3 meses de atraso): ")
    pay_jul_4 = st.number_input("Estado de reembolso en julio de 2005 (4 meses de atraso): ")
    pay_jul_5 = st.number_input("Estado de reembolso en julio de 2005 (5 meses de atraso): ")
    pay_jul_6 = st.number_input("Estado de reembolso en julio de 2005 (6 meses de atraso): ")
    pay_jul_7 = st.number_input("Estado de reembolso en julio de 2005 (7 meses de atraso): ")
    pay_jul_8 = st.number_input("Estado de reembolso en julio de 2005 (8 meses de atraso): ")

    pay_jun_1 = st.number_input("Estado de reembolso en junio de 2005 (1 mes de atraso): ")
    pay_jun_2 = st.number_input("Estado de reembolso en junio de 2005 (2 meses de atraso): ")
    pay_jun_3 = st.number_input("Estado de reembolso en junio de 2005 (3 meses de atraso): ")
    pay_jun_4 = st.number_input("Estado de reembolso en junio de 2005 (4 meses de atraso): ")
    pay_jun_5 = st.number_input("Estado de reembolso en junio de 2005 (5 meses de atraso): ")
    pay_jun_6 = st.number_input("Estado de reembolso en junio de 2005 (6 meses de atraso): ")
    pay_jun_7 = st.number_input("Estado de reembolso en junio de 2005 (7 meses de atraso): ")
    pay_jun_8 = st.number_input("Estado de reembolso en junio de 2005 (8 meses de atraso): ")

    pay_may_2 = st.number_input("Estado de reembolso en mayo de 2005 (2 meses de atraso): ")
    pay_may_3 = st.number_input("Estado de reembolso en mayo de 2005 (3 meses de atraso): ")
    pay_may_4 = st.number_input("Estado de reembolso en mayo de 2005 (4 meses de atraso): ")
    pay_may_5 = st.number_input("Estado de reembolso en mayo de 2005 (5 meses de atraso): ")
    pay_may_6 = st.number_input("Estado de reembolso en mayo de 2005 (6 meses de atraso): ")
    pay_may_7 = st.number_input("Estado de reembolso en mayo de 2005 (7 meses de atraso): ")
    pay_may_8 = st.number_input("Estado de reembolso en mayo de 2005 (8 meses de atraso): ")
    
    pay_apr_2 = st.number_input("Estado de reembolso en abril de 2005 (2 meses de atraso): ")
    pay_apr_3 = st.number_input("Estado de reembolso en abril de 2005 (3 meses de atraso): ")
    pay_apr_4 = st.number_input("Estado de reembolso en abril de 2005 (4 meses de atraso): ")
    pay_apr_5 = st.number_input("Estado de reembolso en abril de 2005 (5 meses de atraso): ")
    pay_apr_6 = st.number_input("Estado de reembolso en abril de 2005 (6 meses de atraso): ")
    pay_apr_7 = st.number_input("Estado de reembolso en abril de 2005 (7 meses de atraso): ")
    pay_apr_8 = st.number_input("Estado de reembolso en abril de 2005 (8 meses de atraso): ")
    
    
    original_title = "<p style='color:Blue; font-size: 15px; font-weight:bold'>Llene los siguientes datos con el valor en dolares:</p>"
    #st.write("\nLlene los siguientes datos con el valor en dolares':")
    st.write(" ")
    st.markdown(original_title, unsafe_allow_html=True)
    pay_amt_may = st.number_input("Ingrese el monto de la factura en mayo de 2005: ")
    pay_amt_jun = st.number_input("Ingrese el monto de la factura en junio de 2005: ")
    
    
    datos_cliente = {'age':age, 'pay_sep_1':pay_sep_1, 'pay_sep_2':pay_sep_2, 'pay_sep_3':pay_sep_3, 'pay_sep_4':pay_sep_4, 
       'pay_sep_5':pay_sep_5, 'pay_sep_6':pay_sep_6, 'pay_sep_7':pay_sep_7, 'pay_sep_8':pay_sep_8, 
       'pay_ago_0':pay_ago_0, 'pay_ago_1':pay_ago_1, 'pay_ago_2':pay_ago_2, 'pay_ago_3':pay_ago_3, 'pay_ago_4':pay_ago_4,
       'pay_ago_5':pay_ago_5, 'pay_ago_6':pay_ago_6, 'pay_ago_7':pay_ago_7, 'pay_ago_8':pay_ago_8, 'pay_jul_0':pay_jul_0, 
       'pay_jul_1':pay_jul_1, 'pay_jul_2':pay_jul_2, 'pay_jul_3':pay_jul_3, 'pay_jul_4':pay_jul_4, 'pay_jul_5':pay_jul_5,
       'pay_jul_6':pay_jul_6, 'pay_jul_7':pay_jul_7, 'pay_jul_8':pay_jul_8, 'pay_jun_1':pay_jun_1, 'pay_jun_2':pay_jun_2, 
       'pay_jun_3':pay_jun_3, 'pay_jun_4':pay_jun_4, 'pay_jun_5':pay_jun_5, 'pay_jun_6':pay_jun_6, 'pay_jun_7':pay_jun_7,
       'pay_jun_8':pay_jun_8, 'pay_may_2':pay_may_2, 'pay_may_3':pay_may_3, 'pay_may_4':pay_may_4, 'pay_may_5':pay_may_5, 
       'pay_may_6':pay_may_6, 'pay_may_7':pay_may_7, 'pay_may_8':pay_may_8, 'pay_apr_2':pay_apr_2, 'pay_apr_3':pay_apr_3, 
       'pay_apr_4':pay_apr_4, 'pay_apr_5':pay_apr_5, 'pay_apr_6':pay_apr_6, 'pay_apr_7':pay_apr_7, 'pay_apr_8':pay_apr_8, 
       'pay_amt_may':pay_amt_may, 'pay_amt_jun':pay_amt_jun    }
    
    return datos_cliente


# Funciones básicas para nombrar y describir el dashboard


st.title("Predicción de pago de tarjeta de crédito")
st.sidebar.image('./header.jpeg', width = 300)
st.sidebar.write( '''Esta página es parte del proyecto 2 de DS y consiste en un modelo SVM
   para predecir si el cliente tendrá un incumplimiento de pago al mes siguiente
   dadas su historial de pago y edad
''')


# Aceptar los datos del usuario para predecir el pago del proximo año
datos_cliente = aceptar_datos_usuario()

# Pasar los datos al modelo para que lo clasifique
    
resultado = devuelve_prediccion(modelo_cc,
                    escalador_cc,
                    datos_cliente)

if(resultado==0):
    pred = 'NO tendra incumplimiento de pago al mes siguiente'
else:
    pred = 'SI tendra incumplimiento de pago al mes siguiente'
# Desplegar los datos y el resultado
st.write(" ")
original_title = "<p style='color:Purple; font-size: 15px; font-weight:bold'>Segun los datos ingresados...</p>"
#st.write("\nLlene los siguientes datos con el valor en dolares':")
st.write(" ")
st.markdown(original_title, unsafe_allow_html=True)

#st.text("Segun los datos ingresados:  \n")
st.text(f"El cliente {pred}")
 

