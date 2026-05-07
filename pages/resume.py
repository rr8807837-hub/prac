import streamlit as st
from xhtml2pdf import pisa
import base64
if "gen" not in st.session_state:
    st.session_state.gen=""
    
st.title("RESUME GENERATOR")
st.caption("Please fill the details")
st.markdown("""
            <style>
            .stApp{
                background:#2f8ee0;
                color:white;
            }
            .stButton > button{
                background:green;
            }
            .stDownloadButton > button{
                background: green;
            }
            </style>""",unsafe_allow_html=True)
with st.container(border=True):
    st.subheader("PERSONAL INFORMATION")
    st.session_state.name=st.text_input("Full name:")
    st.session_state.dob=st.date_input("Enter your Date of Birth")
    st.session_state.email=st.text_input("Email:")
    st.session_state.linkedin=st.text_input("Linkedin profile:")
    st.session_state.language=st.multiselect("Select languages:",("Teligu","English","Hindi","Other"))
    if "Other" in st.session_state.language:
        other=st.text_input("If other, please specify",key="other_skill")
        st.session_state.language.append(other)
    st.session_state.gender = st.radio("Select Gender", ("Male", "Female", "Other"))     
    st.session_state.phone=st.text_input("Phone number:")
    st.session_state.location = st.text_input("Address(Street,City, State,pin code)")
with st.container(border=True):
    st.subheader("🎓Education details:")
    st.session_state.High=st.selectbox("Select your highest qualification", ("Associate Degree", "Bachelor's Degree(BSc)", "Master's Degree(MSc)", "Btech", "PhD", "Other"))
    if st.session_state.High == "Other":
        other11=st.text_input("If other, please specify")
        High = other11
    st.session_state.college = st.text_input("Enter your College/University Name")
    st.session_state.field= st.text_input("Enter your Field/stream of study")
    st.session_state.graduation_year = st.text_input("Enter your Graduation Year(Eg:2020-2023)")
    st.divider()
    st.subheader("Enter your 12th details:")
    st.session_state.inter=st.selectbox("Board Name", ("Intermediate CBSE", "ICSE", "Intermediate State Board", "Other"))
    if st.session_state.inter == "Other":
        other1=st.text_input("If other, please specify")
        inter = other1
    st.session_state.college_12 =st.text_input("Enter your School/College Name")
    st.session_state.field_12=st.text_input("Enter your Field/stream of study (Eg:BIPC/MPC/CEC/Other)")
    if st.session_state.field_12 == "Other":
        other2 =st.sidebar.text_input("If other, please specify")
        field_12 = other2 
    st.session_state.graduation_12 = st.text_input("Enter your Graduation Year(Eg:2020-2022)")
    st.divider()
    st.subheader("Enter your 10th details:")
    st.session_state.high_s=st.selectbox("Board Name", ("CBSE", "ICSE", "SSC", "Other"))
    if st.session_state.high_s == "Other":
        other3=st.sidebar.text_input("If other, please specify")
        high_s = other3
    st.session_state.school_10 = st.text_input("Enter your School Name")
    st.session_state.graduation_year_10 = st.text_input("Enter your Graduation Year(Eg:2020-2023)",key="ssc")
with st.container(border=True):
    st.subheader("Job Role:")
    st.session_state.job_role = st.selectbox("", ("Software Engineer",
                                             "Data Scientist", 
                                             "Product Manager", 
                                             "UX Designer",
                                             "web developer",
                                             "mobile app developer",
                                             "Data Analyst",
                                             "Machine Learning Engineer",
                                             "DevOps Engineer", 
                                             "Other"))
    if st.session_state.job_role == "Other":
        other=st.text_input("If other, please specify")
        job_role = other        
    st.subheader("Skills:")
    st.session_state.skill=st.multiselect("Select your skills", ("Python", "Java", "C++", "SQL", "Machine Learning", "Data Analysis", "Web Development", "Mobile App Development", "Cloud Computing", "Other"))
    if "Other" in st.session_state.skill:
        other=st.text_input("If other, please specify",key="other_skill")
        st.session_state.skill.append(other)
    st.subheader("Project details:")    
    st.session_state.project=st.text_input("project name:",key="project_name")    
    st.session_state.project_descript=st.text_area("Describe your project (Includes description, technologies used, and your role in the project)")
    st.subheader("Internship details:")
    st.session_state.internship=st.text_input("Internship name:",key="internship_name")
    st.session_state.internship_descript=st.text_area("Describe your internship experience (Includes description, technologies used, and your role in the internship)")
    st.session_state.strength=st.multiselect("Select your strengths", ("Problem Solving", "Teamwork", "Communication", "Adaptability", "Leadership", "Time Management", "Creativity", "Critical Thinking", "Other"))
    if "Other" in st.session_state.strength:
        other=st.text_input("If other, please specify",key="other_strength")
        st.session_state.strength.append(other)
    st.session_state.hobby=st.multiselect("Select your hobbies", ("Reading", "Traveling", "Cooking", "Sports", "Music", "Art", "Other"))
    if "Other" in st.session_state.hobby:
        other=st.text_input("If other, please specify",key="other_hobby")
        st.session_state.hobby.append(other)
st.subheader("Resume themes:")
st.session_state.theme = st.selectbox("Select a resume theme", ("Classic", "Modern"))        
def classic():
    return f"""
    <html>
    <head>

    <style>

    @page {{
        size: A4;
        margin: 10mm;
    }}

    body {{
        font-family: Arial, sans-serif;
        color: #222222;
        line-height: 1.5;
        font-size: 12px;
    }}

    h1 {{
        color: #0F766E;
        margin-bottom: 5px;
        font-size: 28px;
    }}

    h2 {{
        color: #0F766E;
        border-bottom: 1px solid #0F766E;
        padding-bottom: 4px;
        margin-top: 18px;
        font-size: 18px;
    }}

    p {{
        margin: 5px 0;
    }}

    ul {{
        margin: 5px 0;
        padding-left: 18px;
    }}

    .header {{
        text-align: center;
        margin-bottom: 20px;
    }}

    .contact {{
        text-align: center;
        font-size: 11px;
    }}

    .section {{
        margin-bottom: 15px;
    }}

    </style>

    </head>

    <body>

    <div class="header">
        <h1>{st.session_state.name}</h1>

        <div class="contact">
            {st.session_state.email} |
            {st.session_state.phone} |
            {st.session_state.location}
        </div>

        <div class="contact">
            LinkedIn: {st.session_state.linkedin}
        </div>

        <div class="contact">
            {st.session_state.job_role}
        </div>
    </div>

    <div class="section">
        <h2>Personal Information</h2>

        <p><b>Date of Birth:</b> {st.session_state.dob}</p>
        <p><b>Gender:</b> {st.session_state.gender}</p>

        <p><b>Languages:</b></p>

        <ul>
            {"".join(f"<li>{lang}</li>" for lang in st.session_state.language)}
        </ul>
    </div>

    <div class="section">
        <h2>Education</h2>

        <p>
        <b>{st.session_state.High}</b> in
        {st.session_state.field}
        from
        {st.session_state.college}
        ({st.session_state.graduation_year})
        </p>

        <p>
        <b>{st.session_state.inter}</b> in
        {st.session_state.field_12}
        from
        {st.session_state.college_12}
        ({st.session_state.graduation_12})
        </p>

        <p>
        <b>{st.session_state.high_s}</b>
        from
        {st.session_state.school_10}
        ({st.session_state.graduation_year_10})
        </p>
    </div>

    <div class="section">
        <h2>Skills</h2>

        <ul>
            {"".join(f"<li>{skill}</li>" for skill in st.session_state.skill)}
        </ul>
    </div>

    <div class="section">
        <h2>Project</h2>

        <p><b>{st.session_state.project}</b></p>

        <p>{st.session_state.project_descript}</p>
    </div>

    <div class="section">
        <h2>Internship</h2>

        <p><b>{st.session_state.internship}</b></p>

        <p>{st.session_state.internship_descript}</p>
    </div>

    <div class="section">
        <h2>Strengths</h2>

        <ul>
            {"".join(f"<li>{strength}</li>" for strength in st.session_state.strength)}
        </ul>
    </div>

    <div class="section">
        <h2>Hobbies</h2>

        <ul>
            {"".join(f"<li>{hobby}</li>" for hobby in st.session_state.hobby)}
        </ul>
    </div>

    <div class="section">
        <h2>Declaration</h2>

        <p>
        I hereby declare that the above information is true and correct
        to the best of my knowledge.
        </p>
    </div>

    </body>
    </html>
    """
def modern():
    return f"""
    <html>
    <head>
    <title>resume</title>    
    <style>
        @page{{
            size: A4;
            margin: 10mm;
        }}
        table{{
        border-collapse: collapse;
        }}
        .head{{
            background-color: #0F766E;
            padding: 10px;
            text-align: left;
        }}
        .left{{
        background-color: #14B8A6;
        padding: 10px;
        }}
        .right{{
        background-color: #CCFBF1;
        padding: 10px;
        }}
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
        }}
        h1{{
            color: #333;
        }}
        .template-list {{
            list-style-type: none;
            padding: 0;
        }}
        .template-item {{
            background-color: #f9f9f9;
            border: 1px solid #ddd;
            padding: 10px;
            margin-bottom: 10px;
            border-radius: 5px;
        }}
        .template-item h2 {{
            margin-top: 0;
        }}
        .template-item p {{
            margin: 5px 0;
        }}
    </style>
</head>
<body style="padding: 20px;">
<div>
    <div class="head">
        <h1>{st.session_state.name}</h1>
        <h2>{st.session_state.job_role}</h2>
    </div>
</div>
<table width="100%" cellspacing="0" cellpadding="0">
<tr>    <td class="left" width="25%" valign="top">
        <h2>PERSONAL INFO:</h2>
        <p>{st.session_state.email}</p>
        <p>{st.session_state.phone}</p>
        <p>{st.session_state.location}</p>
        <p>{st.session_state.linkedin}</p>
        <p>Gender:{st.session_state.gender}</p>
        <hr>
        <h2>SKILLS:</h2>
        <p style="list-style-type: disc; padding-left: 20px;">{"".join(f"<ul><li>{s}</li></ul>" for s in st.session_state.skill)}</p>
    </div>
    <td class="right" width="75%" valign="top">
        <h2>EDUCATION:</h2>
        <div>
        <p>{st.session_state.High} in {st.session_state.field} at {st.session_state.college} during {st.session_state.graduation_year}</p>
        <p>{st.session_state.inter} in {st.session_state.field_12} at {st.session_state.college_12} during {st.session_state.graduation_12}</p>
        <p>{st.session_state.high_s} at {st.session_state.school_10} during {st.session_state.graduation_year_10}</p>
        </div>
        <hr>
        <h2>PROJECT:</h2>
        <p>Name:{st.session_state.project}</p>
        <p>{st.session_state.project_descript}</p>
        <hr>
        <h2>INTERNSHIP:</h2>
        <p>Name:{st.session_state.internship}</p>
        <p>{st.session_state.internship_descript}</p>
        <hr>
        <h2>STRENGTHS:</h2>
        <p>{", ".join(st.session_state.strength)}</p>
        <hr>
        <h2>HOBBIES:</h2>
        <p >{", ".join(st.session_state.hobby)}</p>
        <hr>
        <h2>DECLARATION:</h2>
        <p>I hereby declare that the above information is true and correct to the best of my knowledge.</p>
    </td>
</tr>
</table>   
</body>
</html>
    """ 
          
if st.button("Generate Resume"):
    if st.session_state.theme== "Classic":
        st.session_state.gen=classic()
    elif st.session_state.theme=="Modern":
        st.session_state.gen=modern()
if st.session_state.gen:

    st.components.v1.html(
        st.session_state.gen,
        height=1300,
        width=860,
        scrolling=True
    )

    st.success("Resume generated successfully!")

    with open("resume.pdf", "wb") as pdf_file:
        pisa.CreatePDF(
            st.session_state.gen,
            dest=pdf_file
        )

    with open("resume.pdf", "rb") as f:
        col1,col2=st.columns(2)
        with col1:    
            st.download_button(
            "Download Pdf",use_container_width=True,
            data=f,
            file_name="resume.pdf",
            mime="application/pdf"
        )
        with col2:
            st.download_button(
        "Download HTML",use_container_width=True,
        data=st.session_state.gen,
        file_name=f"{st.session_state.name}.resume_html",
        mime="text/html"
        )        
        
                
               
