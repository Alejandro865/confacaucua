import streamlit as st
import pickle
import pandas as pd
st.image("image/cauca.svg",width=200 )
st.title('Number of student enrolled model')
year = [2017, 2018, 2019]
year = st.sidebar.selectbox('Select a year', year)
Period = [1 , 2]
Period = st.sidebar.selectbox('Select a period', Period)
Programs = [1,2,3,4,5,6,7,8,9,10]
Programs = st.sidebar.selectbox('Select numbers of the programs', Programs)

number = 2*year+2*Period+25*Programs

if(st.button('Calculate number students')):
    st.text("Numbers of the students for the year {} period {} are {}.".format(year,Period,number ))
