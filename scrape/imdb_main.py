from imdb_results_page import process_results_page
from sql_db import create_imdb_tables, create_mysql_connection

# # Create MySQL tables in imdb MySQL database
sql = create_mysql_connection()
create_imdb_tables(sql)

# Parse each movie page
for i in range(21, 101):
    url = "http://www.imdb.com/search/title?count=100&countries=us&languages=en&production_status=released&release_date=2013,2016-12&sort=year,asc&title_type=feature&page={}&ref_=adv_nxt".format(i)
    print(i, url)
    process_results_page(sql, url)
    #break
