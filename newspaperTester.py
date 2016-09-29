#WHEN RUNNING THIS FILE - MUST RUN AS:
# > sudo python3 newspaperTester.py

import newspaper
import datetime
import urllib
import json

base_url = "http://gateway-a.watsonplatform.net/calls/url/URLGetCombinedData?extract=page-image,entity,keyword,taxonomy&apikey=c1c260da3b9e4723186408e9baccf626fc1ea92c&showSourceText=0&sentiment=1&quotations=1&outputMode=json&url="

categories = []
catCount = []
counter = 0
news_domain = "http://cnn.com"

cnn_paper = newspaper.build(news_domain)

tempList = ["http://www.cnn.com/2016/06/16/us/orlando-shooter-omar-mateen/index.html","http://www.cnn.com/2016/06/16/politics/obama-visit-orlando-shooting/index.html","http://www.cnn.com/2016/06/16/europe/russia-hooligans-chance/index.html","http://www.cnn.com/2016/06/16/europe/british-mp-jo-cox-attacked/?iid=ob_lockedrail_topeditorial","http://www.cnn.com/2016/06/15/politics/donald-trump-republican-leaders-by-myself/?iid=ob_lockedrail_topeditorial","http://bleacherreport.com/articles/2646582-carson-wentz-locked-inside-gas-station-bathroom-rescued-by-guys-leg-kick?iid=ob_lockedrail_topeditorial"]

print("----------------------------------------")
print("Getting recent articles from: " + news_domain)
print("----------------------------------------")

for article in tempList: #use cnn_paper.articles for the real thing
    counter+=1

    #constructing the url using newspaper API
    news_url = article #use article.url for the real thing
    final_url = base_url + news_url

    #getting the json data from AlchemyAPI
    jdata = urllib.request.urlopen(final_url).read()
    string = jdata.decode("utf-8")
    data = json.loads(string)

    #this is our primary category given to the article by Watson
    category = data['taxonomy'][0]['label']
    if categories.count(category)==0:
        print('NEW')
        categories.append(category)
        catCount.append(1);
        #categories[categories.index(category)].append([1])
    elif categories.count(category==1):
        print('ADDING TO EXISTING')
        catCount[categories.index(category)]+=1
        #categories[categories.index(category)][1]+=1


for item in categories:
    itemIndex = categories.index(item)
    print(itemIndex)
    print(item+" appeared: "+str(catCount[itemIndex]) + " times")

print()
print("----------------------------------------")
print("Articles Fetched: "+str(counter))
print("----------------------------------------")
#implementing sqlite database to store urls
#currentDate = datetime.datetime.now().date()
