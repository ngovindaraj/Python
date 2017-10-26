'''
List of fields we need to collect inside one page:
- Budget             - Int
- Production Company - Enum --not doing
- Release Date  - Date/Time
- Writer             - Enum
- Opening Weekend$   - Int -- not doing
'''

import re
from utils import readURL, html2Soup, getTagText


# Get the 2nd writier for a movie if one exists
def get_second_writer(mv):
    try:
        return mv.find_all('a', href=re.compile('tt_ov_wr'))[1]
    except IndexError:
        return None


def get_budget(mv):
    try:
        return mv.find(text=re.compile("Budget:")).next.strip()
    except:
        return 'Empty'


def process_one_movie_url(url):
    url = 'http://www.imdb.com' + url
    html = readURL(url)
    movie_section = html2Soup(html).find(id="pagecontent")
    mv = movie_section.select(".flatland")[0]
    budget = get_budget(mv)
    release_dt = ' '.join(mv.find(
        text=re.compile("Release Date:")).next.split()[:3])
    writer1 = getTagText(mv.find('a', href=re.compile('tt_ov_wr')))
    writer2 = getTagText(get_second_writer(mv))
    return budget, release_dt, writer1, writer2


# Test
# budget, release_dt, writer1, writer2 = process_one_movie_url(
#     '/Users/navina/Desktop/movie1.htm')
# print("Budget: {}".format(budget))
# print("Release Date: {}".format(release_dt))
# print("Writer1: {}".format(writer1))
# print("Writer2: {}".format(writer2))
