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
- *Director        - Enum
- *Stars           - List of Enum
- US Gross        - Int
- #Votes          - Int
'''

# import libraries
import re
from utils import readURL, html2Soup, getTagText, getInt, getFloat
# from sql_db import MySql




'''
sql = MySql(user='ngovindaraj', passwd='the rock', db='imdb')
sql.connect()
'''

#0) Get URL of movie page
#1) Create SQL tables in 3NF
#2) Insert dummy values
#3) Hook up insert_one_movie_into_mysql() to insert 100 movies into MySQL
#4) Use Request, to get all 12K Movies into MySQL


# Create all the tables that we need for results page
def create_sql_tables():
    pass


def get_urls():
    movie_url = mv.find('a', href=re.compile('/title/'))
    print(movie_url)


def insert_one_movie_into_mysql(
    sno, title, mpaa_rating, metascore,
    user_rating, genre, runtime, votes_count, us_box_gross, director,
    star1, star2, star3, movie_url):
    print("{sno}. {title} has rating {mpaa}".format(
        sno=sno, title=title, mpaa=mpaa_rating))
    print("Metascore: {}".format(metascore))
    print("User Rating: {}".format(user_rating))
    print("Genre: {}".format(genre))
    print("Runtime: {}".format(runtime))
    print("Votes Count: {}".format(votes_count))
    print("US Box Office Gross: {}".format(us_box_gross))
    print("Director: {dir} Stars: {s1}, {s2}, {s3}".format(
        dir=director, s1=star1, s2=star2, s3=star3))
    print("Movie URL: {}".format(movie_url))
    #sql.insertRow()


# For each movie use BeautifulSoup find() to get all the relevant fields.
# After processing one movie, insert it to MySQL
def process_results_one_movie(mv):
    sno = getTagText(mv.find(
        "span", class_="lister-item-index unbold text-primary"))
    title = getTagText(mv.find("h3", class_="lister-item-header").find("a"))
    mpaa_rating = getTagText(mv.find("span", class_="certificate"))
    metascore = getInt(getTagText(mv.find("span", class_="metascore")))
    user_rating = getFloat(getTagText(mv.find(
        "div",
        class_="inline-block ratings-imdb-rating").find("strong")))
    genre = getTagText(mv.find("span", class_="genre"))
    runtime = getTagText(mv.find("span", class_="runtime"))
    runtimeNum = getInt(runtime.split()[0])
    votes = getTagText(mv.find(
        "p", class_="sort-num_votes-visible")).split()[1]
    votes_count = getInt(votes.replace(',', ''))
    us_box_gross = getTagText(mv.find(
        "p", class_="sort-num_votes-visible")).split()[-1]
    director = getTagText(mv.find('a', href=re.compile('adv_li_dr_0')))
    star1 = getTagText(mv.find('a', href=re.compile('adv_li_st_0')))
    star2 = getTagText(mv.find('a', href=re.compile('adv_li_st_1')))
    star3 = getTagText(mv.find('a', href=re.compile('adv_li_st_2')))
    movie_url = mv.find('a', href=re.compile('/title/'))['href']
    insert_one_movie_into_mysql(
        sno, title, mpaa_rating, metascore,
        user_rating, genre, runtimeNum, votes_count, us_box_gross, director,
        star1, star2, star3, movie_url)


def process_results_page(url):
    html = readURL(url)
    main_section = html2Soup(html).find(id="main")
    for each_movie in main_section.select(".article .lister-item-content"):
        process_results_one_movie(each_movie)
        # break


# process_results_page('/Users/navina/Desktop/imdb_test.htm')
