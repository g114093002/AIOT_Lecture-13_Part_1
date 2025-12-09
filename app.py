
import streamlit as st
import pandas as pd
import sqlite3
import numpy as np

def main():
    st.set_page_config(layout="wide")
    st.title("Taiwan Real-time Weather Dashboard")

    # Connect to SQLite database
    conn = sqlite3.connect('data.db')
    df = pd.read_sql_query("SELECT * FROM weather", conn)
    conn.close()

    # --- Summary Metrics ---
    st.subheader("Current Weather Summary")
    total_stations = len(df)
    avg_temp = round(df['temperature'].mean(), 2)
    min_temp = df['temperature'].min()
    max_temp = df['temperature'].max()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Stations", total_stations)
    col2.metric("Average Temperature", f"{avg_temp} °C")
    col3.metric("Min Temperature", f"{min_temp} °C")
    col4.metric("Max Temperature", f"{max_temp} °C")

    st.markdown("---")

    # --- Main Dashboard Layout ---
    st.subheader("Weather Stations Map and Data")
    col1, col2 = st.columns([2, 1])

    with col1:
        st.map(df)

    with col2:
        st.dataframe(df)

    st.markdown("---")

    # --- Temperature Distribution ---
    st.subheader("Temperature Distribution")
    hist_values = np.histogram(df['temperature'], bins=20, range=(df['temperature'].min(), df['temperature'].max()))[0]
    st.bar_chart(pd.DataFrame(hist_values, columns=["count"]))

    st.markdown("---")

    # --- Station Details ---
    st.subheader("Station Details")
    station_list = ["All"] + list(df['location'].unique())
    selected_station = st.selectbox("Select a station to view details", station_list)

    if selected_station == "All":
        st.write("Showing data for all stations.")
    else:
        station_data = df[df['location'] == selected_station]
        st.write(f"Details for {selected_station}:")
        st.dataframe(station_data)


if __name__ == '__main__':
    main()
