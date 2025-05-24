   import pandas as pd
   import matplotlib.pyplot as plt
   import streamlit as st

   # Streamlit Interface
   st.title("CSV Data Visualizer")

   # File Upload
   uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

   if uploaded_file:
       # Read CSV into DataFrame
       df = pd.read_csv(uploaded_file)
       st.write("Data Preview:", df.head())

       # Select visualization type
       chart_type = st.selectbox("Select visualization type", ["Histogram", "Bar Chart", "Pie Chart", "Line Diagram"])

       # Column selection based on the chart type
       if chart_type == "Histogram":
           column = st.selectbox("Select Column", df.columns)
           if st.button("Visualize"):
               plt.hist(df[column].dropna())
               st.pyplot(plt)

       elif chart_type == "Bar Chart":
           x_column = st.selectbox("X-Axis Column", df.columns)
           y_column = st.selectbox("Y-Axis Column", df.columns)
           if st.button("Visualize"):
               plt.bar(df[x_column], df[y_column])
               st.pyplot(plt)

       elif chart_type == "Pie Chart":
           column = st.selectbox("Select Column", df.columns)
           if st.button("Visualize"):
               plt.pie(df[column].value_counts(), labels=df[column].value_counts().index)
               st.pyplot(plt)

       elif chart_type == "Line Diagram":
           x_column = st.selectbox("X-Axis Column", df.columns)
           y_column = st.selectbox("Y-Axis Column", df.columns)
           if st.button("Visualize"):
               plt.plot(df[x_column], df[y_column])
               st.pyplot(plt)
   
