# Web-scraping

Studies about web scraping with Python

Web scraping is an automated process for collecting structured data from web pages.

Widely used in price monitoring, business intelligence, news monitoring, lead generation and market research

In general, web data extraction is used by people and companies that want to use a large amount of available information to support smarter choices.

## Scraping

Scraping is a method of extracting specific information from any unstructured data source (web page) and persisting that data in a structured form in some database

Ex: extract the prices of products from some e-commerce

## Crawling

When we access web pages and track their links, storing generic information such as a source link.

Search engines use this method to identify the flow of any webpage without extracting information from it.

So a web scraper is a tool that we build to crawl back pages and extract structured data from there and persist it in some form like a database or Excel spreadsheet

We have to be careful, because a web scraper is not an illegal tool, but using the extracted data outside the environment where we collect it can cause us problems. Also, some data is protected by international regulations, so we really have to be cautious.

Many companies use the web scraper to compose a massive database and obtain insights from specific sectors. Some of these companies sell these insights obtained through the web scraper

## requests-html

When we build an application that automatically accesses a web page, what is returned to us is an HTML code, and for that, we need to use request-html

request-html is a python module that we use to access a web page

It's not a built in module, so we need to install

`pip install requests-html`

```python
from requests_html import HTMLSession

url = 'https://www.larian.com'
session = HTMLSession()
response = session.get(url)
print(response.text)
print(f"status code: {response.status_code}")
```

url -> defines the link we want to access
session -> here we define a session, like when we open the browser to access a web page
response -> here we use the get method of the session that has already been opened to make a GET HTTP request

### Filtering by classes

In the example above, we are crawling through the website searching for all img tags that are connected with the CSS class `highlight__picture__img` using the `find()` function that is part of `html` property from the response of `get()` function.

```python
links = response.html.find("img.highlight__picture__img")
```

This `get` function has a series of functions to navigate through HTML's page and extract data.

Each extracted element, using `find()` function, has a property called `attrs`. This property is a dictionary that contains all HTML attributes of element. We could use it to filter even more our extracted data.

```python
for link in links:
    print(link.attrs['src'])
```

## Selenium Portable Framework
