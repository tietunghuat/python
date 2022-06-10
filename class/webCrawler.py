# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from requests import get
from bs4 import BeautifulSoup


url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'
response = get(url)
#print(response.text[:500])

testHtml='''
<!DOCTYPE html>
<html>
<head>
<title>hi, this is a simple page</title>
</head>
<body>

<h1>This is a Heading</h1>
<p>This is a paragraph.</p>

</body>
</html>
'''

html_soup = BeautifulSoup(response.text, 'html.parser')

#print(type(html_soup))
print("********************\n")
print(html_soup.title.text)

movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')
print(type(movie_containers))
print(len(movie_containers))

for i in range(5):
    the_movie = movie_containers[i]
    print("Title:", the_movie.h3.a.text)
    print("Rating:",the_movie.strong.text)
    print("Director:", the_movie.p.text)
    votes=the_movie.find_all("span",{"name":"nv"})
    print("Votes:",votes[0].text)
    print("Gross:",votes[1].text)
    go = the_movie.find_all("span", {"class": "runtime"})
    print("Runtime:",go[0].text)
    ko = the_movie.find_all("span", {"class": "certificate"})
    print("Certificate:",ko[0].text)
    lo = the_movie.find_all("span", {"class": "genre"})
    print("Type:",lo[0].text)
    print("\n\n")



#print(first_movie)





