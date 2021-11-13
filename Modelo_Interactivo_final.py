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

modelo_cc = load_model("modelo_rna.h5")
escalador_cc = joblib.load("escalador_rna.pkl") 


def devuelve_prediccion(modelo, escalador, muestra_json):
    
    #caracteristicas = ['age', 'months_late', 'pay_amt_may','']
    # se leen las caracteristicas ingresadas y se agregan a la info del cliente
    age = muestra_json['age']
    months_late = muestra_json['months_late']
    pay_amt_may = muestra_json['pay_amt_may']
    pay_amt_jun = muestra_json['pay_amt_jun']
    
    cliente = [[age, months_late,
             pay_amt_may, pay_amt_jun]]

    #data = []
    #for i in caracteristicas:
    #    data.append(muestra_json[i])
    
    #cliente = [data]
    cliente = escalador.transform(cliente)
    
    clases = np.array([0,1])

    
    clase_ind = np.argmax(modelo.predict(cliente), axis=-1)
    
    #print('RESULTADO',[clase_ind])
    return clases[clase_ind][0]


def form_user_data():	

    #se piden los datos necesarios para predecir
    age = st.number_input("Ingrese la edad: ")

    original_title = "<p style='color:Blue; font-size: 15px; font-weight:bold'>Selecciona los datos segun los pagos realizados</p>"
    st.write(" ")
    st.markdown(original_title, unsafe_allow_html=True)

    months = st.radio(
        "¿Meses de atraso en pago?",
        (0, 1, 2, 3, 4, 5, 6, 7, 8))
    if months == 0:
        months_late = 0
    elif months == 1:
        months_late = 1
    elif months == 2:
        months_late = 2
    elif months == 3:
        months_late = 3
    elif months == 4:
        months_late = 4
    elif months == 5:
        months_late = 5
    elif months == 6:
        months_late = 6
    elif months == 7:
        months_late = 7
    elif months == 8:
        months_late = 8
    else:
        st.write("Debes seleccionar una opcion")
    
    
    original_title = "<p style='color:Blue; font-size: 15px; font-weight:bold'>Llene los siguientes datos con el valor en dolares:</p>"
    st.write(" ")
    st.markdown(original_title, unsafe_allow_html=True)
    pay_amt_may = st.number_input("Ingrese el monto de la factura en mayo de 2005: ")
    pay_amt_jun = st.number_input("Ingrese el monto de la factura en junio de 2005: ")
    
    
    datos_cliente = {'age':age, 'months_late':months_late, 'pay_amt_may':pay_amt_may, 'pay_amt_jun':pay_amt_jun    }
    
    return datos_cliente


# Descripcion y decoracion del dashboard
st.title("Predicción de pago de tarjeta de crédito")
st.sidebar.image('./header.jpeg', width = 300)
st.sidebar.write( '''Esta página es parte del proyecto 2 de DS y consiste en un modelo SVM
   para predecir si el cliente tendrá un incumplimiento de pago al mes siguiente
   dadas su historial de pago y edad
''')


# Se piden y aceptar los datos del usuario para predecir el pago del proximo año
datos_cliente = form_user_data()

# Se ejecuta modelo con los datos para que haga la prediccion
resultado = devuelve_prediccion(modelo_cc,
                    escalador_cc,
                    datos_cliente)

#resultado = random.choice([0, 1])

if(resultado==0):
    pred = 'NO tendra incumplimiento de pago al mes siguiente'
else:
    pred = 'SI tendra incumplimiento de pago al mes siguiente'

# Desplegar el resultado del a prediccion
st.write(" ")
original_title = "<p style='color:Purple; font-size: 15px; font-weight:bold'>Segun los datos ingresados...</p>"
st.write(" ")
st.markdown(original_title, unsafe_allow_html=True)
st.text(f"El cliente {pred}")
 

