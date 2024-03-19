import pandas as pd
import numpy as np
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

URL = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
titanic = pd.read_csv(URL, index_col='PassengerId')

st.title('Titanic con Streamlit')

st.write('Hagamos un primer visionado del dataset')

st.write(titanic.head())

option = st.selectbox(
    'Que es lo que quieres ver?',
    ('Supervivientes por Sexo', 'Supervivientes por Edad', 'Supervivientes por Clase'))

st.write('You selected:', option)

if option == 'Supervivientes por Sexo':

    st.bar_chart(data=titanic, x='Sex', y='Survived')

if option == 'Supervivientes por Edad':

    st.bar_chart(data=titanic, x='Age', y='Survived')

if option == 'Supervivientes por Clase':

    st.bar_chart(data=titanic, x='Pclass', y='Survived')