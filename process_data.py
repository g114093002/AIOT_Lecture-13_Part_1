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
    cursor.execute('DROP TABLE IF EXISTS weather')
    cursor.execute('''
        CREATE TABLE weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            location TEXT,
            lat REAL,
            lon REAL,
            temperature REAL,
            description TEXT
        )
    ''')

    if 'records' in data and 'Station' in data['records']:
        stations = data['records']['Station']
        for station in stations:
            location_name = station['StationName']
            temperature = station['WeatherElement']['AirTemperature']
            description = station['WeatherElement']['Weather']
            lat = None
            lon = None
            for coords in station['GeoInfo']['Coordinates']:
                if coords['CoordinateName'] == 'WGS84':
                    lat = float(coords['StationLatitude'])
                    lon = float(coords['StationLongitude'])
            
            if lat is not None and lon is not None and temperature != '-99':
                # Insert a row of data
                cursor.execute("INSERT INTO weather (location, lat, lon, temperature, description) VALUES (?, ?, ?, ?, ?)",
                               (location_name, lat, lon, float(temperature), description))
    else:
        print("Could not find the expected data structure in the JSON file.")


    # Commit changes and close connection
    conn.commit()
    conn.close()
    print("Data processed and stored in data.db")

if __name__ == '__main__':
    process_and_store_data()