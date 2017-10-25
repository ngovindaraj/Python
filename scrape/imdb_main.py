from imdb_results_page import process_results_page
from sql_db import create_imdb_tables, create_mysql_connection

# Create MySQL tables in imdb MySQL database
sql = create_mysql_connection()
create_imdb_tables(sql)

# Create a list of Results URLs and process them one by one
# for i in 1 to 120:
#     url = "www.imdb.com/search/title?count={}".format(i)
#     process_results_page(url)



# Parse each movie page
