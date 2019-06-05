#import libraries
from bs4 import BeautifulSoup
import urllib3
import codecs
import csv
import os

#create output file
FILENAME = "test.csv"
ENCODING = 'utf-8'

with codecs.open(FILENAME, "w", ENCODING) as fp:
    writer = csv.writer(fp)
    writer.writerow(['city', 'citywikipage', 'founded_date', 'settled_date', 'incorporated_date', 'namedfor'])
      

    
#set the url 
    http = urllib3.PoolManager()

    url="https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population"
    wikiurl="https://en.wikipedia.org"

    
#connect to the url and save to BeautifulSOup in order to Parse
    response = http.request('GET', url)
    soup = BeautifulSoup(response.data, "html.parser")
    
#find first table and it's body
    tablespan = soup.find("table", class_ = lambda s:s.startswith ("wikitable sortable"))
    tablebody = tablespan.find(lambda tag: tag.name == ('tbody'))
    
#find a common aspect about multiple cities. In this case, the aspect is the largest city in each states.
    tablebodyitag = tablebody.find_all(lambda tag: tag.name == ('i'))
    ##print(tablebodyitag)
    
#traverse the list
    for tableitag in tablebodyitag:
        tablerows = tableitag.find_all(lambda tag: tag.name == ('a') and tag.has_attr('title'))
        for trows in tablerows:
            # print(tablerows.text,tablerows["href"],tablerows["title"])

            #get the list of rows in the table to get cityname and city wiki page
            city = trows.text
            citypage = trows['href']
            
            #create full url for each city page
            cityurl = wikiurl + citypage
            # print(str(city))

            #initialize specific data that is to be extracted from each individual city wiki page
            cityresponse = http.request('GET', cityurl)
            cityfounded = ''
            citysettled = ''
            cityincorporated = ''
            citynamedfor = ''

            #open city wikipage for parsing
            citysoup = BeautifulSoup(cityresponse.data, "html.parser")

            #extract specific table
            citytablespan = citysoup.find("table", {"class":"infobox geography vcard"})

            #find the specific rows in the table
            citytablebody = citytablespan.find_all('tr')

            #Navigate through the tablerows, 1 row at a time
            for row in citytablebody:
                ## print(row)
                citytablebodylist = row.find(lambda tag: tag.name == ('th') and tag.has_attr('scope'))
                if (citytablebodylist != None):
                    text_of_interest = citytablebodylist.get_text()
                    if (text_of_interest == 'Founded'):
                        cityfounded = citytablebodylist.find_next('td').get_text()
                    else:
                            if (text_of_interest == 'Settled'):
                                citysettled = citytablebodylist.find_next('td').get_text()
                            else:
                                    if (text_of_interest == 'Incorporated'):
                                        cityincorporated = citytablebodylist.find_next('td').get_text()
                                    else:
                                            if (text_of_interest == 'Named for'):
                                                citynamedfor = citytablebodylist.find_next('td').get_text()
                                            
                                                print(city.encode('utf-8'), cityfounded.encode('utf-8'), citysettled.encode('utf-8'), cityincorporated.encode('utf-8'),citynamedfor.encode('utf-8'))
        rowtowrite = [city, cityurl, cityfounded, citysettled, cityincorporated, citynamedfor]
        writer.writerow(rowtowrite)
fp.close()
            

               
        
        
