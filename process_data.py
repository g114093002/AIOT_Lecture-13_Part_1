
import json
import sqlite3

def process_and_store_data():
    # Load JSON data
    with open('cwa_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Connect to SQLite database
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            location TEXT,
            min_temp REAL,
            max_temp REAL,
            description TEXT
        )
    ''')

    # The actual data is in a different location for this dataset
    if 'cwaopendata' in data and 'resources' in data['cwaopendata']:
        locations = data['cwaopendata']['resources']['resource']['data']['agrWeatherForecasts']['weatherForecasts']['location']
        for location in locations:
            location_name = location['locationName']
            wx_daily = location['weatherElements']['Wx']['daily']
            min_t_daily = location['weatherElements']['MinT']['daily']
            max_t_daily = location['weatherElements']['MaxT']['daily']

            for i in range(len(wx_daily)):
                description = wx_daily[i]['weather']
                min_temp = min_t_daily[i]['temperature']
                max_temp = max_t_daily[i]['temperature']

                # Insert a row of data
                cursor.execute("INSERT INTO weather (location, min_temp, max_temp, description) VALUES (?, ?, ?, ?)",
                               (location_name, min_temp, max_temp, description))
    else:
        print("Could not find the expected data structure in the JSON file.")


    # Commit changes and close connection
    conn.commit()
    conn.close()
    print("Data processed and stored in data.db")

if __name__ == '__main__':
    process_and_store_data()
