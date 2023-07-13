from requests_html import HTMLSession

url = 'https://www.olx.com.br/eletronicos-e-celulares/estado-sp?q=iphone'
#url = 'https://www.olx.com.br/estado-sp?q=nintendo%20switch'
session = HTMLSession()
response = session.get(url)

# Nota: Utiliza-se ´#´ antes do nome para representar ids
# Nota2: Utiliza-se ´.´ após a tag HTML para representar classes
advert = []

links = response.html.find("#ad-list li a")
print("\n")
for link in links:
    url_iphone = link.attrs['href']

    response_iphone = session.get(url_iphone)

    title = response_iphone.html.find('h1', first=True).text
    price = response_iphone.html.find('span.ad__sc-1wimjbb-1', first=True).text
    
    advert.append({
        'url': url_iphone,
        'title': title,
        'price': price
    })
    print(f"Titulo: {title}\nPrice: {price}\nURL: {url_iphone}\n")

#print(advert)

