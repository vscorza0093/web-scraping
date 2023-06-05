from requests_html import HTMLSession

url = 'https://www.larian.com'
session = HTMLSession()
response = session.get(url)
print(response.text)
print(f"status code: {response.status_code}")
