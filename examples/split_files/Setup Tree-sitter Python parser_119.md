### 3. BeautifulSoup

BeautifulSoup is used for web scraping and offers a Pythonic interface to navigate and search HTML/XML documents.

#### Simple Example
Find all links:
```python
soup.find_all('a')
```

#### Advanced Example
Using lambda for more complex queries:
```python
soup.find_all(lambda tag: tag.name == 'div' and 'class' in tag.attrs)
```

