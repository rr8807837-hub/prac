import streamlit as st
import base64
import pdfkit
st.set_page_config(page_title="Resume Generator", page_icon=":briefcase:", layout="wide",initial_sidebar_state="collapsed")
# session state
if "generated" not in st.session_state:
    st.session_state.generated = False
if "resume_html" not in st.session_state:
    st.session_state.resume_html = ""
st.title("Resume Generator")
st.write("Hello! I'm your resume generator. Please fill in the details to create your resume.")
st.sidebar.title("Provide your Details Here",width=500)

#widgets for user input
name = st.sidebar.text_input("Full Name")
email = st.sidebar.text_input("✉️Email")
phone = st.sidebar.text_input("📞Phone Number")
linkedin = st.sidebar.text_input("🔗LinkedIn Profile url(optional)")
github = st.sidebar.text_input("🔗GitHub Profile(optional)")
st.sidebar.subheader("Gender")
gender = st.sidebar.radio("Select Gender", ("Male", "Female", "Other")) 
st.sidebar.subheader("📍Location")
location = st.sidebar.text_input("City, State,pin code")
st.sidebar.subheader("🎓Education details:")
High=st.sidebar.selectbox("Select your highest qualification", ("High School Diploma", "Associate Degree", "Bachelor's Degree", "Master's Degree", "Btech", "PhD", "Other"))
if High == "Other":
    other11=st.sidebar.text_input("If other, please specify")
    High = other11
college = st.sidebar.text_input("Enter your University/College Name")
field= st.sidebar.text_input("Enter your Field/stream of study")
graduation_year = st.sidebar.text_input("Enter your Graduation Year(Eg:2020-2023)")
st.sidebar.divider()
st.sidebar.subheader("Enter your 12th details:")
inter=st.sidebar.selectbox("Board Name", ("Intermediate CBSE", "ICSE", "Intermediate State Board", "Other"),key="inter")
if inter == "Other":
    other1=st.sidebar.text_input("If other, please specify")
    inter = other1
college_12 =st.sidebar.text_input("Enter your School/College Name",key="college_12")
field_12=st.sidebar.text_input("Enter your Field/stream of study (Eg:BIPC/MPC/CEC/Other)",key="field_12")
if field_12 == "Other":
    other2 =st.sidebar.text_input("If other, please specify")
    field_12 = other2 
graduation_12 = st.sidebar.text_input("Enter your Graduation Year(Eg:2020-2022)",key="graduation_12")
st.sidebar.divider()
st.sidebar.subheader("Enter your 10th details:")
high_s=st.sidebar.selectbox("Board Name", ("CBSE", "ICSE", "SSC", "Other"),key="high_s")
if high_s == "Other":
    other3=st.sidebar.text_input("If other, please specify")
    high_s = other3
school_10 = st.sidebar.text_input("Enter your School Name",key="school_10")
graduation_year_10 = st.sidebar.text_input("Enter your Graduation Year(Eg:2020-2023)",key="graduation_year_10")
st.sidebar.divider()
job_role = st.sidebar.selectbox("Job Role", ("Software Engineer",
                                             "Data Scientist", 
                                             "Product Manager", 
                                             "UX Designer",
                                             "web developer",
                                             "mobile app developer",
                                             "Data Analyst",
                                             "Machine Learning Engineer",
                                             "DevOps Engineer", 
                                             "Other"))
if job_role == "Other":
    other=st.sidebar.text_input("If other, please specify")
    job_role = other        
st.sidebar.subheader("Skills:")
skill=st.sidebar.multiselect("Select your skills", ("Python", "Java", "C++", "SQL", "Machine Learning", "Data Analysis", "Web Development", "Mobile App Development", "Cloud Computing", "Other"))
if "Other" in skill:
    other=st.sidebar.text_input("If other, please specify",key="other_skill")
    skill.append(other)
st.sidebar.subheader("Project details:")    
project=st.sidebar.text_input("project name:",key="project_name")    
project_descript=st.sidebar.text_area("Describe your project (Includes description, technologies used, and your role in the project)")
intern=st.sidebar.subheader("Internship details:")
internship=st.sidebar.text_input("Internship name:",key="internship_name")
internship_descript=st.sidebar.text_area("Describe your internship experience (Includes description, technologies used, and your role in the internship)")
strength=st.sidebar.multiselect("Select your strengths", ("Problem Solving", "Teamwork", "Communication", "Adaptability", "Leadership", "Time Management", "Creativity", "Critical Thinking", "Other"))
if "Other" in strength:
    other=st.sidebar.text_input("If other, please specify",key="other_strength")
    strength.append(other)
hobby=st.sidebar.multiselect("Select your hobbies", ("Reading", "Traveling", "Cooking", "Sports", "Music", "Art", "Other"))
if "Other" in hobby:
    other=st.sidebar.text_input("If other, please specify",key="other_hobby")
    hobby.append(other)
photo=st.sidebar.file_uploader("Upload your photo (optional)",type=["jpg","jpeg","png"],key="photo")
if photo:
    photo_data = photo.read()
    encoded = base64.b64encode(photo_data).decode("utf-8")
    photo = f"data:{photo.type};base64,{encoded}"
else:
    photo="https://www.pngall.com/wp-content/uploads/5/Profile-PNG-High-Quality-Image.png"

st.sidebar.subheader("Resume themes:")
theme = st.sidebar.selectbox("Select a resume theme", ("Classic", "Modern", "Creative"))
def classic_template():
    return f"""
    <html>
    <body style="font-family: Arial;">
        <h1>PERSONAL INFORMATION</h1>
        <h1>{name}</h1>
        <p>{email} | {phone} | {location}</p>
        <p><b>{job_role}</b></p>
        <div>
        <img src="{photo}" style="height:150px; width:150px; border-radius:50%; border:2px solid #000;">
        </div>
        <h2>Contact</h2>
        <p>{email} | {phone} | {location}</p>

        <h2>Education</h2>
        <p>{High} - {college} ({graduation_year})</p>

        <h2>Skills</h2>
        <p>{", ".join(skill)}</p>
    </body>
    </html>
    """

def modern_template():
    return f"""
    <html>
<head>
    <title>Project Templates</title>    
    <style>
        .head{{
            background-color: #0F766E;
            padding: 10px;
            text-align: left;
            width: 70%;
        }}
        .left{{
            height: 1000px;
            width: 70.7%;
            background-color: #14B8A6;
            padding: 20px;
        }}
        .right{{
            height: 1000px;
            width: 70.7%;
            background-color: #CCFBF1;
            padding: 20px;
        }}
        .img{{
            background-color: aqua;
            display: flex;
            gap: 0px;
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
<body style="height: 297mm; width: 210mm; padding: 20px; align-items: center; justify-content: center;">
<div style="display: flex; gap:0px">
    <div style="width: 32%; display: flex; justify-content: center; align-items: center; background-color: #0F766E;">
    <img src="{photo}" style="height:150px; width:150px; border-radius:50%; border:2px solid #000; object-fit: cover;">     
    </div>
    <div class="head">
        <h1>{name}</h1>
        <h2>{job_role}</h2>
    </div>
</div>
<div style="display: flex;gap:0px;">
    <div class="left" style="width: 30%;">
        <h2>PERSONAL INFO:</h2>
        <p>✉️{email}</p>
        <p>📞{phone}</p>
        <p>📍{location}</p>
        <p>🔗{linkedin}</p>
        <p>Gender:{gender}</p>
        <hr>
        <h2>SKILLS:</h2>
        <p style="list-style-type: disc; padding-left: 20px;">{"".join(f"<li>{s}</li>" for s in skill)}</p>
    </div>
    <div style="height: 1000px;
            width: 1px;
            background-color: black;"></div>
    <div class="right" style="width: 70%;">
        <h2>EDUCATION:</h2>
        <div>
        <p>💠{High or other11} in {field} at {college} during {graduation_year}</p>
        <p>💠{inter or other1} in {field_12} at {college_12} during {graduation_12}</p>
        <p>💠{high_s or other3} at {school_10} during {graduation_year_10}</p>
        </div>
        <hr>
        <h2>PROJECT:</h2>
        <p>Name:{project}</p>
        <p>{project_descript}</p>
        <hr>
        <h2>INTERNSHIP:</h2>
        <p>Name:{internship}</p>
        <p>{internship_descript}</p>
        <hr>
        <h2>STRENGTHS:</h2>
        <p>➡️{", ".join(strength)}</p>
        <hr>
        <h2>HOBBIES:</h2>
        <p >➡️{", ".join(hobby)}</p>
        <hr>
        <h2>DECLARATION:</h2>
        <p>I hereby declare that the above information is true and correct to the best of my knowledge.</p>
    </div>
</div>    
</body>
</html>
    """
    
def creative_template():
    return f"""
    <html>
    <body style="font-family: Georgia; background:#222; color:white; padding:20px;">
        <h1 style="color:#00adb5;">{name}</h1>
        <p>{job_role}</p>

        <hr>

        <h2>Skills</h2>
        <p>{", ".join(skill)}</p>

        <h2>Projects</h2>
        <p>{project}</p>
    </body>
    </html>
    """        
if st.sidebar.button("Generate Resume",use_container_width=True):
    st.toast("resume generated successfully!",icon="✅")
    st.balloons()
    if theme == "Classic":
        resume_html = classic_template()
    elif theme == "Modern":
        resume_html = modern_template()

    elif theme == "Creative":
        resume_html = creative_template()
    st.session_state.resume_html = resume_html
    st.session_state.generated = True
    st.set_page_config(initial_sidebar_state="collapsed")


# preview (outside button)
if st.session_state.generated:
    st.components.v1.html(st.session_state.resume_html, height=1300, width=860, scrolling=True)
    st.success("Resume generated successfully!")

if st.session_state.generated:
    st.sidebar.download_button(
        "Download Resume",use_container_width=True,
        data=st.session_state.resume_html,
        file_name=f"{name}_resume.html",
        mime="text/html"
    )
    