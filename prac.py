import streamlit as st
st.markdown("""
   <style>
   header[data-testid="stHeader"]{
       display=none;
    }
   footer{display=none;}
   #MainMenu{
       visibility:hidden;
   }
   section[data-testid="stSidebar"]{
       display:block !important;
   } 
   <\style>         
""",unsafe_allow_html=True)
st.sidebar.text_input("name")
