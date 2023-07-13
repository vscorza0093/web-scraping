from requests_html import HTMLSession

url = 'https://www.adrenaline.com.br/'
session = HTMLSession()
response = session.get(url)
links = response.html.find("a")
news = []
#print(response.text)
#print(f"status code: {response.status_code}")

for link in links:
    url = 'https://www.adrenaline.com.br/{}'.format(link.attrs['href'])
    response = session.get(url)
    infos = response.html.find('.btn-4')
    new = {
        'titulo': response.html.find('h1', first=True).text,
        'texto': response.html.find('')
    }
    news.append(new)
    print(new)
