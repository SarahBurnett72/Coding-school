#"""
#Now, let’s build something practical—a Researcher Profile Page. This app will showcase a researcher’s details, including their name, field of study, publications, and an interactive section for exploring their work.

#Stop the current `app.py` file in your terminal from running by pressing CTRL+C a few times.

#Now in Spyder create a new app called `app_profile.py`, copy the code below to this file
#"""


import streamlit as st
import pandas as pd

# Title of the app
#st.title("Researcher Profile Page")

# Set page title
st.set_page_config(page_title="Researcher Profile", layout="wide")

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Researcher Profile", "What is biophysics?", "Science communication", "Contact"],
)

if menu == "Researcher Profile":
    # Collect basic information
    name = "Sarah Burnett"
    field = "Biophysics"
    institution = "University of Pretoria"
    
    
    # Display basic profile information
    st.header("Researcher Overview")
    col1, col2 = st.columns(2)
    
    with col1:
        st.write(" ")
        st.write(" ")
        st.write(f"**Name:** {name}")
        st.write(f"**Field of Research:** {field}")
        st.write(f"**Institution:** {institution}")
    
    with col2:
        st.image('6-IMG_8246.jpg', width=250)

    st.write("Climate change has caused extreme heat waves to increase in intensity and frequency. This has a severe negative impact on crop yield and therefore food production. My project aims to investigate the growth response of wheat to high temperature stress, using hyperspectral imaging and sun-induced chlorophyll fluorescence, as well as various biological and chemical techniques. I aim to identify the physiological and quantum mechanical mechanisms of the plant’s response to heat stress, as well as plant adaptation strategies to heat waves. This knowledge can be used to inform the development of adaptive cultivation techniques to mitigate yield loss in high temperature conditions. This project is an exciting look into the intersection between physics, biology and chemistry and will investigate the effects of non-trivial physics in the context of a complex biological system.")
    

elif menu == "What is biophysics?":
    st.header("What is biophysics?")
    st.write("Biophysics is a vibrant, interdisciplinary field that brings together scientists from fields such as physics, biology, chemistry, maths, and material science to share their skills and develop new tools for understanding how biology works. Biophysicists study life at every level, from the molecular level up to entire ecosystems. They develop new experimental and computational methods to understand all aspects of biological systems at a fundamental level, solving scientific mysteries in the process. Biophysicists push the scientific envelope to answer questions that have remained unanswered and solve the problems of the future.")
    #Section for research field
    st.write("Learn more about the research group I belong to by following the link below:")
    st.link_button("Research Group website", 'https://biophysicsup.netlify.app/research/')


elif menu == "Science communication":
    st.write("I ")
elif menu == "Contact":
    st.header("Contact Information")
    name = "Sarah Burnett"
    email = "jane.doe@example.com"
    st.write(f"You can reach {name} at {email}.")
# Add a section for publications
#st.header("Publications")
#uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

#if uploaded_file:
    #publications = pd.read_csv(uploaded_file)
    #st.dataframe(publications)

    # Add filtering for year or keyword
    #keyword = st.text_input("Filter by keyword", "")
    #if keyword:
       # filtered = publications[
            #publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        #]
        #st.write(f"Filtered Results for '{keyword}':")
        #st.dataframe(filtered)
    #else:
        #st.write("Showing all publications")

#Add a section for visualizing publication trends
#st.header("Publication Trends")
#if uploaded_file:
    #if "Year" in publications.columns:
        #year_counts = publications["Year"].value_counts().sort_index()
        #st.bar_chart(year_counts)
   # else:
        #st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add a contact section


#st.header("Coding School instructions")
#st.write("Here I have stored the instructions from Canvas")
#"""
#Basic Inputs for Profile Details:

#- The st.text_input() widget lets users enter their name, field of study, and institution. These inputs update the displayed profile dynamically.

#Displaying Publications:

#- The st.file_uploader() widget allows researchers to upload a CSV of their publications. We use Pandas to read the file and display it as a table with st.dataframe().

#Filtering Publications:

#- To add interactivity, we let users filter the publications by keyword. The apply() function searches for the keyword across all columns in the DataFrame, making it flexible for various data formats.

#Visualizing Trends:

#- If the uploaded CSV contains a "Year" column, we use Streamlit’s built-in st.bar_chart() to visualize the number of publications per year. This provides a quick way to analyze research output.

#Contact Information:

#- The app ends with a contact section, where researchers can share their email address.
#"""
