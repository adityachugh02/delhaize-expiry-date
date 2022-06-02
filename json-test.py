import requests
url = 'https://delhaize-expiry-date.herokuapp.com/'
files = {'image': open('sample1.jpg', 'rb')}
response = requests.post(url, files=files)
print(response.text)