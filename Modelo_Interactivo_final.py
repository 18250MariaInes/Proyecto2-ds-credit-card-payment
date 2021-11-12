# https://streamlit.io/
# https://docs.streamlit.io/library/api-reference/widgets/st.radio
"""
Modelo Interactivo

Proyecto final Data science

streamlit run Modelo_Interactivo_final.py

@authors: Maria Ines Vasquez Figueroa, Diana Ximena de Leon Figueroa, Maria Jose Castro Lemus, Paula Camila Gonzalez Ortega
"""

# Importar librerías

import numpy as np
import pandas as pd
import random
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
    
    clases = np.array(['0','1'])

    
    clase_ind = np.argmax(modelo.predict(cliente), axis=-1)
    
    print('RESULTADO',[clase_ind])
    return clases[clase_ind][0]


def aceptar_datos_usuario():	
    age = st.number_input("Ingrese la edad: ")
    
    #st.write("\nLlene los siguientes datos con 1 para 'si' y  0 para 'no':")

    original_title = "<p style='color:Blue; font-size: 15px; font-weight:bold'>Selecciona los datos segun los pagos realizados</p>"
    st.write(" ")
    st.markdown(original_title, unsafe_allow_html=True)

    sept = st.radio(
        "¿Con cuantos meses de atraso pagó septiembre de 2005?",
        (0, 1, 2, 3, 4, 5, 6, 7, 8))
    if sept == 0:
        pay_sep_1 = 0
        pay_sep_2, pay_sep_3, pay_sep_4, pay_sep_5, pay_sep_6, pay_sep_7, pay_sep_8 = 0, 0, 0, 0, 0, 0, 0
    elif sept == 1:
        pay_sep_1 = 1
        pay_sep_2, pay_sep_3, pay_sep_4, pay_sep_5, pay_sep_6, pay_sep_7, pay_sep_8 = 0, 0, 0, 0, 0, 0, 0    
    elif sept == 2:
        pay_sep_2 = 1
        pay_sep_1, pay_sep_3, pay_sep_4, pay_sep_5, pay_sep_6, pay_sep_7, pay_sep_8 = 0, 0, 0, 0, 0, 0, 0  
    elif sept == 3:
        pay_sep_3 = 1
        pay_sep_1, pay_sep_2, pay_sep_4, pay_sep_5, pay_sep_6, pay_sep_7, pay_sep_8 = 0, 0, 0, 0, 0, 0, 0  
    elif sept == 4:
        pay_sep_4 = 1
        pay_sep_1, pay_sep_3, pay_sep_2, pay_sep_5, pay_sep_6, pay_sep_7, pay_sep_8 = 0, 0, 0, 0, 0, 0, 0  
    elif sept == 5:
        pay_sep_5 = 1
        pay_sep_1, pay_sep_3, pay_sep_4, pay_sep_2, pay_sep_6, pay_sep_7, pay_sep_8 = 0, 0, 0, 0, 0, 0, 0  
    elif sept == 6:
        pay_sep_6 = 1
        pay_sep_1, pay_sep_3, pay_sep_4, pay_sep_5, pay_sep_2, pay_sep_7, pay_sep_8 = 0, 0, 0, 0, 0, 0, 0  
    elif sept == 7:
        pay_sep_7 = 1
        pay_sep_1, pay_sep_3, pay_sep_4, pay_sep_5, pay_sep_6, pay_sep_2, pay_sep_8 = 0, 0, 0, 0, 0, 0, 0  
    elif sept == 8:
        pay_sep_8 = 1
        pay_sep_1, pay_sep_3, pay_sep_4, pay_sep_5, pay_sep_6, pay_sep_7, pay_sep_2 = 0, 0, 0, 0, 0, 0, 0  
    else:
        st.write("Debes seleccionar una opcion")


    ago = st.radio(
        "¿Con cuantos meses de atraso pagó agosto de 2005?",
        (0, 1, 2, 3, 4, 5, 6, 7, 8))
    if ago == 0:
        pay_ago_0 = 1
        pay_ago_1, pay_ago_2, pay_ago_3, pay_ago_4, pay_ago_5, pay_ago_6, pay_ago_7, pay_ago_8 = 0, 0, 0, 0, 0, 0, 0, 0    
    elif ago == 1:
        pay_ago_1 = 1
        pay_ago_0, pay_ago_2, pay_ago_3, pay_ago_4, pay_ago_5, pay_ago_6, pay_ago_7, pay_ago_8 = 0, 0, 0, 0, 0, 0, 0, 0  
    elif ago == 2:
        pay_ago_2 = 1
        pay_ago_1, pay_ago_0, pay_ago_3, pay_ago_4, pay_ago_5, pay_ago_6, pay_ago_7, pay_ago_8 = 0, 0, 0, 0, 0, 0, 0, 0  
    elif ago == 3:
        pay_ago_3 = 1
        pay_ago_1, pay_ago_2, pay_ago_0, pay_ago_4, pay_ago_5, pay_ago_6, pay_ago_7, pay_ago_8 = 0, 0, 0, 0, 0, 0, 0, 0  
    elif ago == 4:
        pay_ago_24 = 1
        pay_ago_1, pay_ago_2, pay_ago_3, pay_ago_0, pay_ago_5, pay_ago_6, pay_ago_7, pay_ago_8 = 0, 0, 0, 0, 0, 0, 0, 0 
    elif ago == 5:
        pay_ago_5 = 1
        pay_ago_1, pay_ago_2, pay_ago_3, pay_ago_4, pay_ago_0, pay_ago_6, pay_ago_7, pay_ago_8 = 0, 0, 0, 0, 0, 0, 0, 0 
    elif ago == 6:
        pay_ago_6 = 1
        pay_ago_1, pay_ago_2, pay_ago_3, pay_ago_4, pay_ago_5, pay_ago_0, pay_ago_7, pay_ago_8 = 0, 0, 0, 0, 0, 0, 0, 0 
    elif ago == 7:
        pay_ago_7 = 1
        pay_ago_1, pay_ago_2, pay_ago_3, pay_ago_4, pay_ago_5, pay_ago_6, pay_ago_0, pay_ago_8 = 0, 0, 0, 0, 0, 0, 0, 0  
    elif ago == 8:
        pay_ago_8 = 1
        pay_ago_1, pay_ago_2, pay_ago_3, pay_ago_4, pay_ago_5, pay_ago_6, pay_ago_7, pay_ago_0 = 0, 0, 0, 0, 0, 0, 0, 0
    else:
        st.write("Debes seleccionar una opcion.")

    
    jul = st.radio(
        "¿Con cuantos meses de atraso pagó julio de 2005?",
        (0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    if jul == 0:
        pay_jul_0 = 1
        pay_jul_1, pay_jul_2, pay_jul_3, pay_jul_4, pay_jul_5, pay_jul_6, pay_jul_7, pay_jul_8 = 0, 0, 0, 0, 0, 0, 0, 0    
    elif jul == 1:
        pay_jul_1 = 1
        pay_jul_0, pay_jul_2, pay_jul_3, pay_jul_4, pay_jul_5, pay_jul_6, pay_jul_7, pay_jul_8 = 0, 0, 0, 0, 0, 0, 0, 0  
    elif jul == 2:
        pay_jul_2 = 1
        pay_jul_1, pay_jul_0, pay_jul_3, pay_jul_4, pay_jul_5, pay_jul_6, pay_jul_7, pay_jul_8 = 0, 0, 0, 0, 0, 0, 0, 0  
    elif jul == 3:
        pay_jul_3 = 1
        pay_jul_1, pay_jul_2, pay_jul_0, pay_jul_4, pay_jul_5, pay_jul_6, pay_jul_7, pay_jul_8 = 0, 0, 0, 0, 0, 0, 0, 0  
    elif jul == 4:
        pay_jul_4 = 1
        pay_jul_1, pay_jul_2, pay_jul_3, pay_jul_0, pay_jul_5, pay_jul_6, pay_jul_7, pay_jul_8 = 0, 0, 0, 0, 0, 0, 0, 0 
    elif jul == 5:
        pay_jul_5 = 1
        pay_jul_1, pay_jul_2, pay_jul_3, pay_jul_4, pay_jul_0, pay_jul_6, pay_jul_7, pay_jul_8 = 0, 0, 0, 0, 0, 0, 0, 0 
    elif jul == 6:
        pay_jul_6 = 1
        pay_jul_1, pay_jul_2, pay_jul_3, pay_jul_4, pay_jul_5, pay_jul_0, pay_jul_7, pay_jul_8 = 0, 0, 0, 0, 0, 0, 0, 0 
    elif jul == 7:
        pay_jul_7 = 1
        pay_jul_1, pay_jul_2, pay_jul_3, pay_jul_4, pay_jul_5, pay_jul_6, pay_jul_0, pay_jul_8 = 0, 0, 0, 0, 0, 0, 0, 0 
    elif jul == 8:
        pay_jul_8 = 1
        pay_jul_1, pay_jul_2, pay_jul_3, pay_jul_4, pay_jul_5, pay_jul_6, pay_jul_7, pay_jul_0 = 0, 0, 0, 0, 0, 0, 0, 0
    else:
        st.write("Debes seleccionar una opcion.")

    jun = st.radio(
        "¿Con cuantos meses de atraso pagó junio de 2005?",
        (0, 1, 2, 3, 4, 5, 6, 7, 8))
    if jun == 0:
        pay_jun_1 = 0
        pay_jun_2, pay_jun_3, pay_jun_4, pay_jun_5, pay_jun_6, pay_jun_7, pay_jun_8 = 0, 0, 0, 0, 0, 0, 0
    elif jun == 1:
        pay_jun_1 = 1
        pay_jun_2, pay_jun_3, pay_jun_4, pay_jun_5, pay_jun_6, pay_jun_7, pay_jun_8 = 0, 0, 0, 0, 0, 0, 0 
    elif jun == 2:
        pay_jun_2 = 1
        pay_jun_1, pay_jun_3, pay_jun_4, pay_jun_5, pay_jun_6, pay_jun_7, pay_jun_8 = 0, 0, 0, 0, 0, 0, 0 
    elif jun == 3:
        pay_jun_3 = 1
        pay_jun_1, pay_jun_2, pay_jun_4, pay_jun_5, pay_jun_6, pay_jun_7, pay_jun_8 = 0, 0, 0, 0, 0, 0, 0
    elif jun == 4:
        pay_jun_4 = 1
        pay_jun_1, pay_jun_2, pay_jun_3, pay_jun_5, pay_jun_6, pay_jun_7, pay_jun_8 = 0, 0, 0, 0, 0, 0, 0 
    elif jun == 5:
        pay_jun_5 = 1
        pay_jun_1, pay_jun_2, pay_jun_3, pay_jun_4, pay_jun_6, pay_jun_7, pay_jun_8 = 0, 0, 0, 0, 0, 0, 0 
    elif jun == 6:
        pay_jun_6 = 1
        pay_jun_1, pay_jun_2, pay_jun_3, pay_jun_4, pay_jun_5, pay_jun_7, pay_jun_8 = 0, 0, 0, 0, 0, 0, 0
    elif jun == 7:
        pay_jun_7 = 1
        pay_jun_1, pay_jun_2, pay_jun_3, pay_jun_4, pay_jun_5, pay_jun_6, pay_jun_8 = 0, 0, 0, 0, 0, 0, 0  
    elif jun == 8:
        pay_jun_8 = 1
        pay_jun_1, pay_jun_2, pay_jun_3, pay_jun_4, pay_jun_5, pay_jun_6, pay_jun_7 = 0, 0, 0, 0, 0, 0, 0  
    else:
        st.write("Debes seleccionar una opcion.")

    may = st.radio(
        "¿Con cuantos meses de atraso pagó mayo de 2005?",
        (0, 1, 2, 3, 4, 5, 6, 7, 8))
    if may == 0:
        pay_may_2 = 0
        pay_may_3, pay_may_4, pay_may_5, pay_may_6, pay_may_7, pay_may_8 = 0, 0, 0, 0, 0, 0
    elif may == 1:
        pay_may_2 = 0
        pay_may_3, pay_may_4, pay_may_5, pay_may_6, pay_may_7, pay_may_8 = 0, 0, 0, 0, 0, 0
    elif may == 2:
        pay_may_2 = 1
        pay_may_3, pay_may_4, pay_may_5, pay_may_6, pay_may_7, pay_may_8 = 0, 0, 0, 0, 0, 0 
    elif may == 3:
        pay_may_3 = 1
        pay_may_2, pay_may_4, pay_may_5, pay_may_6, pay_may_7, pay_may_8 = 0, 0, 0, 0, 0, 0
    elif may == 4:
        pay_may_4 = 1
        pay_may_2, pay_may_3, pay_may_5, pay_may_6, pay_may_7, pay_may_8 = 0, 0, 0, 0, 0, 0
    elif may == 5:
        pay_may_5 = 1
        pay_may_2, pay_may_3, pay_may_4, pay_may_6, pay_may_7, pay_may_8 = 0, 0, 0, 0, 0, 0 
    elif may == 6:
        pay_may_6 = 1
        pay_may_2, pay_may_3, pay_may_4, pay_may_5, pay_may_7, pay_may_8 = 0, 0, 0, 0, 0, 0
    elif may == 7:
        pay_may_7 = 1
        pay_may_2, pay_may_3, pay_may_4, pay_may_5, pay_may_6, pay_may_8 = 0, 0, 0, 0, 0, 0
    elif may == 8:
        pay_may_8 = 1
        pay_may_2, pay_may_3, pay_may_4, pay_may_5, pay_may_6, pay_may_7 = 0, 0, 0, 0, 0, 0
    else:
        st.write("Debes seleccionar una opcion.")

    apr = st.radio(
        "¿Con cuantos meses de atraso pagó abril de 2005?",
        (0, 1, 2, 3, 4, 5, 6, 7, 8))
    if apr == 0:
        pay_apr_2 = 0
        pay_apr_3, pay_apr_4, pay_apr_5, pay_apr_6, pay_apr_7, pay_apr_8 = 0, 0, 0, 0, 0, 0
    elif apr == 1:
        pay_apr_2 = 0
        pay_apr_3, pay_apr_4, pay_apr_5, pay_apr_6, pay_apr_7, pay_apr_8 = 0, 0, 0, 0, 0, 0
    elif apr == 2:
        pay_apr_2 = 1
        pay_apr_3, pay_apr_4, pay_apr_5, pay_apr_6, pay_apr_7, pay_apr_8 = 0, 0, 0, 0, 0, 0
    elif apr == 3:
        pay_apr_3 = 1
        pay_apr_2, pay_apr_4, pay_apr_5, pay_apr_6, pay_apr_7, pay_apr_8 = 0, 0, 0, 0, 0, 0
    elif apr == 4:
        pay_apr_4 = 1
        pay_apr_2, pay_apr_3, pay_apr_5, pay_apr_6, pay_apr_7, pay_apr_8 = 0, 0, 0, 0, 0, 0
    elif apr == 5:
        pay_apr_5 = 1
        pay_apr_2, pay_apr_3, pay_apr_4, pay_apr_6, pay_apr_7, pay_apr_8 = 0, 0, 0, 0, 0, 0 
    elif apr == 6:
        pay_apr_6 = 1
        pay_apr_2, pay_apr_3, pay_apr_4, pay_apr_5, pay_apr_7, pay_apr_8 = 0, 0, 0, 0, 0, 0
    elif apr == 7:
        pay_apr_7 = 1
        pay_apr_2, pay_apr_3, pay_apr_4, pay_apr_5, pay_apr_6, pay_apr_8 = 0, 0, 0, 0, 0, 0
    elif apr == 8:
        pay_apr_8 = 1
        pay_apr_2, pay_apr_3, pay_apr_4, pay_apr_5, pay_apr_6, pay_apr_7 = 0, 0, 0, 0, 0, 0
    else:
        st.write("Debes seleccionar una opcion.")
    
    
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
resultado = random.choice([0, 1])
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
 

