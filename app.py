
import streamlit as st
import pandas as pd
import sqlite3

def main():
    st.title("Weather Data Viewer")

    # Connect to SQLite database
    conn = sqlite3.connect('data.db')

    # Read data from the weather table into a pandas DataFrame
    df = pd.read_sql_query("SELECT * FROM weather", conn)

    # Close the database connection
    conn.close()

    # Display the DataFrame
    st.dataframe(df)

if __name__ == '__main__':
    main()
