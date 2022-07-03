# importar librearias

import streamlit as st
import pickle
import pandas as pd

# Extraer los archivos pickle

with open('lin_reg.pkl', 'rb') as li:
    lin_reg = pickle.load(li)

with open('log_reg.pkl', 'rb') as lo:
    log_reg = pickle.load(lo)

with open('svc_m.pkl', 'rb') as sv:
    svc_m = pickle.load(sv)

#Función para clasificar las alumnos que aprueban  

def classify(num):
    if num == 0:
        return 'Aprobed'
    elif num == 1:
        return 'Rejected'
    else:
        return 'Retired'

def main():
# titulo
    st.title('Subject approval predictive model')
# titulo del slidebar
    st.sidebar.header('Report Card')
# funcion para poner losparametros
    def user_input_parameters():
        Parcial1 = st.sidebar.slider('Grade 1', 0.0, 5.0 , 0.0)
        Parcial2 = st.sidebar.slider('Grade 2', 0.0, 5.0 , 0.0)

        data = {'Grade 1' : Parcial1,
                'Grade 2' : Parcial1,
                }
        features = pd.DataFrame(data, index=[0])
        return features

    df = user_input_parameters()
# escoger el modelo
    option = ['Linear Regresion', 'Logistic Regresion', 'SVM']
    model = st.sidebar.selectbox('Which model you like to use?', option)

    st.subheader(model)
    st.subheader('User Input parameters')
    st.write(df)

    if  st.button('RUN'):
        if model == 'Linear Regression':
            st.success(classify(lin_reg.predict(df)))
        elif model == 'Logistic Regresion':
            st.success(classify(log_reg.predict(df)))
        else:
            st.success(classify(svc_m.predict(df)))


if __name__ == '__main__':
    main()
