#Project 01: unit convertor
#Built a Google Unit Convertor using python and streamlit:

import streamlit as st
st.markdown(
    """
    <style>
    body {
       background-color: #1e1e2f;
      color: white;
    }
    .stApp {
       background: linear-gradient(135deg, #bcbcbc,#cfe2f);
       padding: 30px;
       border-radius: 15px;
       box-shadow: 0px 10px 30px rgba(0, 0 ,0,0.3);
    }
    h1 {
        text-align: center;
        margin-bottom: 30px;
        font-size: 36px;
        font-weight: bold;
        color: white;
    }
    .stButton>button{
        background-color: #2e2e4a;
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 10px;
        box-shadow: 0px 5px 15px rgba(0, 255, 255, 0.3);
    }
    .stButton>button:hover{
        transform: scale(1.05);
        transition: transform 0.3s ease;
        background-color: #4e4e7a;
        color: black;
    }
    .result-box{
        
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background:rgba(255,255,255,0.1);
        padding: 25px;
        border-radius: 10px;
        marging-top: 20px; 
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.3);
    }
    .footer{
        text-align: center;
        marging-top: 50px;
        font-size: 14px;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#title and description:
st.markdown("<h1>💥Universal Unit Convertor 💥</h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of length, weight, and temperature.")

#side bar and description:
conversion_type = st.sidebar.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter the value", value=0.0, min_value=0.0, step=0.1 )
col1, col2 = st.columns(2)

#conversion logic:
if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From Unit", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles","Feet", "Inches", "Yards" ])
    with col2:
        to_unit = st.selectbox("To Unit", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles","Feet", "Inches", "Yards" ])
elif conversion_type == "Weight": 
    with col1:
        from_unit = st.selectbox("From Unit", ["Kilograms", "Grams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To Unit", ["Kilograms", "Grams", "Pounds", "Ounces"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])

#conversion function:
def length_conversion(value, from_unit, to_unit):
    length_units = {
        "Meters": 1.0, 
        "Kilometers": 0.001,
        "Centimeters": 100,
        "Millimeters": 1000,
        "Miles": 0.000621371,
        "Feet": 3.28,
        "Inches": 39.3701,
        "Yards": 1.09361
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_conversion(value, from_unit, to_unit):
    weight_units = {
        "Kilograms": 1.0,
        "Grams": 1000,
        "Pounds": 2.20462,
        "Ounces": 35.274
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temperature_conversion(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else (value + 273.15) if to_unit == "Kelvin" else value
        return (value - 32) * 5/9
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return (value - 273.15) if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32 if to_unit == "Fahrenheit" else value
    return value

#button to perform conversion:
if st.button("🌐Convert"):
    if conversion_type == "Length":
        result = length_conversion(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_conversion(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temperature_conversion(value, from_unit, to_unit)
    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

#footer:
st.markdown("<div class='footer'>Developed by [💎Asmara Faisal💎]</div>", unsafe_allow_html=True)







