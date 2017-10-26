from imdb_results_page import process_results_page
from sql_db import create_imdb_tables, create_mysql_connection

# Create MySQL tables in imdb MySQL database
sql = create_mysql_connection()
create_imdb_tables(sql)

# Create a list of Results URLs and process them one by one
process_results_page(sql, 'http://www.imdb.com/search/title?count=100&countries=us&languages=en&production_status=released&release_date=2013,2016-12&sort=year,asc&title_type=feature')
# for i in range(1 to 121):
#     url = "www.imdb.com/search/title?count={}".format(i)
#     process_results_page(sql, url)



# Parse each movie page
