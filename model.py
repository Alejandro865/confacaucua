# Importar las librearias
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.svm import SVC
import pandas as pd
import pickle

# cargar los datos en un datasets

datos = pd.read_csv("data/datos.csv", low_memory=False)



#iris = datasets.load_iris()

X = datos[['Parcial1', 'Parcial2']]
y = datos['estado-encoded']

#Separar los datos en entrenamiento y prueba

x_train, x_test, y_train, y_test = train_test_split(X, y)

lin_reg = LinearRegression()
log_reg = LogisticRegression()
svc_m = SVC()

# entrenar modelos

lin_reg = lin_reg.fit(x_train, y_train)
log_reg = log_reg.fit(x_train, y_train)
svc_mo = svc_m.fit(x_train, y_train)

with open('lin_reg.pkl', 'wb') as li:
    pickle.dump(lin_reg, li)

with open('log_reg.pkl', 'wb') as lo:
    pickle.dump(log_reg, lo)

with open('svc_m.pkl', 'wb') as sv:
    pickle.dump(svc_m, sv)
