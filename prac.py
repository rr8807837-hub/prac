import streamlit as st
st.markdown("""
   <style>
   header[data-testid="stHeader"]{
       visibility:hidden;
    }
   footer{display=none;}
   #MainMenu{
       visibility:hidden;
   }
   section[data-testid="stSidebar"]{
       visibility:block !important;
   } 
   <\style>         
""",unsafe_allow_html=True)
st.sidebar.text_input("name")
