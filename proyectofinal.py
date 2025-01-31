# -*- coding: utf-8 -*-
"""ProyectoFinal.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13M5WvToWp97CsqsaFG3QVkjCGKItODHM

Se carga las archivos y se manejan los errores de estos
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargamos los datos
vino_rojo = pd.read_csv('winequality-red.csv', delimiter=';')
vino_blanco = pd.read_csv('winequality-white.csv', delimiter=';')

# Convertir columnas numéricas y manejar errores
datos_vinoRojo_numericos = vino_rojo.apply(pd.to_numeric, errors='coerce')

# Eliminar filas con NaN
datos_vinos_numericos = datos_vinoRojo_numericos.dropna()

# Convertir columnas numéricas y manejar errores
datos_vinoBlanco_numericos = vino_blanco.apply(pd.to_numeric, errors='coerce')

# Eliminar filas con NaN
datos_vinoB_numericos = datos_vinoBlanco_numericos.dropna()

"""Identificar cuales son las variables de cada archivos"""

import pandas as pd

# Carga tus datos
datos_vino = pd.read_csv('winequality-red.csv', delimiter=';')

# Verifica los nombres de las columnas
print(datos_vino.columns)

# Carga tus datos
datos_vinoBlanco = pd.read_csv('winequality-white.csv', delimiter=';')

# Verifica los nombres de las columnas
print(datos_vinoBlanco.columns)

"""Analisis Grafico de los vinos rojos"""

# Visualización de la distribución de una variable numérica (acides fija)
plt.figure(figsize=(10, 6))
sns.histplot(vino_rojo['fixed_acidity'], bins=20, kde=True)
plt.title('Distribución de la acides fija en los vinos rojos')
plt.xlabel('fixed_acidity')
plt.ylabel('Frecuencia')
plt.show()

# Visualización de la distribución de una variable numérica (acido citrico)
plt.figure(figsize=(10, 6))
sns.histplot(vino_rojo['citric_acid'], bins=20, kde=True)
plt.title('Distribución del Acido citrico en los vinos rojos')
plt.xlabel('citric_acid')
plt.ylabel('Frecuencia')
plt.show()

# Visualización de la distribución de una variable numérica (alcohol)
plt.figure(figsize=(10, 6))
sns.histplot(vino_rojo['alcohol'], bins=20, kde=True)
plt.title('Distribución del Alcohol en los vinos rojos')
plt.xlabel('alcohol')
plt.ylabel('Frecuencia')
plt.show()

# Visualización de la distribución de una variable numérica (calidad)
plt.figure(figsize=(10, 6))
sns.histplot(vino_rojo['quality'], bins=20, kde=True)
plt.title('Distribución de la Calidad en los vinos rojos')
plt.xlabel('quality')
plt.ylabel('Frecuencia')
plt.show()

# Visualización de la relación entre dos variables numéricas (acides fija y acides citrica)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='fixed_acidity', y='citric_acid', data=vino_rojo)
plt.title('Relación entre acides fija y acido citrico de vinos rojos')
plt.xlabel('fixed_acidity')
plt.ylabel('citric_acid')
plt.show()

# Visualización de la relación entre dos variables numéricas (alcohol y calidad)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='alcohol', y='quality', data=vino_rojo)
plt.title('Relación entre calidad y alcohol de vinos rojos')
plt.xlabel('alcohol')
plt.ylabel('quality')
plt.show()

#Presentamos un inconveniente con un dato, el cual no fue posible convertir por lo que recurrimos a lo siguiente:
# Intentar calcular la correlación entre dos columnas específicas
try:
    correlacion_ejemplo = datos_vinos_numericos[['fixed_acidity', 'citric_acid']].corr()
    print("Correlación entre acides fija y acido citrico:")
    print(correlacion_ejemplo)
except Exception as e:
    print("Error al calcular la correlación:", e)

# Matriz de correlación y mapa de calor
try:
  matriz_correlacion = datos_vinos_numericos.corr()
  plt.figure(figsize=(10, 8))
  sns.heatmap(matriz_correlacion, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
  plt.title('Matriz de correlación entre variables')
  plt.show()
except Exception as e:
    print("Error:", e)

"""Analisis grafico de los Vinos Blancos"""

# Analisis Grafico de los vinos blancos

# Visualización de la distribución de una variable numérica (acides fija)
plt.figure(figsize=(10, 6))
sns.histplot(vino_blanco['free_sulfur_dioxide'], bins=20, kde=True)
plt.title('Distribución de la Dioxido de Azufre libre en los vinos blancos')
plt.xlabel('free_sulfur_dioxide')
plt.ylabel('Frecuencia')
plt.show()

# Visualización de la distribución de una variable numérica (pH)
plt.figure(figsize=(10, 6))
sns.histplot(vino_blanco['total_sulfur_dioxide'], bins=20, kde=True)
plt.title('Distribución del total de Dioxido de Azufre en los vinos blancos')
plt.xlabel('total_sulfur_dioxide')
plt.ylabel('Frecuencia')
plt.show()

# Visualización de la distribución de una variable numérica (alcohol)
plt.figure(figsize=(10, 6))
sns.histplot(vino_rojo['alcohol'], bins=20, kde=True)
plt.title('Distribución del Alcohol en los vinos blancos')
plt.xlabel('alcohol')
plt.ylabel('Frecuencia')
plt.show()

# Visualización de la distribución de una variable numérica (calidad)
plt.figure(figsize=(10, 6))
sns.histplot(vino_rojo['quality'], bins=20, kde=True)
plt.title('Distribución de la Calidad en los vinos blancos')
plt.xlabel('quality')
plt.ylabel('Frecuencia')
plt.show()



# Visualización de la relación entre dos variables numéricas (acides fija y calidad)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='total_sulfur_dioxide', y='free_sulfur_dioxide', data=vino_blanco)
plt.title('Relación entre el Total de Dioxido de Azufre y el Dioxido de Azufre Libre en los vinos blancos')
plt.xlabel('total_sulfur_dioxide')
plt.ylabel('free_sulfur_dioxide')
plt.show()

# Visualización de la relación entre dos variables numéricas (alcohol y calidad)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='alcohol', y='quality', data=vino_rojo)
plt.title('Relación entre calidad y alcohol de vinos blancos')
plt.xlabel('alcohol')
plt.ylabel('quality')
plt.show()


#Al mostrar inconvenientes para calcular la matriz de correlación, presentamos la siguiente solución
#Intentar calcular la correlación entre dos columnas específicas
try:
    correlacion_ejemplo = datos_vinoB_numericos[['fixed_acidity', 'pH']].corr()
    print("Correlación entre acides fija y pH:")
    print(correlacion_ejemplo)
except Exception as e:
    print("Error al calcular la correlación:", e)

# Matriz de correlación y mapa de calor
try:
  matriz_correlacion = datos_vinoB_numericos.corr()
  plt.figure(figsize=(10, 8))
  sns.heatmap(matriz_correlacion, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
  plt.title('Matriz de correlación entre variables')
  plt.show()
except Exception as e:
    print("Error:", e)

"""Normalización, Busqueda de Datos atipicos y entrenamiento de diferentes redes neuronales para los Vinos Rojos de las variables: Alcohol y Calidad"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Cargar los datos
data = pd.read_csv('winequality-red.csv', delimiter=';')

# Asegúrate de que la columna 'alcohol' sea numérica
data['alcohol'] = pd.to_numeric(data['alcohol'], errors='coerce')

# Eliminar filas con valores NaN en la columna 'alcohol'
data = data.dropna(subset=['alcohol'])

# Calcular IQR y eliminar outliers
Q1 = data['alcohol'].quantile(0.25)
Q3 = data['alcohol'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
data_filtered = data[(data['alcohol'] >= lower_bound) & (data['alcohol'] <= upper_bound)]

# La columna característica es 'alcohol' y la columna objetivo es 'quality'
X = data_filtered[['alcohol']].astype(float)
y = data_filtered['quality'].astype(int)

# Convertimos la calidad a una tarea binaria (bueno o malo)
y = (y > 5).astype(int)

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Verificar las formas de los conjuntos
print(f'X_train shape: {X_train.shape}, y_train shape: {y_train.shape}')
print(f'X_test shape: {X_test.shape}, y_test shape: {y_test.shape}')

# Definir los modelos
def create_perceptron():
    model = Sequential([
        Dense(units=1, activation='sigmoid', input_shape=(1,), use_bias=True)
    ])
    return model

def create_single_hidden():
    model = Sequential([
        Dense(units=1, activation='sigmoid', input_shape=(1,), use_bias=True),
        Dense(units=1, activation='sigmoid', use_bias=True)
    ])
    return model

def create_double_hidden():
    model = Sequential([
        Dense(units=2, activation='sigmoid', input_shape=(1,), use_bias=True),
        Dense(units=2, activation='sigmoid', use_bias=True),
        Dense(units=1, activation='sigmoid', use_bias=True)
    ])
    return model

# Lista de modelos
models = [
    ('Perceptrón', create_perceptron),
    ('Una capa oculta', create_single_hidden),
    ('Dos capas ocultas', create_double_hidden)
]

# Diccionario para almacenar resultados
results = {}

# Entrenar y evaluar cada modelo
for name, create_model in models:
    model = create_model()
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=10, batch_size=1, verbose=1)
    y_pred = model.predict(X_test)
    y_pred = (y_pred > 0.5).astype(int)

    # Calcular métricas
    acc = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)

    # Guardar resultados
    results[name] = {
        'accuracy': acc,
        'precision': precision,
        'recall': recall,
        'f1_score': f1,
        'conf_matrix': conf_matrix
    }

# Mostrar resultados
for name, metrics in results.items():
    print(f'\n{name}:')
    print(f"Accuracy: {metrics['accuracy']:.4f}")
    print(f"Precision: {metrics['precision']:.4f}")
    print(f"Recall: {metrics['recall']:.4f}")
    print(f"F1 Score: {metrics['f1_score']:.4f}")
    print(f"Confusion Matrix:\n{metrics['conf_matrix']}")

# Análisis comparativo
print("\nAnálisis comparativo:")
for metric in ['accuracy', 'precision', 'recall', 'f1_score']:
    print(f'\n{metric.capitalize()}:')
    for name in results:
        print(f'{name}: {results[name][metric]:.4f}')

"""Normalización, Busqueda de Datos atipicos y entrenamiento de diferentes redes neuronales para los Vinos Blancos de las variables: Alcohol y Calidad"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Cargar los datos
data = pd.read_csv('winequality-white.csv', delimiter=';')

# Asegúrate de que la columna 'alcohol' sea numérica
data['alcohol'] = pd.to_numeric(data['alcohol'], errors='coerce')

# Eliminar filas con valores NaN en la columna 'alcohol'
data = data.dropna(subset=['alcohol'])

# Calcular IQR y eliminar outliers
Q1 = data['alcohol'].quantile(0.25)
Q3 = data['alcohol'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
data_filtered = data[(data['alcohol'] >= lower_bound) & (data['alcohol'] <= upper_bound)]

# La columna característica es 'alcohol' y la columna objetivo es 'quality'
X = data_filtered[['alcohol']].astype(float)
y = data_filtered['quality'].astype(int)

# Convertimos la calidad a una tarea binaria (bueno o malo)
y = (y > 5).astype(int)

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Verificar las formas de los conjuntos
print(f'X_train shape: {X_train.shape}, y_train shape: {y_train.shape}')
print(f'X_test shape: {X_test.shape}, y_test shape: {y_test.shape}')

# Definir los modelos
def create_perceptron():
    model = Sequential([
        Dense(units=1, activation='sigmoid', input_shape=(1,), use_bias=True)
    ])
    return model

def create_single_hidden():
    model = Sequential([
        Dense(units=1, activation='sigmoid', input_shape=(1,), use_bias=True),
        Dense(units=1, activation='sigmoid', use_bias=True)
    ])
    return model

def create_double_hidden():
    model = Sequential([
        Dense(units=2, activation='sigmoid', input_shape=(1,), use_bias=True),
        Dense(units=2, activation='sigmoid', use_bias=True),
        Dense(units=1, activation='sigmoid', use_bias=True)
    ])
    return model

# Lista de modelos
models = [
    ('Perceptrón', create_perceptron),
    ('Una capa oculta', create_single_hidden),
    ('Dos capas ocultas', create_double_hidden)
]

# Diccionario para almacenar resultados
results = {}

# Entrenar y evaluar cada modelo
for name, create_model in models:
    model = create_model()
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=10, batch_size=1, verbose=1)
    y_pred = model.predict(X_test)
    y_pred = (y_pred > 0.5).astype(int)

    # Calcular métricas
    acc = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)

    # Guardar resultados
    results[name] = {
        'accuracy': acc,
        'precision': precision,
        'recall': recall,
        'f1_score': f1,
        'conf_matrix': conf_matrix
    }

# Mostrar resultados
for name, metrics in results.items():
    print(f'\n{name}:')
    print(f"Accuracy: {metrics['accuracy']:.4f}")
    print(f"Precision: {metrics['precision']:.4f}")
    print(f"Recall: {metrics['recall']:.4f}")
    print(f"F1 Score: {metrics['f1_score']:.4f}")
    print(f"Confusion Matrix:\n{metrics['conf_matrix']}")

# Análisis comparativo
print("\nAnálisis comparativo:")
for metric in ['accuracy', 'precision', 'recall', 'f1_score']:
    print(f'\n{metric.capitalize()}:')
    for name in results:
        print(f'{name}: {results[name][metric]:.4f}')

"""Normalización, Busqueda de Datos atipicos y entrenamiento de diferentes redes neuronales para los Vinos rojos de las variables: Acides Fija y Acides citrica respecto a la calidad

"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Cargar los datos
data = pd.read_csv('winequality-red.csv', delimiter=';')

# Función para identificar outliers usando el método IQR
def identify_outliers(df, feature):
    Q1 = df[feature].quantile(0.25)
    Q3 = df[feature].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[feature] < lower_bound) | (df[feature] > upper_bound)]
    return outliers
# Identificar outliers en 'fixed_acidity'
outliers_fixed_acidity = identify_outliers(data, 'fixed_acidity')
print(f'Outliers in fixed_acidity:\n{outliers_fixed_acidity}')

# Identificar outliers en 'citric_acid'
outliers_citric_acid = identify_outliers(data, 'citric_acid')
print(f'Outliers in citric_acid:\n{outliers_citric_acid}')

# Visualización de outliers
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
sns.boxplot(y=data['fixed_acidity'])
plt.title('Fixed Acidity Outliers')

plt.subplot(1, 2, 2)
sns.boxplot(y=data['citric_acid'])
plt.title('Citric Acid Outliers')

plt.show()

# Eliminar outliers en 'fixed_acidity' y 'citric_acid'
def remove_outliers(df, feature):
    Q1 = df[feature].quantile(0.25)
    Q3 = df[feature].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df = df[(df[feature] >= lower_bound) & (df[feature] <= upper_bound)]
    return df

data_cleaned = remove_outliers(data, 'fixed_acidity')
data_cleaned = remove_outliers(data_cleaned, 'citric_acid')


# Seleccionar las características y la columna objetivo
X = data[['fixed_acidity', 'citric_acid']]
y = data['quality']

# Convertir la calidad a una tarea binaria (bueno o malo)
y = (y > 5).astype(int)

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Verificar las formas de los conjuntos
print(f'X_train shape: {X_train.shape}, y_train shape: {y_train.shape}')
print(f'X_test shape: {X_test.shape}, y_test shape: {y_test.shape}')

def train_and_evaluate_model(model, X_train, y_train, X_test, y_test):
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=10, batch_size=1, verbose=0)
    y_pred = (model.predict(X_test) > 0.5).astype(int)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    return accuracy, precision, recall, f1, cm

# Perceptrón
model_perceptron = Sequential([
    Dense(units=1, activation='sigmoid', input_shape=(2,), use_bias=True)
])
accuracy_perceptron, precision_perceptron, recall_perceptron, f1_perceptron, cm_perceptron = train_and_evaluate_model(model_perceptron, X_train, y_train, X_test, y_test)
print(f'Perceptrón:\nAccuracy: {accuracy_perceptron}\nPrecision: {precision_perceptron}\nRecall: {recall_perceptron}\nF1 Score: {f1_perceptron}\nConfusion Matrix:\n{cm_perceptron}\n')

# Red neuronal con una capa oculta
model_one_hidden = Sequential([
    Dense(units=2, activation='relu', input_shape=(2,), use_bias=True),
    Dense(units=1, activation='sigmoid', use_bias=True)
])
accuracy_one_hidden, precision_one_hidden, recall_one_hidden, f1_one_hidden, cm_one_hidden = train_and_evaluate_model(model_one_hidden, X_train, y_train, X_test, y_test)
print(f'Una capa oculta:\nAccuracy: {accuracy_one_hidden}\nPrecision: {precision_one_hidden}\nRecall: {recall_one_hidden}\nF1 Score: {f1_one_hidden}\nConfusion Matrix:\n{cm_one_hidden}\n')

# Red neuronal con dos capas ocultas
model_two_hidden = Sequential([
    Dense(units=2, activation='relu', input_shape=(2,), use_bias=True),
    Dense(units=2, activation='relu', use_bias=True),
    Dense(units=1, activation='sigmoid', use_bias=True)
])
accuracy_two_hidden, precision_two_hidden, recall_two_hidden, f1_two_hidden, cm_two_hidden = train_and_evaluate_model(model_two_hidden, X_train, y_train, X_test, y_test)
print(f'Dos capas ocultas:\nAccuracy: {accuracy_two_hidden}\nPrecision: {precision_two_hidden}\nRecall: {recall_two_hidden}\nF1 Score: {f1_two_hidden}\nConfusion Matrix:\n{cm_two_hidden}\n')

"""Normalización, Busqueda de Datos atipicos y entrenamiento de diferentes redes neuronales para los Vinos Blancos de las variables: dioxido de azufre libre, total de dioxido de azufre respecto a la calidad"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Cargar los datos
data = pd.read_csv('winequality-white.csv', delimiter=';')

# Función para identificar outliers usando el método IQR
def identify_outliers(df, feature):
    Q1 = df[feature].quantile(0.25)
    Q3 = df[feature].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[feature] < lower_bound) | (df[feature] > upper_bound)]
    return outliers
# Identificar outliers en 'azufre libre'
outliers_free_sulfur_dioide = identify_outliers(data, 'free_sulfur_dioxide')
print(f'Outliers in free_sulfur_dioide:\n{outliers_free_sulfur_dioide}')

# Identificar outliers en 'azufre total'
outliers_total_sulfur_dioxide = identify_outliers(data,'total_sulfur_dioxide')
print(f'Outliers in total_sulfur_dioxide:\n{outliers_total_sulfur_dioxide}')

# Visualización de outliers
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
sns.boxplot(y=data['free_sulfur_dioxide'])
plt.title('Free Sulfur Dioxide Outliers')

plt.subplot(1, 2, 2)
sns.boxplot(y=data['total_sulfur_dioxide'])
plt.title('Total Sulfur Dioxide Outliers')

plt.show()

# Eliminar outliers en 'fixed_acidity' y 'citric_acid'
def remove_outliers(df, feature):
    Q1 = df[feature].quantile(0.25)
    Q3 = df[feature].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df = df[(df[feature] >= lower_bound) & (df[feature] <= upper_bound)]
    return df

data_cleaned = remove_outliers(data, 'free_sulfur_dioxide')
data_cleaned = remove_outliers(data_cleaned, 'total_sulfur_dioxide')


# Seleccionar las características y la columna objetivo
X = data[['free_sulfur_dioxide', 'total_sulfur_dioxide']]
y = data['quality']

# Convertir la calidad a una tarea binaria (bueno o malo)
y = (y > 5).astype(int)

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Verificar las formas de los conjuntos
print(f'X_train shape: {X_train.shape}, y_train shape: {y_train.shape}')
print(f'X_test shape: {X_test.shape}, y_test shape: {y_test.shape}')

def train_and_evaluate_model(model, X_train, y_train, X_test, y_test):
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=10, batch_size=1, verbose=0)
    y_pred = (model.predict(X_test) > 0.5).astype(int)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    return accuracy, precision, recall, f1, cm

# Perceptrón
model_perceptron = Sequential([
    Dense(units=1, activation='sigmoid', input_shape=(2,), use_bias=True)
])
accuracy_perceptron, precision_perceptron, recall_perceptron, f1_perceptron, cm_perceptron = train_and_evaluate_model(model_perceptron, X_train, y_train, X_test, y_test)
print(f'Perceptrón:\nAccuracy: {accuracy_perceptron}\nPrecision: {precision_perceptron}\nRecall: {recall_perceptron}\nF1 Score: {f1_perceptron}\nConfusion Matrix:\n{cm_perceptron}\n')

# Red neuronal con una capa oculta
model_one_hidden = Sequential([
    Dense(units=2, activation='relu', input_shape=(2,), use_bias=True),
    Dense(units=1, activation='sigmoid', use_bias=True)
])
accuracy_one_hidden, precision_one_hidden, recall_one_hidden, f1_one_hidden, cm_one_hidden = train_and_evaluate_model(model_one_hidden, X_train, y_train, X_test, y_test)
print(f'Una capa oculta:\nAccuracy: {accuracy_one_hidden}\nPrecision: {precision_one_hidden}\nRecall: {recall_one_hidden}\nF1 Score: {f1_one_hidden}\nConfusion Matrix:\n{cm_one_hidden}\n')

# Red neuronal con dos capas ocultas
model_two_hidden = Sequential([
    Dense(units=2, activation='relu', input_shape=(2,), use_bias=True),
    Dense(units=2, activation='relu', use_bias=True),
    Dense(units=1, activation='sigmoid', use_bias=True)
])
accuracy_two_hidden, precision_two_hidden, recall_two_hidden, f1_two_hidden, cm_two_hidden = train_and_evaluate_model(model_two_hidden, X_train, y_train, X_test, y_test)
print(f'Dos capas ocultas:\nAccuracy: {accuracy_two_hidden}\nPrecision: {precision_two_hidden}\nRecall: {recall_two_hidden}\nF1 Score: {f1_two_hidden}\nConfusion Matrix:\n{cm_two_hidden}\n')