import streamlit as st

def unit_converter(value:float , unit_from : str, unit_to:str):


    conversions = {
    "meters_kilometers" : 0.001 ,  #1 kilometers = 1000 metrs
    "kilometers_meters" : 1000 ,# 1 meters   = 0.001 kilometers
    "grams_kilograms" : 0.001 ,   # 1 kilogram =  1000 grams 
    "kilograms_grams" : 1000 # 1 gram = 0.001 kilogram
    }

    key = f"{unit_from}_{unit_to}"

    if key in conversions:
        conversion = conversions[key]
        return value * conversion    
    else:
        return "conversion not supported"


st.title("unit converter")
value = st.number_input("enter the value:")

unit_from = st.selectbox("convert_from", ["meters","kilometers","grams","kilograms"])

unit_to = st.selectbox("convert_to", ["meters","kilometers","grams","kilograms"])

if st.button ("convert"):
    result = unit_converter(value,unit_from,unit_to)
    st.write(f"converted value :, {result}")
    