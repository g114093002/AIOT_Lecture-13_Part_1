import requests

url = "https://opendata.cwa.gov.tw/fileapi/v1/opendataapi/F-A0010-001?Authorization=CWA-0CB59CAA-65F8-4C1A-989E-183572B28056&format=JSON"
response = requests.get(url)

if response.status_code == 200:
    with open("cwa_data.json", "w", encoding="utf-8") as f:
        f.write(response.text)
    print("Data downloaded successfully.")
else:
    print(f"Failed to download data. Status code: {response.status_code}")
