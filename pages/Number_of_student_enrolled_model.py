import streamlit as st
import pickle
import pandas as pd
st.image("image/cauca.svg",width=200 )
st.title('Number of student enrolled model')
year = [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
year = st.sidebar.selectbox('Select a year', year)
Period = [1 , 2]
Period = st.sidebar.selectbox('Select a period', Period)
Programs = [1,2,3,4,5,6,7,8,9,10]
Programs = st.sidebar.selectbox('Select numbers of the programs', Programs)

number = -314418.891848 + 156.53*year + 37.0773*Period + 31.5408*Programs

if(st.button('Calculate number students')):
    st.text("Numbers of the students for the year {} period {} are {}.".format(year,Period,number ))
