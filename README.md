# Taiwan Real-time Weather Dashboard

This is a Streamlit web application that displays real-time weather data from various weather stations across Taiwan. It provides a map-based visualization, a data table, and summary statistics in a dashboard format.

## Features

*   **Real-time Data:** Fetches and displays up-to-date weather information from the Central Weather Administration (CWA) of Taiwan.
*   **Interactive Map:** Shows the locations of weather stations on an interactive map of Taiwan.
*   **Dashboard View:** Presents a clean and modern dashboard with key weather metrics:
    *   Total number of active weather stations.
    *   Average temperature across all stations.
    *   Minimum and maximum temperatures recorded.
*   **Data Table:** Displays the raw data in a sortable and searchable table.
*   **Temperature Distribution:** A bar chart visualizing the distribution of temperatures across the country.
*   **Station Details:** A dropdown menu to select a specific weather station and view its detailed data.

## Data Source

The application uses the open data API from the **Central Weather Administration (CWA) of Taiwan**. Specifically, it fetches data from the [Automatic Weather Station - Meteorological Observation Data](https://opendata.cwa.gov.tw/dataset/observation/O-A0001-001) dataset (ID: `O-A0001-001`).

## Technologies Used

*   **Python:** The core programming language for the application.
*   **Streamlit:** The web framework used to build the interactive dashboard.
*   **Pandas:** For data manipulation and analysis.
*   **Requests:** To fetch data from the CWA API.
*   **SQLite:** As a lightweight local database to store the weather data.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/g114093002/AIOT_Lecture-13_Part_1.git
    cd AIOT_Lecture-13_Part_1
    ```

2.  **Install the required Python libraries:**
    Make sure you have Python 3.7+ installed. Then, run the following command to install the dependencies:
    ```bash
    pip install streamlit pandas requests
    ```

## Usage

1.  **Run the data processing script:**
    First, you need to download the data and populate the local database. Run the following command in your terminal:
    ```bash
    python process_data.py
    ```
    This will create a `data.db` file in the project directory.

2.  **Run the Streamlit application:**
    After the data is processed, you can start the web application:
    ```bash
    streamlit run app.py
    ```
    This will open the application in your default web browser.

## Screenshot

*(Here you can add a screenshot of the running application)*

![Dashboard Screenshot](<PATH_TO_YOUR_SCREENSHOT.PNG>)
