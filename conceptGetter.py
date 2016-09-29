import newspaper
import datetime
import urllib
import json

from operator import itemgetter, attrgetter
from newsbie_config import *
from

base_url = "http://gateway-a.watsonplatform.net/calls/url/URLGetCombinedData?extract=page-image,concepts,entity,keyword,taxonomy&apikey="+API_KEY+"&showSourceText=0&sentiment=1&quotations=1&outputMode=json&url="

categories = []
catCount = []
sortedList = []
counter = 0

#news_domain = "http://cnn.com"
news_domain = "http://www.wired.com/"
#news_domain = "https://techcrunch.com/"
#news_domain = "http://www.nytimes.com/"
#news_domain = "http://www.sfgate.com/"


cnn_paper = newspaper.build(news_domain)

print("----------------------------------------")
print("Getting recent articles from: tempList") #news_domain)
print("----------------------------------------")

for url in tempList:
# for article in cnn_paper.articles:
    counter+=1
    #constructing the url using newspaper API
    #url = article.url
    final_url = base_url + url
    #final_url = base_url + article.url
    final_url.encode('utf8')

    #got an error that said a certain http type wasn't supported.

    #getting the json data from AlchemyAPI
    jdata = urllib.request.urlopen(final_url).read()
    string = jdata.decode("utf-8")
    data = json.loads(string)
    print("...fetching article number"+str(counter))


    print(string)
    return_status = data['status']
    #print('return_status:'+return_status+'-TEST')
    if return_status=='OK' and not data['concepts']==[]:
        category = data['concepts'][0]['text'] #this is where I am making the change to get the concept rather than the taxonomy
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

initial = categories[0][1]
currentMaxIndex = 0
top = initial
done = False
first = True
counter = 0

for item in categories:
    itemIndex = categories.index(item)
    score = catCount[itemIndex]
    sortedList.append([item,score])

newSort = sorted(sortedList, key=itemgetter(1), reverse=True)

print('new: ')
for item in newSort:
    print(item[0]+" appeared: "+str(item[1]) + " times")
        #further... if it is less than the previous value, move onto the next largest max.
        #will need a while loop to do this.

        #be sure to set the new max index when a new max is read in by the system.


print("=====^NEW^================vOLDv==================")

#need to reprint from the new array system that I am creating.
for item in categories:
    itemIndex = categories.index(item)
    print(item+" appeared: "+str(catCount[itemIndex]) + " times")
