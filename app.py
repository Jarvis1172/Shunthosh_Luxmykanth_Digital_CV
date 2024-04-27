from pathlib import Path

import streamlit as st
from PIL import Image

## Path settings
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Shunthosh Luxmykanth CV 2024.pdf"
profile_pic = current_dir / "assets" / "ProfilePic.png"

## General Settings

page_title = "Digital Resume | Shunthosh Luxmykanth "
icon = ":eyeglasses:"
name = "Shunthosh Luxmykanth"
desc = "Having completed my Data Science and Business Analytics degree at the University of London, I bring over a year of experience as a Data Analyst at Stax. With a solid foundation in both academia and practical work, I'm equipped to contribute effectively to the team. Eager to continue learning and adapting, I am committed to adding value to the organisation through my skills and expertise."

email = "shunthosh2001@gmail.com"

social_media = {
    "LinkedIn" : "https://www.linkedin.com/in/shunthoshluxmykanth2001?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BchB8CSYpRgyNy3SHiRtn0w%3D%3D",
    "GitHub" : "https://github.com/Jarvis1172",
    "Instagram" : "https://www.instagram.com/shunthosh22/"

}


    

## Page 

st.set_page_config(page_title = page_title, page_icon = icon)

## Load css
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html = True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)


## Head Section
col1, col2 = st.columns(2, gap = "small")

with col1:
    st.image(profile_pic, width = 230)


with col2:
    st.title(name)
    st.write(desc)
    st.download_button(
        label = "📄 Download CV",
        data = PDFbyte,
        file_name = resume_file.name,
        mime = "application/octet-stream",
    )

    st.write(":e-mail:", email)


## Social Media

st.write("#")
cols  = st.columns(len(social_media))

for index, (platform,link) in enumerate (social_media.items()):
    cols[index].write(f"[{platform}]({link})")

## Experience

st.write("#")
st.subheader("Expereince & Qualifications")

st.write(
    """

    - 💼 Data Analyst at Stax LLC
    - 💼 Mathematics Lecturer at Royal Institute
    - 💼 Freelance Programming Lecturer at Blacboard
    - 💵 Private Mathematics & ICT Tutor
    - 💵 Freelance Data Analyst

    - 🎓 MSc Business Analytics, Robert Gordon University
    - 🎓 BSc Data Science & Business Analytics, University of London
    - 🎓 Assured Diploma in Information Technology (DITECH), Esoft Metro Campus 
    - 🎓 GCE Advanced Level, Royal Institute
    - 🎓 GCE Ordinary Level, Royal Institute
    """
)

## Skills

st.write("#")
st.subheader("Skills")


st.write(
    """

    - 👨🏾‍💻 Programming: Python, R
    - 🤖 AI: Prompt Engineering
    - 📊 Data Visualization: Excel, Tableau, QGIS
    - 🗃️ Databases: SQL
    - ⛏️ Web Scrapping - Selenium
    - 🌐 Web Apps - Streamlit
    



    """
)

## Courses

st.write("#")
st.subheader("Courses")


st.write(
    """

    - 👨🏾‍💻 Introduction to R Programming COMPLETE
    - 📈 Stax Academy: An introduction to strategy consulting COMPLETE
    - 🤖 Udemy: Basics of Machine Learning in Python & R IN PROGRESS
    - 🤖 DeepLearning.AI: LangChain for LLM Application Developmen

    



    """
)

## Projects

st.write("#")
st.subheader("Projects")
st.write("---")

st.write("🏆", "**Customer Review Theme Classification with OpenAI API**")
st.write("01/2024 - Present")
st.write("""

- Using OpenAI API to classify reviews based on **themes** using Prompt engineering.
- Applying Hugging Face transformers to predict the **sentiment** (positive or negative) of the review 


""")

## Work history

st.write("#")
st.subheader("Work History")
st.write("---")

st.write("💼", "**Data Analyst | Stax LLC**")
st.write("11/2022 - Present")
st.write("""

- Used Seleinum and BeautifulSoup4 conduct web scrapping for analysis focussing on TAM estimation, Sentiment analysis.
- Conducted Sentiment analysis using Python and Excel.
- Conducted AI initiatives to classify reviews based on **themes** using Prompt engineering with OpenAI API.
- Created LinkedIn automation tools, to reduce manual tasks by 80%.
- Visualized multi location maps using QGIS

""")


st.write("#")
st.write("💼", "**Mathematics Lecturer | Royal Institute**")
st.write("02/2019 - 02/2020")
st.write("""

- Responsible for lecturing Mathematics for grade 9 students of Royal Institute.
- Taught 10+ students showcasing exceptional grades on GSCE O/L examinations.

""")

st.write("#")
st.write("💵", "**Freelance Programming Lecturer | Blackboard**")
st.write("02/2024 - Present")
st.write("""

- Responsible for tutoring Programming for Data Science for undergraduates of University of London.
- Assisted students with projects involving data analysis using Pythons.

""")

st.write("#")
st.write("💵", "**Private Mathematics & ICT Tutor**")
st.write("06/2019 - Present")
st.write("""

- Responsible for tutoring Mathematics & ICT for English medium students of grades 8 to Ordinary Level.
- Taught 20+ students showcasing exceptional grades on GSCE O/L examinations and other examinations.

""")

st.write("#")
st.write("💵", "**Freelance Data Analyst**")
st.write("02/2024 - Present")
st.write("""

- Conducted review sscrapes and preliminary ratings analysis using tools such as Python,Excel.
- Completed a Ratings Analysis for TearDrop group of Hotels and competitors.

""")

## Education 

st.write("#")
st.subheader("Education")
st.write("---")

st.write("🎓", "**MSc Business Analytics | Robert Gordon University**")
st.write("01/2024 - Present")
st.write("""

- Currently following Statistics for Business Analytics and Business Modelling and Analytics modules.
- Upcoming modules include: 

  Introduction to Big Data and Data Science
 
  Data Management
  
  Business Intelligence Tools and Applications 
  
  Data Warehousing 
  
  Research Methods 
  
  Web Mining

- Expected to publish a Project on a real-life application of Business Analytics

""")


st.write("#")
st.write("🎓", "**BSc Data Science & Business Analytics | University of London**")
st.write("09/2019 - 08/2023")
st.write("""

- Second Class Honours
- Modules:
  
  Introduction to economics (EC1002)

  Statistics 1 (ST104a - Half course)

  Statistics 2 (ST104b - Half course)
  
  Mathematical Methods (MT1186)

  Business analytics, applied modelling and prediction (ST2187)

  Machine learning (ST3189)

  Advanced statistics: distribution theory (ST2133 - Half course)

  Advanced statistics: statistical inference (ST2134 - Half course)

  Programming for data science (ST2195)

  Information systems management (IS2184)


- Projects:

  🏆 Programming for data science (ST2195) - Data analysis of Aircraft Delays for the Harvard Airline Expo 2006 datasets
  
  🏆 Machine learning (ST3189) -  Simple Linear Regression and Classification exercises


  

""")

st.write("#")
st.write("🎓", "**Assured Diploma in Information Technology (DITECH) | Esoft Metro Campus**")
st.write("09/2019 - 05/2021")
st.write("""

- Modules:

  Information Technology Concepts	

  Enhancing Productivity with MS Office	

  Computer Hardware	

  Network Technology	

  Internet, Email & Web Design	

  Graphics and Multimedia	

  Software Engineering	

  Programming with Python

  Databases with SQL	

  Programming with C# 	

""")

st.write("🎓", "**GCE Advanced Level | Royal Institute**")
st.write("09/2017 - 09/2019")
st.write("""
- Results:

  Mathematics (Pure Mathematics & Statistics)  – B
  
  Accounting                                   - B
  
  Economics                                    - C
""")

st.write("🎓", "**IELTS | British Council Sri Lanka**")
st.write("09/2019")
st.write("""
- Results:

  Listening - 7.5

  Reading  - 6.5

  Writing - 5.5

  Speaking - 7.5

- **Overal score - 7**

""")



st.write("🎓", "**GCE Ordinary Level | Royal Institute**")
st.write("09/2016 - 09/2017")
st.write("""
- Results:

  Mathematics         - A
  
  Computer Science   - A
  
  Biology             - A
  
  Chemistry          - A
  
  Physics              - B
  
  Commerce          - B
  
  English Language - D
""")
