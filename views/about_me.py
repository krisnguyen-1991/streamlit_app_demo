import streamlit as st # type: ignore

from forms.contact import contact_form

@st.dialog("Contact Me")
def show_contact_form():
    contact_form()
# --- PAGE SETUP ---

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/profilepic.jpeg")
with col2:
    st.title("Kris", anchor=False)
    st.subheader("Data Scientist | Machine Learning Engineer | Software Engineer")
    st.write(
        """
        I am a data scientist with a passion for machine learning and software engineering. 
        I love to solve complex problems and create innovative solutions using data.
        """
    )
    if st.button("Contact Me"):
        show_contact_form()
    
st.write("\n")
st.subheader("Experience and Qualifications", anchor=False)
st.write(
    """
    - **Master of Science in Data Science** from University of California, Berkeley
    - **Bachelor of Science in Computer Science** from University of California, Berkeley
    - **Certified Data Scientist** from Data Science Council of America (DASCA)
    """
)

st.write("\n")
st.subheader("Skills", anchor=False)
st.write(
    """
    - **Programming Languages**: Python, R, SQL, Java, C++
    - **Machine Learning**: Scikit-learn, TensorFlow, Keras, PyTorch
    - **Data Visualization**: Matplotlib, Seaborn, Plotly
    - **Web Development**: Streamlit, Flask, Django
    - **Cloud Computing**: AWS, Google Cloud Platform
    """
)