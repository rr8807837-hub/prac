import streamlit as st
import pymongo
from pymongo import MongoClient
import webbrowser

if "gen" not in st.session_state:
    st.session_state.gen=""
# MongoDB connection
client = MongoClient("mongodb+srv://rr8807837_db_user:raja44raja@cluster0.jstxelp.mongodb.net/")
db = client["chat"]
collection = db["message"]
st.set_page_config(page_title="mongo",layout="wide",page_icon=":mango:")
st.title("MongoDB connection")
st.session_state.chat = st.text_input("enter here" ,key="chatinput")
st.latex(r"a+b=c") 
if st.button("save"):
    chat=collection.insert_one({"message":st.session_state.chat})
    st.success("saved into mongoDB")
    st.switch_page("pages/p.py")
st.markdown("""
            <style>
            .stButton>button{
                border-radius:10px;
                background-color:red;
            }
            </style>
            """,unsafe_allow_html=True)        
t1=st.toggle("login")
if  t1:
    st.toggle("signup")      
