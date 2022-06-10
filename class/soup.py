from requests import get
from bs4 import BeautifulSoup

url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'
response = get(url)
print(response.text[:500])

text= """
<!DOCTYPE html >
<html >
<head >
<title > Page Title < /title >
</head >
<body >

<h1 > This is a Heading < /h1 >
<p > This is a paragraph. < /p >

</body >
</html >
"""

html = BeautifulSoup(text,'html.parser')
print(type(html))
print(html.title)