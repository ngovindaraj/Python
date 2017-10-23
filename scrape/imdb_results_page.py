'''
Predicting US Box Office Gross
IMDB (English language, only in US)
List of fields we need to collect:
List of 100s:
- Movie title     - String (div id ="main" > div class ="article"> div class =" lister list detail sub-list", div class = "lister-list", div class="lister-item mode-advanced", div class="lister-item-image float-left", a href -->img alt = "title">
- MPAA rating     - Enum (div id ="main" > div class ="article"> div class =" lister list detail sub-list", div class = "lister-list", div class="lister-item mode-advanced", div class="lister-item-content", p class="text-muted", span class="certificate")
- Metascore  /100 - Float (div id ="main" > div class ="article"> div class =" lister list detail sub-list", div class = "lister-list", div class="lister-item mode-advanced", div class="lister-item-content",div class="ratings-bar", div class="inline-block ratings-metascore", inspan class="metascore*")
- User Rating /10 - Float(div id ="main" > div class ="article"> div class =" lister list detail sub-list", div class = "lister-list", div class="lister-item mode-advanced", div class="lister-item-content",div class="ratings-bar", div class="inline-block ratings-imdb-rating", data value=?)
- Genre           - Enum
- Runtime in mins - Int
- Director        - Enum
- Stars           - List of Enum
- US Gross        - Int
- #Votes          - Int

Inside one page:
- Budget             - Int
- Production Company - Enum --not doing
- Release Date  - Date/Time
- Writer             - Enum
- Opening Weekend$   - Int
'''

# import libraries
import requests
from bs4 import BeautifulSoup

# Get html contents
def readURL(url):
    # page = requests.get(url)
    with open(url, 'r') as myfile:
        data = myfile.read()
    return data

# url1
html = readURL('/Users/navina/Desktop/imdb_test.htm')
soup = BeautifulSoup(html, 'html.parser')

# url2
html2 = readURL('/Users/navina/Desktop/movie1.htm')
soup2 = BeautifulSoup(html2, 'html.parser')

def process_movie_main_link(mv):
    sno = mv.find("span", "lister-item-index unbold text-primary").get_text()
    title = mv.find("h3", "lister-item-header").find("a").get_text()
    mpaa_rating = mv.find("span", "certificate").get_text()
    metascore = mv.find("span", "metascore").get_text()
    user_rating = mv.find("div", "inline-block ratings-imdb-rating").find("strong").get_text()
    genre = mv.find("span", "genre").get_text().strip()
    runtime = mv.find("span", "runtime").get_text()
    print("Serial No. {}").format(sno)
    print("Movie Title: {}").format(title)
    print("MPAA Rating: {}").format(mpaa_rating)
    print("Metacore: {}").format(metascore)
    print("User Rating: {}").format(user_rating)
    print("Genre: {}").format(genre)
    print("Runtime {}").format(runtime)


main_section = soup.find(id="main")
all_movie_tags = main_section.select(".article .lister-item-content")

for each_movie in all_movie_tags:
    process_movie_main_link(each_movie)




    #add to mysql




'''
# test for first movie

first_movie = all_movie_tags[0]
print(first_movie)
sno = first_movie.find("span", "lister-item-index unbold text-primary").get_text()
title = first_movie.find("h3", "lister-item-header").find("a").get_text()
mpaa_rating = first_movie.find("span", "certificate").get_text()
metascore = first_movie.find("span", "metascore").get_text()
user_rating = first_movie.find("div", "inline-block ratings-imdb-rating").find("strong").get_text()
genre = first_movie.find("span", "genre").get_text().strip()
runtime = first_movie.find("span", "runtime").get_text()

print("Serial No. {}".format(sno))
print("Movie Title: {}".format(title))
print("MPAA Rating: {}".format(mpaa_rating))
print("Metacore: {}".format(metascore))
print("User Rating: {}".format(user_rating))
print("Genre: {}".format(genre))
print("Runtime: {}".format(runtime))

#url2

# titlebar = soup.find("div", "titleBar")
# print(type(titlebar))

#titlebar_tags = titlebar.select(".div .subtext")
#first_movie_titlebar = titlebar_tags[0]
#print(first_movie_titlebar)

director = soup2.find("span", "itemprop").find(itemprop="director").get_text()
#print(director)

total_votes = soup2.find("span", {"itemprop": "ratingCount"}).get_text()
print(total_votes)

#us_boxoffice_gross = soup2.find("div", "article").get_text()
#print(us_boxoffice_gross)

stars = soup2.find("span", {"itemprop": "actors"}).get_text()
print(stars)

box_office = soup2.find("")
budget = soup2.find("span", {"itemprop": "actors"}).get_text()
print(budget)

release_date = soup2.find("a", {"title": "See more release dates"}).get_text()
print(release_date)

writer = soup2.find("span", {"itemprop": "creator"}).get_text()
print(writer)

opening_weekend_gross = soup2.find("span", {"itemprop": "creator"}).get_text()
print(opening_weekend_gross)
'''
