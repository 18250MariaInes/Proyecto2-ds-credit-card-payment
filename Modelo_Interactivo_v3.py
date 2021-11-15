# https://streamlit.io/
# https://docs.streamlit.io/library/api-reference/widgets/st.radio
"""
Modelo Interactivo

Proyecto final Data science

streamlit run Modelo_Interactivo_v3.py

@authors: Maria Ines Vasquez Figueroa, Diana Ximena de Leon Figueroa, Maria Jose Castro Lemus, Paula Camila Gonzalez Ortega
"""

# Importar librerías

import numpy as np
import pandas as pd
import random
import streamlit as st

from tensorflow.keras.models import load_model
import joblib

modelo_cc = joblib.load("modelo_v3.h5")
escalador_cc = joblib.load("escalador_v3.pkl")


def devuelve_prediccion(modelo, escalador, muestra_json):
    
    
    cliente = [list(muestra_json.values())]
    
    cliente = escalador.transform(cliente)
    
    clases = np.array([0, 1])
    
    #clase_ind = np.argmax(modelo.predict(cliente), axis=-1)
    clase_ind = modelo.predict(cliente)
    print(modelo.predict(cliente))
    return [clase_ind][0]


def form_user_data():	

    #se piden los datos necesarios para predecir
    percentage_paid = st.number_input("percentage paid: ")
    avg_bill_cl = st.number_input("average bill: ")
    avg_pay_cl = st.number_input("average pay: ")
    num_delays = st.number_input("Dias de atraso: ")
    st.write(" ")
    bill_change_sep = st.number_input("bill change septiembre: ")
    bill_change_ago = st.number_input("bill change agosto: ")
    bill_change_jul = st.number_input("bill change julio: ")
    bill_change_jun = st.number_input("bill change junio: ")
    bill_change_may = st.number_input("bill change mayo: ")
    st.write(" ")
    pay_change_sep = st.number_input("pay change septiembre: ")
    pay_change_ago = st.number_input("pay change agosto: ")
    pay_change_jul = st.number_input("pay change julio: ")
    pay_change_jun = st.number_input("pay change junio: ")
    pay_change_may = st.number_input("pay change mayo: ")
    st.write(" ")
    cur_delay = st.number_input("atraso actual: ")
    #original_title = "<p style='color:Blue; font-size: 15px; font-weight:bold'>Selecciona los datos segun los pagos realizados</p>"
    st.write(" ")
    #st.markdown(original_title, unsafe_allow_html=True)
    sex = st.radio(
        "Sexo",
        (['Femenino', 'Masculino']))
    if sex == 'Femenino':
        sex_male = 0
    else:
        sex_male = 1
    st.write(" ")

    marriage = st.radio(
        "Estado Civil",
        (['Casad@', 'Solter@', 'Otro']))
    if marriage == 'Casad@':
        marriage_others = 0
        marriage_single = 0
    elif marriage == 'Solter@':
        marriage_others = 0
        marriage_single = 1
    else:
        marriage_others = 1
        marriage_single = 0
    st.write(" ")
    education = st.radio(
        "Educacion",
        (['Media', 'Superior', 'Otra', 'Desconocida']))
    if education == 'Media@':
        education_highschool = 1
        education_others = 0
        education_undergraduate = 0
        education_unknown = 0
    elif education == 'Superior':
        education_highschool = 0
        education_others = 0
        education_undergraduate = 1
        education_unknown = 0
    elif education == 'Otra':
        education_highschool = 0
        education_others = 1
        education_undergraduate = 0
        education_unknown = 0
    else:
        education_highschool = 0
        education_others = 0
        education_undergraduate = 0
        education_unknown = 1
    st.write(" ")
    Edad = st.radio(
        "Selecciona el rango de tu edad",
        (['20-30','30-40', '40-50', '50-60', '60-70']))
    if education == '20-30':
        age_30_40 = 0
        age_40_50 = 0
        age_50_60 = 0
        age_60_70 = 0
        age_70_death = 0
    elif education == '30-40':
        age_30_40 = 1
        age_40_50 = 0
        age_50_60 = 0
        age_60_70 = 0
        age_70_death = 0
    elif education == '40-50':
        age_30_40 = 0
        age_40_50 = 1
        age_50_60 = 0
        age_60_70 = 0
        age_70_death = 0
    elif education == '50-60':
        age_30_40 = 0
        age_40_50 = 0
        age_50_60 = 1
        age_60_70 = 0
        age_70_death = 0
    elif education == '60-70':
        age_30_40 = 0
        age_40_50 = 0
        age_50_60 = 0
        age_60_70 = 1
        age_70_death = 0
    else:
        age_30_40 = 0
        age_40_50 = 0
        age_50_60 = 0
        age_60_70 = 0
        age_70_death = 1
    
    st.write(" ")
    #st.markdown(original_title, unsafe_allow_html=True)
    limit_bal = st.radio(
        "Selecciona el rango de tu balance limite",
        (['80000.0-200000.0', '9999.999-80000.0']))
    if limit_bal == '80000.0-200000.0':
        limit_bal_80000 = 1
        limit_bal_9999 = 0
    else:
        limit_bal_80000 = 0
        limit_bal_9999 = 1
    st.write(" ")
    
    
    #original_title = "<p style='color:Blue; font-size: 15px; font-weight:bold'>Llene los siguientes datos con el valor en dolares:</p>"
    #st.write(" ")
    #st.markdown(original_title, unsafe_allow_html=True)
    #pay_amt_may = st.number_input("Ingrese el monto de la factura en mayo de 2005: ")
    #pay_amt_jun = st.number_input("Ingrese el monto de la factura en junio de 2005: ")
    
    
    datos_cliente = {
        'percentage_paid': percentage_paid, 
        'avg_bill_cl': avg_bill_cl, 
        'avg_pay_cl': avg_pay_cl, 
        'num_delays': num_delays,
       'bill_change_sep': bill_change_sep, 
        'bill_change_ago': bill_change_ago, 
        'bill_change_jul': bill_change_jul,
       'bill_change_jun': bill_change_jun, 
        'bill_change_may': bill_change_may, 
        'pay_change_sep': pay_change_sep,
       'pay_change_ago': pay_change_ago, 
        'pay_change_jul': pay_change_jul, 
        'pay_change_jun': pay_change_jun, 
        'pay_change_may': pay_change_may,
        'cur_delay': cur_delay, 
        'sex_male': sex_male, 
        'marriage_others': marriage_others,
       'marriage_single': marriage_single, 
        'education_highschool': education_highschool, 
        'education_others': education_others,
       'education_undergraduate': education_undergraduate, 
        'education_unknown': education_unknown, 
        'age_(30-40)': age_30_40,
       'age_(40-50)': age_40_50, 
        'age_(50-60)': age_50_60, 
        'age_(60-70)': age_60_70, 
        'age_(70-death)': age_70_death,
       'limit_bal_(80000.0-200000.0)': limit_bal_80000, 
        'limit_bal_(9999.999-80000.0)': limit_bal_9999}
    
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

print("RESULTADO:" ,resultado)
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
 

