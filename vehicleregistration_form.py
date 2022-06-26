# Import the libraries for Pandas and Streamlit
import streamlit as st
import pandas as pd

# Create a title for your application using markdown syntax and the Streamlit
# `write` function.
st.write("# Car Registration Web Application")

# Create an opening sentence for your application using regular text and the
# Streamlit `write` function.
st.write("This Web Application allows you to register your vehicle as a vistor.")

with st.form("Vehicle_Registration_Form"):
    st.write("Vehicle Information")
    text = st.text_input("Enter your vehicle information here. Unit visting, license plate number, car make & year, car color, and parking spot number.")

    library = st.selectbox(
    "For how many days are you visiting?",
    ("1 day", "5 days", "More than 5 days")
)

    picture = st.file_uploader("Vehicle photo", type=['png', 'jpg'], accept_multiple_files=False, key=None, help="Snap a photo of vehicle and upload it", on_change=None, args=None, kwargs=None, disabled=False)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("vehicle_information", text, "how_manydays", library, "vehicle_photo", picture)

st.write("## Please note, vehicles not properly registered will be towed at the owner's expense.")

st.button("Click Here For Questions")

st.image('LOGO.png')


