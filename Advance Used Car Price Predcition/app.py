import pickle

import numpy as np
import streamlit as st

st.title("Used car Price Prediction")

with open('C:\\Users\\Ghost Codm\\Downloads\\Compressed\\archive\\catmodel.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('C:\\Users\\Ghost Codm\\Downloads\\Compressed\\archive\\data.pkl', 'rb') as data_file:
    data = pickle.load(data_file)

    
    
st.title('Used Car Price Prediction')

# setting feature for predict price

name = st.selectbox('Enter Car Name', data['name'].unique())
year = st.number_input("Enter Buying Year")
km_driven = st.number_input('Enter Driven Km')
fuel = st.selectbox('Select Fuel Type', data['fuel'].unique())
saller_type = st.selectbox('Enter SallerType',data['seller_type'].unique())
transmission = st.selectbox('Choose Transmissin Type',data['transmission'].unique())
owner = st.selectbox('Select Owern Lavel',data['owner'].unique())
mileage = st.number_input("Enter Mileage")
engine = st.number_input('Enter Engine Power')
max_power = st.number_input('Enter Max_Power')
seats = st.selectbox('Select Seats Number',data['seats'].unique())
torque_value = st.number_input("Enter Torque Value")
engine_rpm = st.number_input('Enter Engine RPM value')

if st.button('Predict'):
    query = np.array([name,year,km_driven,fuel,saller_type,transmission,owner,mileage,engine,max_power,seats,torque_value,engine_rpm])
    query = query.reshape(1,13)
    st.title("The Price Of Your Will May Be: " + str(int(model.predict(query)))*2)