import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import graphviz
from io import StringIO

# LinkedList implementation for visualization
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def display(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(current.data)
            current = current.next
        return nodes
    
    def visualize(self):
        dot = graphviz.Digraph()
        current = self.head
        i = 0
        
        while current:
            dot.node(f'node_{i}', str(current.data))
            if i > 0:
                dot.edge(f'node_{i-1}', f'node_{i}')
            current = current.next
            i += 1
        
        return dot

# Streamlit app
def main():
    st.set_page_config(page_title="Data Analytics Dashboard", layout="wide")
    st.title("Data Analytics Dashboard with Data Structure Visualizations")
    
    # Sidebar controls
    st.sidebar.header("Controls")
    
    # DataFrame section
    st.header("DataFrame Visualization")
    
    # Create sample DataFrame
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 40, 45],
        'Score': [85, 92, 78, 88, 95]
    }
    df = pd.DataFrame(data)
    
    # Display DataFrame
    st.subheader("Sample DataFrame")
    st.dataframe(df)
    
    # DataFrame statistics
    st.subheader("DataFrame Statistics")
    st.write(df.describe())
    
    # DataFrame visualization
    st.subheader("Data Visualization")
    chart_type = st.selectbox("Select chart type", ["Bar Chart", "Line Chart", "Scatter Plot"])
    
    if chart_type == "Bar Chart":
        fig, ax = plt.subplots()
        df.plot(kind='bar', x='Name', y='Score', ax=ax)
        st.pyplot(fig)
    elif chart_type == "Line Chart":
        fig, ax = plt.subplots()
        df.plot(kind='line', x='Name', y='Score', ax=ax)
        st.pyplot(fig)
    elif chart_type == "Scatter Plot":
        fig, ax = plt.subplots()
        df.plot(kind='scatter', x='Age', y='Score', ax=ax)
        st.pyplot(fig)
    
    # LinkedList section
    st.header("LinkedList Visualization")
    
    # LinkedList controls
    col1, col2 = st.columns(2)
    with col1:
        ll_input = st.text_input("Add items to LinkedList (comma separated)", "1,2,3,4,5")
    with col2:
        st.write("")  # Spacer
    
    # Create LinkedList
    ll = LinkedList()
    items = [x.strip() for x in ll_input.split(',') if x.strip()]
    for item in items:
        ll.append(item)
    
    # Display LinkedList
    st.subheader("LinkedList Contents")
    st.write(ll.display())
    
    # Visualize LinkedList
    st.subheader("LinkedList Structure")
    dot = ll.visualize()
    st.graphviz_chart(dot)
    
    # Data structure explanation
    st.header("About Data Structures")
    with st.expander("Learn about DataFrames"):
        st.write("""
        A DataFrame is a 2-dimensional labeled data structure with columns of potentially different types. 
        It is similar to a spreadsheet or SQL table, or a dictionary of Series objects.
        """)
    
    with st.expander("Learn about LinkedLists"):
        st.write("""
        A LinkedList is a linear data structure where each element is a separate object. 
        Each element (node) of a list consists of two items - the data and a reference to the next node.
        """)

if __name__ == "__main__":
    main()
