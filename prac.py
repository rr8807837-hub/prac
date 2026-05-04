import streamlit as st
st.set_page_config(page_title="Streamlit Practice", page_icon=":smile:",initial_sidebar_state="expanded")
if "gen" not in st.session_state:
    st.session_state.gen=False
st.markdown("""
   <style>
   header[data-testid="stHeader"]{
       display:none;
    }
   footer{display=none;}
   #MainMenu{
       visibility:hidden;
   }
   <\style>         
""",unsafe_allow_html=True)
st.sidebar.text_input("name")
name=st.text_input("name", key="text")
button=st.button("submit" ,key="sub")
if st.button:
    st.write(name)
