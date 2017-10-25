'''
List of fields we need to collect inside one page:
- Budget             - Int
- Production Company - Enum --not doing
- Release Date  - Date/Time
- Writer             - Enum
- Opening Weekend$   - Int
'''

# import libraries
import re
from utils import readURL, html2Soup, getTagText
from sql_db import MySql

html2 = readURL('/Users/navina/Desktop/movie1.htm')
individual_movie_pg = html2Soup(html).find(id="main")
sql = MySql(user='ngovindaraj', passwd='the rock', db='imdb')
sql.connect()



def process_movie_page(mv):
    budget = getTagText(mv.find(
        "span", class_="lister-item-index unbold text-primary"))
    release_dt = getTagText(mv.find("h3", class_="lister-item-header").find("a"))
    writer = getTagText(mv.find("span", class_="certificate"))
    opening_weekend_gross =

    print("Budget: {}".format(budget))
    print("Release Date: {}".format(release_dt))
    print("Writer: {}".format(writer))
    print("Opening Weekend Gross: {}".format(opening_weekend_gross))


'''
#url2

movie_pg_top_half = soup2.find(id="main_top")
movie_pg_bottom_half = soup2.find(id="main_bottom")
top_half_tags = movie_pg_top_half.select(".title_overview .title_bar_wrapper")
bottom_half_tags = movie_pg_bottom_half.select("")
print(top_half_tags)



for tag in titlebar_tags:
    process_individual_movie(tag)
'''


#director = top_half_tags.find("div", "credit_summary_item").find("span", "itemprop").get_text()
#print("Director: {}".format(director))

#stars = soup2.find("span", {"itemprop": "actors"}).get_text()
#print(stars)

#box_office = soup2.find("")
#budget = soup2.find("span", {"itemprop": "actors"}).get_text()
#print(budget)

#release_date = soup2.find("a", {"title": "See more release dates"}).get_text()
#print(release_date)

#writer = soup2.find("span", {"itemprop": "creator"}).get_text()
#print(writer)

#opening_weekend_gross = soup2.find("span", {"itemprop": "creator"}).get_text()
#print(opening_weekend_gross)
