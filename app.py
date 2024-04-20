import streamlit as st
import pickle

st.header("PREDICT WEIGHT FROM HEIGHT")
st.write("Demo of Linear Regression")

height = st.number_input(label="Enter height in Inches",min_value=35.0,max_value=120.0,value=50.00,step=1.0)
submitted = st.button('Submit')

if submitted:
    model = pickle.load(open('model.pkl', "rb"))
    weight = model.predict([[height]])
    st.write(f"Expected weight value is **{weight[0]} pounds**")