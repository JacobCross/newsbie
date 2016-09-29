#WHEN RUNNING THIS FILE - MUST RUN AS:
# > sudo python3 newspaperTester.py

import newspaper
import datetime
import urllib
import json

from operator import itemgetter, attrgetter
from newsbie_config import *
from url_lists import *

base_url = "http://gateway-a.watsonplatform.net/calls/url/URLGetCombinedData?extract=page-image,concepts,entity,keyword,taxonomy&apikey="+API_KEY+"&showSourceText=0&sentiment=1&quotations=1&outputMode=json&url="

categories = []
catCount = []
sortedList = []
counter = 0

news_domain = "http://cnn.com"
#news_domain = "http://www.wired.com/"
#news_domain = "https://techcrunch.com/"
#news_domain = "http://www.nytimes.com/"
#news_domain = "http://www.sfgate.com/"

# cnn_paper = newspaper.build(news_domain)

print("----------------------------------------")
print("Getting recent articles from: " + news_domain)
print("----------------------------------------")

for url in tempList1:
# for article in cnn_paper.articles:
    counter+=1

    #url = article.url
    final_url = base_url + url
    final_url.encode('utf8')

    #getting the json data response from AlchemyAPI
    jdata = urllib.request.urlopen(final_url).read()
    string = jdata.decode("utf-8")
    data = json.loads(string)
    print("...analyzing article "+str(counter))


    # checking to make sure the data returned is valid, and adding it to the 2-array collection.
    return_status = data['status']
    if return_status=='OK':
        category = data['taxonomy'][0]['label']
        if categories.count(category)==0:
            print('NEW')
            categories.append(category)
            catCount.append(1)
        elif categories.count(category)==1:
            print('ADDING TO EXISTING')
            catCount[categories.index(category)]+=1
        else:
            print('LIST MATCHING ISSUE')
    else:
        print("RETURN STATUS: ERROR")

if(len(categories)==0):
    print('No Articles Found.')

initial = categories[0][1]
currentMaxIndex = 0
top = initial
done = False
first = True

# combining catCount and categories into a single, 2D array
for item in categories:
    itemIndex = categories.index(item)
    score = catCount[itemIndex]
    sortedList.append([item,score])

#sorting the 2d list of [category, score] objects.
newSort = sorted(sortedList, key=itemgetter(1), reverse=True)

print('--------------------------------------------------------')
print('Sorted List: ')
for item in newSort:
    print(item[0]+" appeared: "+str(item[1]) + " times")
print('--------------------------------------------------------')
print("Articles Fetched: "+str(counter))
print("----------------------------------------")
