import streamlit as st


# --- PAGE SETUP ---
about_page = st.Page (
  page = "views/about_me.py",
  title = "About Me",
  icon = "👤", 
)

project_1_page = st.Page (
  page = "views/sales_dashboard.py",
  title = "Sales Dashboard",
  icon = "📊", 
)
project_2_page = st.Page (
  page = "views/chatbot.py",
  title = "Chatbot",
  icon = "🤖", 
)

pg = st.navigation(
  {
    "Info": [about_page],
    "Projects": [project_1_page, project_2_page],
  }
)

st.logo("assets/logo.jpeg")
st.sidebar.text("Made with ❤️ by Kris")


# --- RUN NAVIGATION ---
pg.run()


