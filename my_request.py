import requests

# response = requests.get('https://sky.pro')
# response = requests.get('https://api.ip2country.info/ip?55.53.53.5')
response = requests.get('https://github.com/public-apis/public-apis')
response = requests.get('https://catfact.ninja/fact')

print(response.text)
print(response.status_code)
print(response.json())

