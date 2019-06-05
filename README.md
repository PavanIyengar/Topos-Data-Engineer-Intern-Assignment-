# Topos-Data-Engineer-Intern-Assignment

The goal of this assignment is to demonstrate your ability to capture unconventional datasets, clean and store them. Write a scraper in either python or NodeJS to collect data from Wikipedia about the top cities in the United States. The fields you collect, as well as the volume of data is up to you, but ideally you add additional data beyond the initial table, such as data found on the individual city pages, or other sources of your choice. The final format should be a CSV file that is ready to be uploaded to a BigQuery table. Please read Bigquery’s Manual to prepare your CSV in the right format. Intermediary steps, environments or processes necessary to run the scraper should be documented in code as well as a Readme.md and hosted on github in a repo devoted to this assignment. 

# Solution details

Environment Python 3.7.3 and BeautifulSoup4 on Windows10 Home Edition
This project contains one source file named WikiStatesProject.py. 

# File Information
The WikiStatesProject.py file contains code that produces a list of specific US Cities from a WIkipedia page that ranked the cities. The code identifies the cities that are the largest in their respective states. It then pulls data from each state's wikipedia page.
The Test.csv file shows the result of the code. It shows the list of the cities, links to their wikipedia pages, along with their founded date, settled date, incorporated date, and who they were named after.

List of cities and links to their wikipedia pages were found on the main wikipedia cities page.
The founded date, settled date, incorporated date, and named after information was found on the city's specific wiki page.

# Validation
The project was validated by comparing the data in the csv file versus the data on each city's wikipedia page. The file was then uploaded using Google's Big Query Web UI to verify that the data was presented correctly and that test.csv was in a format that is ready to be uploaded to a BigQuery table. 
