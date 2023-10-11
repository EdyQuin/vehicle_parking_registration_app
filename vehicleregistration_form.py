# Import the libraries for Pandas and Streamlit
import streamlit as st
import pandas as pd

# Create a title for your application using markdown syntax and the Streamlit
# `write` function.
st.image('LOGO.png')
st.write("# Car Registration Web Application")

# Create an opening sentence for your application using regular text and the
# Streamlit `write` function.
st.write("This Web Application allows you to register your vehicle for private parking.")

with st.form("Vehicle_Registration_Form"):
    st.write("Vehicle Information")
    text = st.text_input("Enter your vehicle information here. Unit, license plate number, car make model & year, car color, and parking spot number.")

    library = st.selectbox(
    "How long is your parking space agreement?",
    ("1 year", "3 months", "6 months")
)

    picture = st.file_uploader("Vehicle photo", type=['png', 'jpg'], accept_multiple_files=False, key=None, help="Snap a photo of vehicle and upload it", on_change=None, args=None, kwargs=None, disabled=False)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("vehicle_information", text, "how_manydays", library, "vehicle_photo", picture)

st.write("## Please note, vehicles not properly registered will be towed at the owner's expense.")

st.button("Click Here For Questions")

