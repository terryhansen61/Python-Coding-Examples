# This will track an IP Address and give back information on where that IP Address
# is located.  The IP Address must be a public address or it will return an error
import requests

# Put in any public IP Address here
ip_address = "208.67.222.222"
url = f"https://ipinfo.io/{ip_address}/geo"

# Fetch the tracking data
data = requests.get(url).json()
print(f"Tracking IP: {ip_address}")
print(f"-" * 25)
print(f"City: {data['city']}")
print(f"Region: {data['region']}")
print(f"Country: {data['country']}")
print(f"GPS Coordinates: {data['loc']}")
print(f"Network ISP: {data['org']}")

