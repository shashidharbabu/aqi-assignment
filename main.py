import pickle
import pandas as pd

import streamlit as st

st.set_page_config(
    page_title="Air Quality Index",
    layout="wide",
    initial_sidebar_state="expanded",
)

pm2 = st.number_input(label="PM2.5")
pm10 = st.number_input(label="PM10")
no = st.number_input(label="NO")
no2 = st.number_input(label="NO2")
nox = st.number_input(label="NOx")
nh3 = st.number_input(label="NH3")
co = st.number_input(label="CO")
so2 = st.number_input(label="SO2")
o3 = st.number_input(label="O3")
benzene = st.number_input(label="Benzene")
toluene = st.number_input(label="Toluene")
xylene = st.number_input(label="Xylene")

temp = {
    'PM2.5': [pm2],
    'PM10': [pm10],
    'NO': [no],
    'NO2': [no2],
    'NOx': [nox],
    'NH3': [nh3],
    'CO': [co],
    'SO2': [so2],
    'O3': [o3],
    'Benzene': [benzene],
    'Toluene': [toluene],
    'Xylene': [xylene]
}
df = pd.DataFrame(data=temp)
model = pickle.load(open('model.pkl', 'rb'))


if st.button("Predit"):
    st.write(model.predict(df)[0])
