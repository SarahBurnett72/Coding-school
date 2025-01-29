import streamlit as st

st.title("Streamlit demo!")

#%%%
"""
Any changed you make to your code save the file in Spyder or your IDE. In cases you need to refresh your browser to see changes take 
effect.

Streamlit lets you create widgets like sliders, text inputs, and buttons with just a line of code. For example:
"""

number = st.slider("Pick a number", 1, 100)
st.write(f"You picked: {number}")

"""
These widgets are automatically synchronized, meaning they update in real-time as you interact with them.

In Streamlit, you can add headings using the st.title(), st.header(), st.subheader(), and st.markdown() functions.

Here is an example:
"""

st.title("Title heading")

st.write("Hello, Streamlit!")

st.header("Header")
st.write("Let's figure out paragraphs /n Is it a new line? Nope. weird")

#%%
"""
Streamlit integrates seamlessly with libraries like Matplotlib, Plotly, and Pandas. You can create beautiful, interactive 
visualizations directly in your app. For example:
"""
import pandas as pd
import plotly.express as px

st.header("Sample Data")

data = pd.DataFrame({"x": [1, 2, 3], "y": [10, 20, 30]})

# Display the data in the Streamlit app
st.write(data)

# Create a Plotly figure
fig = px.line(data, x="x", y="y", title="Simple Plotly Example")

# Display the plot in the Streamlit app
st.plotly_chart(fig)