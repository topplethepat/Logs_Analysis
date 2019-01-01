#!/usr/bin/env python

import psycopg2
DBNAME = "news"


def main():
	# connects to database
	db = psycopg2.connect(database=DBNAME)

	# cursor performs operations
	c = db.cursor()

	# Question No. 1: What are the most popular three articles of all time?
	# help from stack overflow: https://bit.ly/2EL7HqA
	
	top_3_articles = """
		SELECT articles.title, COUNT(log.path) AS num
		FROM log 
		JOIN articles on articles.slug = substring(log.path, 10, 28)
		GROUP BY articles.title,log.path
		HAVING log.path != '/'
		ORDER BY num DESC
		LIMIT 3;
		"""
	c.execute(top_3_articles) 

	article_extract = c.fetchall()
	for title,views in article_extract:
		print(" {} {} views".format(title,views))
	
	# Question No.2: Who are the most popular article authors of all time?

	top_authors = """
		SELECT abc.name, SUM(num)
		AS sum 
		FROM abc
		GROUP BY abc.name
		ORDER BY SUM DESC """

	c.execute(top_authors)

	table_result = c.fetchall()
	for name,views in table_result:
		print(" {} {} views".format(name, views))

	# Question No.3: On what days was the percentage of hits greater than 1?
	# help on stack overflow: https://bit.ly/2CxMe21
	
	percent_error = """
	SELECT date, percentage FROM (
	SELECT date_count.date, (ROUND(100.0 * error_count.error / date_count.num, 2))
	AS percentage 
	FROM date_count JOIN error_count on date_count.date = error_count.date 
	ORDER BY date_count.date) 
	AS result WHERE percentage > 1;
	"""

	c.execute(percent_error)
	result = c.fetchall()
	for date,percentage in result:
		print("On {} there was a {} percent status error rate".format(date, percentage))

	c.close()
	db.close()



if __name__ == "__main__":
	main()	

