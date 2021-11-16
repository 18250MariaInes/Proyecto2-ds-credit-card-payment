# https://streamlit.io/
# https://docs.streamlit.io/library/api-reference/widgets/st.radio
"""
Modelo Interactivo - Proyecto 2

Proyecto final Data science

Para ejecutarlo correr:  streamlit run Modelo_Interactivo_v3.py

@authors: Maria Ines Vasquez Figueroa, Diana Ximena de Leon Figueroa, Maria Jose Castro Lemus, Paula Camila Gonzalez Ortega
"""

# Importar librerías

import numpy as np
import pandas as pd
import random
import streamlit as st

from tensorflow.keras.models import load_model
import joblib

#se carga el modelo y escalador
modelo_cc = joblib.load("modelo_v3.h5")
escalador_cc = joblib.load("escalador_v3.pkl")


def devuelve_prediccion(modelo, escalador, muestra_json):
    #se predice impago o no usando el modelo, escalador y datos ingresados
    
    cliente = [list(muestra_json.values())]
    
    cliente = escalador.transform(cliente)
    
    clases = np.array([0, 1])
    
    clase_ind = modelo.predict(cliente)
    print(modelo.predict(cliente))
    return [clase_ind][0]


def form_user_data():	

    #se piden los datos necesarios para predecir
    st.write(" ")
    original_title = "<p style='color:palevioletred; font-size: 15px; font-weight:bold'>Datos personales</p>"
    st.markdown(original_title, unsafe_allow_html=True)
    st.write(" ")
    limit_bal = st.number_input("Limite Crediticio")

    st.write(" ")
    sex = st.radio(
        "Sexo",
        (['Femenino', 'Masculino']))
    if sex == 'Femenino':
        sex_male = 0
    else:
        sex_male = 1
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

    age = st.radio(
        "Selecciona el rango de tu edad",
        (['20-30','30-40', '40-50', '50-60', '60-70']))
    if age == '20-30':
        age_30_40 = 0
        age_40_50 = 0
        age_50_60 = 0
        age_60_70 = 0
        age_70_death = 0
    elif age == '30-40':
        age_30_40 = 1
        age_40_50 = 0
        age_50_60 = 0
        age_60_70 = 0
        age_70_death = 0
    elif age == '40-50':
        age_30_40 = 0
        age_40_50 = 1
        age_50_60 = 0
        age_60_70 = 0
        age_70_death = 0
    elif age == '50-60':
        age_30_40 = 0
        age_40_50 = 0
        age_50_60 = 1
        age_60_70 = 0
        age_70_death = 0
    elif age == '60-70':
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


    original_title = "<p style='color:lime; font-size: 15px; font-weight:bold'>Ingresa los meses atrasados</p>"
    st.markdown(original_title, unsafe_allow_html=True)
    st.write(" ")
    pay_0 = st.number_input("Cantidad de meses atrasado en septiembre: ")
    pay_2 = st.number_input("Cantidad de meses atrasado en agosto: ")
    pay_3 = st.number_input("Cantidad de meses atrasado en julio: ")
    pay_4 = st.number_input("Cantidad de meses atrasado en junio: ")
    pay_5 = st.number_input("Cantidad de meses atrasado en mayo: ")
    pay_6 = st.number_input("Cantidad de meses atrasado en abril: ")
    total_pay = pay_0 + pay_2 + pay_3 + pay_4 + pay_5 + pay_6
    
    st.write(" ")
    original_title = "<p style='color:turquoise; font-size: 15px; font-weight:bold'>Ingresa los montos de factura</p>"
    st.markdown(original_title, unsafe_allow_html=True)
    bill_amt_1 = st.number_input("Monto de la factura en septiembre: ")
    bill_amt_2 = st.number_input("Monto de la factura en agosto: ")
    bill_amt_3 = st.number_input("Monto de la factura en julio: ")
    bill_amt_4 = st.number_input("Monto de la factura en junio: ")
    bill_amt_5 = st.number_input("Monto de la factura en mayo: ")
    bill_amt_6 = st.number_input("Monto de la factura en abril: ")
    total_bill_amt = bill_amt_1 + bill_amt_2 + bill_amt_3 + bill_amt_4 + bill_amt_5 + bill_amt_6
    
    st.write(" ")
    original_title = "<p style='color:palevioletred; font-size: 15px; font-weight:bold'>Ingresa los montos de pagos anteriores</p>"
    st.markdown(original_title, unsafe_allow_html=True)
    pay_amt_1 = st.number_input("Monto del pago anterior en septiembre: ")
    pay_amt_2 = st.number_input("Monto del pago anterior en agosto: ")
    pay_amt_3 = st.number_input("Monto del pago anterior en julio: ")
    pay_amt_4 = st.number_input("Monto del pago anterior en junio: ")
    pay_amt_5 = st.number_input("Monto del pago anterior en mayo: ")
    pay_amt_6 = st.number_input("Monto del pago anterior en abril: ")
    total_pay_amt = pay_amt_1 + pay_amt_2 + pay_amt_3 + pay_amt_4 + pay_amt_5 + pay_amt_6

    ## comienzan los calculos internos para pasarselos como datos del cliente para el modelo
    percentage_paid = float(total_pay_amt / total_bill_amt)
    avg_bill_cl = float(total_bill_amt / 6 )
    avg_bill_cl = float(avg_bill_cl / limit_bal)
    print(avg_bill_cl)
    avg_pay_cl = float(total_pay_amt / 6 / limit_bal)
    num_delays = (
                    (1 if pay_0 > 0 else 0) + \
                    (1 if pay_2 > 0 else 0) + \
                    (1 if pay_3 > 0 else 0) + \
                    (1 if pay_4 > 0 else 0) + \
                    (1 if pay_5 > 0 else 0) + \
                    (1 if pay_6 > 0 else 0) \
                )

    bill_change_sep = float(bill_amt_1 - bill_amt_2 / limit_bal)
    bill_change_ago = float(bill_amt_2 - bill_amt_3 / limit_bal)
    bill_change_jul = float(bill_amt_3 - bill_amt_4 / limit_bal)
    bill_change_jun = float(bill_amt_4 - bill_amt_5 / limit_bal)
    bill_change_may = float(bill_amt_5 - bill_amt_6 / limit_bal)
    
    pay_change_sep = float(pay_amt_1 - pay_amt_2 / limit_bal)
    pay_change_ago = float(pay_amt_2 - pay_amt_3 / limit_bal)
    pay_change_jul = float(pay_amt_3 - pay_amt_4 / limit_bal)
    pay_change_jun = float(pay_amt_4 - pay_amt_5 / limit_bal)
    pay_change_may = float(pay_amt_5 - pay_amt_6 / limit_bal)
    
    if num_delays >= 1:
        cur_delay = 1
    else:
        cur_delay = 0

    if limit_bal >= 9999.99 and limit_bal < 80000.0:
        limit_bal_9999 = 1
        limit_bal_80000 = 0
    elif limit_bal >= 80000.0 and limit_bal < 200000.0:
        limit_bal_9999 = 0
        limit_bal_80000 = 1
    elif limit_bal >= 200000.0 and limit_bal < 10000000.0:
        limit_bal_9999 = 0
        limit_bal_80000 = 0

    #Se crea el diccionario con toda la informacion del cliente 
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
        'limit_bal_(9999.999-80000.0)': limit_bal_9999
        }
    
    # se devuelve el diccionario con la data del cliente
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

#Se evalua el resultado para presentarlo de forma legible al user
if(resultado==0):
    pred = 'NO tendra incumplimiento de pago al mes siguiente'
else:
    pred = 'SI tendra incumplimiento de pago al mes siguiente'

# Desplegar el resultado del a prediccion
st.write(" ")
original_title = "<p style='color:purple; font-size: 15px; font-weight:bold'>Segun los datos ingresados...</p>"
st.write(" ")
st.markdown(original_title, unsafe_allow_html=True)
st.text(f"El cliente {pred}")
 

