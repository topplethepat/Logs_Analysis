**Logs Analysis Project** 
*Udacity Full Stack Web Developer Nanodegree Project 1*

***REQUIREMENTS***

- Python 2.7
- psycopg2
- PostgreSQL 9.5.10
- data is accessible at https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
- newsdata.sql file must be stored in directory 'vagrant'

The file log_analysis.py may be run in a Vagrant managed virtual machine, or VM.
Vagrant and VirtualBox must be installed on users local machine.

***PROJECT CONTENTS***

- log_analysis.py', the script containing the three sql expressions required for the required output
- 'terminal_output.txt', a copy of the terminal output from running 'log_analysis.py'
- 'README.md', which includes the views the user must first create in the database in order to run the script

***SETUP and EXECUTION***

Start the VM:

	vagrant up

Log into the VM:

	vagrant ssh

Navigate to correct directory:

	cd /vagrant

Load the logs into the database:

	psql -d news -f newsdata.sql

Run the script:

	python log_analyis.py

***VIEWS FOR QUESTION 2***
**VIEW xyz**

create view xyz as select articles.author,articles.slug, count(\*) as num from articles join log on articles.slug = substring(log.path, 10, 28) group by articles.author,articles.slug;

**VIEW abc**

create view abc as select authors.name, xyz.slug, xyz.num from xyz join authors on authors.id = xyz.author group by authors.name, xyz.slug, xyz.num;


***VIEWS FOR QUESTION 3***

**VIEW date_count**
 create view date_count as select date(time),count(\*) as num from log group by date(time) order by date(time);

**VIEW error_count** 
create view error_count as select date(time), count(\*) as error from log where status != '200 OK' group by date(time) order by date(time);

   

