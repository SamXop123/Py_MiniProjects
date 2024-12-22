import requests

# Specify the IP address
ip = "192.168.29.13"

# Make a GET request to the ipinfo.io API with the IP address
response = requests.get(f"https://ipinfo.io/{ip}/json")
data = response.json()

# Extract relevant information
location = {
    "IP": data.get("ip"),
    "City": data.get("city"),
    "Region": data.get("region"),
    "Country": data.get("country"),
    "Latitude and Longitude": data.get("loc"),
    "Organization": data.get("org"),
}

# Print the output in bullet points
print(f"- IP: {location['IP']}")
print(f"- City: {location['City']}")
print(f"- Region: {location['Region']}")
print(f"- Country: {location['Country']}")
print(f"- Latitude and Longitude: {location['Latitude and Longitude']}")
print(f"- Organization: {location['Organization']}")

