import requests

url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0001-001?Authorization=CWA-0CB59CAA-65F8-4C1A-989E-183572B28056"
response = requests.get(url)

if response.status_code == 200:
    with open("cwa_data.json", "w", encoding="utf-8") as f:
        f.write(response.text)
    print("Data downloaded successfully.")
else:
    print(f"Failed to download data. Status code: {response.status_code}")