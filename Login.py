import streamlit as st        
import pymongo 
from pymongo import MongoClient
from datetime import datetime
import pandas as pd
st.set_page_config(page_title="Login page",layout="centered",page_icon=":link:",initial_sidebar_state="collapsed")
if "gen" not in st.session_state:
    st.session_state.gen=""   
st.markdown("""
            <style>
            #MainMenu{visibility:hidden;}
            header {visibility: hidden;} /* top header */
            footer {visibility: hidden;} 
            .stApp{
                background:black;
                color: black;
            }
            .stButton > button{
                margin-left:42px;
                background-color:green;
                color:white;
            }
            </style>
            """,unsafe_allow_html=True)
client = MongoClient("mongodb+srv://rr8807837_db_user:raja44raja@cluster0.jstxelp.mongodb.net/")
db = client["ResumeApp"]
collection = db["Users"]
st.title("RESUME GENERATOR")
st.caption("Build professional resumes in minutes")
st.header("Login page")
col1,col2,col3=st.columns(3)
with col2:
    if st.toggle("Please Click here to Login"):
        with st.container(border=True):
            st.session_state.name=st.text_input("Enter your name")
            st.session_state.email=st.text_input("Enter your Email")
            if st.button("Login",key="log"):
                collection.insert_one({"Name":st.session_state.name,"Email":st.session_state.email,"Time":datetime.utcnow()})
                st.success("Login Successfull")
                st.switch_page("pages/resume.py")
c1,c2=st.columns(2)
with c1:                
    st.expander("About",width=300).write("RESUME GENERATOR helps you to build classic and modern resumes for freshers")                

with c2:
    t=st.expander("Steps to follow")
    t.write("step 1:Login")
    t.write("step 2:Fill your details")
    t.write("step 3:select the theme(Classic/Modern)")
    t.write("step 4:Click Generate Resume")
    t.write("step 5:check the preview of your resume and click download")

                    
   
