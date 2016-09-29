#WHEN RUNNING THIS FILE - MUST RUN AS:
# > sudo python3 newspaperTester.py

import newspaper
import datetime
import urllib
import json

from operator import itemgetter, attrgetter


old_api_key = "c1c260da3b9e4723186408e9baccf626fc1ea92c"
new_api_key_free = "a46af75e70d98ff92433484372e2c03005a1f180"
base_url = "http://gateway-a.watsonplatform.net/calls/url/URLGetCombinedData?extract=page-image,entity,keyword,taxonomy&apikey=a46af75e70d98ff92433484372e2c03005a1f180&showSourceText=0&sentiment=1&quotations=1&outputMode=json&url="

##################ATTENTION HERE TODO#######################
#
# you can also use f.read(file.txt) or something like it - check i/o on python page.
# use this to read in text from a different file.
#
###########################################################

categories = []
catCount = []
sortedList = []
counter = 0

#news_domain = "http://cnn.com"
#news_domain = "http://www.wired.com/"
#news_domain = "https://techcrunch.com/"
#news_domain = "http://www.nytimes.com/"
#news_domain = "http://www.sfgate.com/"


#cnn_paper = newspaper.build(news_domain)

tempList1 = ["http://www.cnn.com/2016/06/16/us/orlando-shooter-omar-mateen/index.html","http://www.cnn.com/2016/06/16/politics/obama-visit-orlando-shooting/index.html","http://www.cnn.com/2016/06/16/europe/russia-hooligans-chance/index.html","http://www.cnn.com/2016/06/16/europe/british-mp-jo-cox-attacked/?iid=ob_lockedrail_topeditorial","http://www.cnn.com/2016/06/15/politics/donald-trump-republican-leaders-by-myself/?iid=ob_lockedrail_topeditorial","http://bleacherreport.com/articles/2646582-carson-wentz-locked-inside-gas-station-bathroom-rescued-by-guys-leg-kick?iid=ob_lockedrail_topeditorial","http://www.cnn.com/2016/09/15/politics/mike-pence-donald-trump-2016-election-erin-burnett/index.html","http://www.cnn.com/2016/09/15/politics/guantanamo-bay-house-bill-terrorism/index.html","http://money.cnn.com/2016/09/14/technology/eu-copyright-youtube-payments/index.html?iid=surge-story-summary","http://www.cnn.com/2016/09/15/us/ohio-columbus-police-kill-teen/index.html","http://money.cnn.com/2016/09/15/investing/john-boehner-smoking-joins-tobacco-company/index.html?iid=ob_lockedrail_topeditorial","http://www.cnn.com/2016/06/16/us/orlando-shooter-omar-mateen/index.html","http://www.cnn.com/2016/06/16/politics/obama-visit-orlando-shooting/index.html","http://www.cnn.com/2016/06/16/europe/russia-hooligans-chance/index.html","http://www.cnn.com/2016/06/16/europe/british-mp-jo-cox-attacked/?iid=ob_lockedrail_topeditorial","http://www.cnn.com/2016/06/15/politics/donald-trump-republican-leaders-by-myself/?iid=ob_lockedrail_topeditorial","http://bleacherreport.com/articles/2646582-carson-wentz-locked-inside-gas-station-bathroom-rescued-by-guys-leg-kick?iid=ob_lockedrail_topeditorial","http://www.cnn.com/2016/09/15/politics/mike-pence-donald-trump-2016-election-erin-burnett/index.html","http://www.cnn.com/2016/09/15/politics/guantanamo-bay-house-bill-terrorism/index.html","http://money.cnn.com/2016/09/14/technology/eu-copyright-youtube-payments/index.html?iid=surge-story-summary","http://www.cnn.com/2016/09/15/us/ohio-columbus-police-kill-teen/index.html","http://money.cnn.com/2016/09/15/investing/john-boehner-smoking-joins-tobacco-company/index.html?iid=ob_lockedrail_topeditorial","http://money.cnn.com/2016/09/15/investing/john-boehner-smoking-joins-tobacco-company/index.html?iid=ob_lockedrail_topeditorial","http://money.cnn.com/2016/09/15/investing/john-boehner-smoking-joins-tobacco-company/index.html?iid=ob_lockedrail_topeditorial","http://money.cnn.com/2016/09/15/investing/john-boehner-smoking-joins-tobacco-company/index.html?iid=ob_lockedrail_topeditorial","http://money.cnn.com/2016/09/15/investing/john-boehner-smoking-joins-tobacco-company/index.html?iid=ob_lockedrail_topeditorial","http://money.cnn.com/2016/09/15/investing/john-boehner-smoking-joins-tobacco-company/index.html?iid=ob_lockedrail_topeditorial","http://money.cnn.com/2016/09/15/investing/john-boehner-smoking-joins-tobacco-company/index.html?iid=ob_lockedrail_topeditorial","http://money.cnn.com/2016/09/15/investing/john-boehner-smoking-joins-tobacco-company/index.html?iid=ob_lockedrail_topeditorial","http://money.cnn.com/2016/09/15/investing/john-boehner-smoking-joins-tobacco-company/index.html?iid=ob_lockedrail_topeditorial","http://money.cnn.com/2016/09/15/investing/john-boehner-smoking-joins-tobacco-company/index.html?iid=ob_lockedrail_topeditorial","http://www.cnn.com/2016/06/16/europe/british-mp-jo-cox-attacked/?iid=ob_lockedrail_topeditorial","http://www.cnn.com/2016/06/16/us/orlando-shooter-omar-mateen/index.html","http://www.cnn.com/2016/06/16/politics/obama-visit-orlando-shooting/index.html","http://www.cnn.com/2016/06/16/europe/russia-hooligans-chance/index.html","http://www.cnn.com/2016/06/16/europe/british-mp-jo-cox-attacked/?iid=ob_lockedrail_topeditorial"]

tempList = []

print("----------------------------------------")
print("Getting recent articles from: tempList") #news_domain)
print("----------------------------------------")

for url in tempList1:
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

print('b4 sort')
for x in sortedList:
    print(x)

print('after sort')
print(sorted(sortedList, key=itemgetter(1), reverse=True))

print("=====^NEW^================vOLDv==================")

#need to reprint from the new array system that I am creating.
for item in categories:
    itemIndex = categories.index(item)
    print(item+" appeared: "+str(catCount[itemIndex]) + " times")

print()
print("----------------------------------------")
print("Articles Fetched: "+str(counter))
print("----------------------------------------")
#implementing sqlite database to store urls
#currentDate = datetime.datetime.now().date()
