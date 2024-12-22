import requests

# Specify the IP address
ip = "{Enter_the_ip}"

# Make a GET request to the ipinfo.io API with the IP address you entered
response = requests.get(f"https://ipinfo.io/{ip}/json")
data = response.json()

# Getting relevant information
location = {
    "IP": data.get("ip"),
    "City": data.get("city"),
    "Region": data.get("region"),
    "Country": data.get("country"),
    "Latitude and Longitude": data.get("loc"),
    "Organization": data.get("org"),
}

print(f"- IP: {location['IP']}")
print(f"- City: {location['City']}")
print(f"- Region: {location['Region']}")
print(f"- Country: {location['Country']}")
print(f"- Latitude and Longitude: {location['Latitude and Longitude']}")
print(f"- Organization: {location['Organization']}")

