import re

import streamlit as st
import requests


WEBHOOK_URL = st.secrets["WEBHOOK_URL"]  # Replace with your actual webhook URL

def is_valid_email(email):
    """
    Validate the email address using a simple regex pattern.
    """
    import re
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

def contact_form():
  with st.form("contact_form"):
      first_name = st.text_input("First Name")
      last_name = st.text_input("Last Name")
      email = st.text_input("Email")
      message = st.text_area("Message")
      submit_button = st.form_submit_button("Submit")
      if submit_button:
        if not first_name or not last_name or not email or not message:
            st.error("Please fill in all fields.")
            st.stop()
        if not is_valid_email(email):
            st.error("Please enter a valid email address.")
            st.stop()

        data = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "message": message
        }
        try:
            response = requests.post(WEBHOOK_URL, json=data)
            if response.status_code == 200:
                st.success("Your message has been sent successfully!")
            else:
                st.error("There was an error sending your message. Please try again later.")
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {e}")