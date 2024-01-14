from pathlib import Path
import streamlit as st
from PIL import Image

#--Path settings
current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
css_file = current_dir/'styles'/'main.css'
resume_file = current_dir / 'assets' / 'CV_NguyenDucTuanDat.pdf'
profile_pic = current_dir/'assets'/'tuandat1.png'


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Nguyen Duc Tuan Dat"
PAGE_ICON = ":wave:"
NAME = "Nguyen Duc Tuan Dat"
DESCRIPTION = """
Data Scientist | Data Analyst
"""
EMAIL = "ndtdat.data@email.com"
SOCIAL_MEDIA = {
    # "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com/DBlue04",
    "Facebook": "https://www.facebook.com/ndtdat.3k/",
    "LinkedIn": 'https://www.linkedin.com/in/%C4%91%E1%BA%A1t-nguy%E1%BB%85n-941983262/',
    "Kaggle": "https://www.kaggle.com/nguyenductuandat"
}
SMALL_PROJECTS = {
    "🏆 Survey and predict the stock of Tesla in the future using yfinance and LTSM model": "https://github.com/DBlue04/stock_market_with_big4",
    "🏆 Survey customer satisfaction from flights": "https://github.com/DBlue04/programmingfords",
    "🏆 Analyzing Air Pollution in Vietnam": "https://github.com/ImPhatDat/FinalProject-Intro2DS"
}

BIG_PROJECTS = {
    
}
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- Education ---
st.write('\n')
st.subheader("Education")
st.write("---")
st.write(
    """
- :book: VNU-HCM UNIVERSITY OF SCIENCE - 2021 to Present
"""
)

# --- Certificates ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write("---")
st.write(
    """
- :crown: Google Data Analytics (10/08/2023)
- :crown: Data Analyst with Python (03/09/2023)
"""
)


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write("---")
st.write(
    """
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write("---")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas,...), SQL, C++
- 📊 Data Visulization: Tableau, PowerBI, MS Excel, Plotly
- 📚 Modeling: Logistic Regression, Linear Regression, Decision trees, LSTM
- 🗄️ Databases: MySQL
"""
)


# --- WORK HISTORY ---
# st.write('\n')
# st.subheader("Work History")
# st.write("---")

# # --- JOB 1
# st.write("🚧", "**Senior Data Analyst | Ross Industries**")
# st.write("02/2020 - Present")
# st.write(
#     """
# - ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
# - ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
# - ► Redesigned data model through iterations that improved predictions by 12%
# """
# )

# # --- JOB 2
# st.write('\n')
# st.write("🚧", "**Data Analyst | Liberty Mutual Insurance**")
# st.write("01/2018 - 02/2022")
# st.write(
#     """
# - ► Built data models and maps to generate meaningful insights from customer data, boosting successful sales eﬀorts by 12%
# - ► Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of $300K
# - ► Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing
# """
# )

# # --- JOB 3
# st.write('\n')
# st.write("🚧", "**Data Analyst | Chegg**")
# st.write("04/2015 - 01/2018")
# st.write(
#     """
# - ► Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc
# - ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
# - ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
# """
# )


# --- Small project ---
st.write('\n')
st.subheader("Small projects")
st.write("---")
for project, link in SMALL_PROJECTS.items():
    st.write(f"[{project}]({link})")
    
# --- Big project ---
st.write('\n')
st.subheader("Big projects")
st.write("---")
for project, link in BIG_PROJECTS.items():
    st.write(f"[{project}]({link})")