import streamlit as st
import pandas as pd
import time

def load_data():
    return pd.read_csv('test.csv')

def main():
    st.title(" >> Netflix Movies Search Engine <<")
    data = load_data()

    # Create a text input for the user to enter the search query
    search_query = st.text_input("Enter your search query:")

    # Display the search query entered by the user
    st.write(f"You entered: {search_query}")

    # Filter data based on the search query
    filtered_data = data[data['title'].str.contains(search_query, case=False, na=False)]

    # Display the filtered data below the search box
    st.dataframe(filtered_data)

if __name__ == "__main__":
    main()