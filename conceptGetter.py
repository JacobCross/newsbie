import newspaper
import datetime
import urllib
import json

from operator import itemgetter, attrgetter
from newsbie_config import *

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

tempList = ['http://www.nytimes.com/2016/10/02/movies/the-siege-of-jadotville-on-netflix-rediscovers-a-faded-footnote.html','http://www.nytimes.com/2016/09/28/opinion/has-pope-francis-failed.html','http://www.nytimes.com/2016/09/28/briefing/us-congress-el-cajon.html?partner=rss&amp;emc=rss','http://www.nytimes.com/2016/09/28/opinion/4-1-miles.html?hp&target=comments#commentsContainer','http://www.nytimes.com/slideshow/2016/09/28/t-magazine/fashion/jacquemus-ysl-saint-laurent-koche-paris-fashion-week.html','http://www.nytimes.com/interactive/2016/09/28/world/middleeast/shimon-peres-quotes.html','http://www.nytimes.com/2016/09/29/world/middleeast/shimon-peres-israel.html','http://www.nytimes.com/2016/09/29/upshot/if-your-vote-doesnt-really-count-is-there-anything-you-can-do.html','http://www.nytimes.com/2016/09/29/us/politics/hillary-clinton-democrats.html','http://www.nytimes.com/2016/09/29/nyregion/2-men-who-found-unexploded-bomb-in-travel-bag-in-chelsea-are-identified.html','http://www.nytimes.com/2016/09/28/books/hitler-ascent-volker-ullrich.html?partner=rss&amp;emc=rss','http://www.nytimes.com/2016/09/29/theater/romeo-castellucci-the-provocative-italian-stage-director.html','http://www.nytimes.com/2016/09/29/sports/baseball/tim-tebow-homers-in-first-at-bat-as-a-professional.html?partner=rss&amp;emc=rss','http://www.nytimes.com/2016/09/29/nyregion/oral-nicholas-hillary-potsdam-murder-trial-garrett-phillips.html','http://www.nytimes.com/2016/10/02/magazine/marilyn-mosby-freddie-gray-baltimore.html?partner=rss&amp;emc=rss','http://www.nytimes.com/2016/09/28/us/california-today-basketball-kevin-durant-warriors.html','http://www.nytimes.com/2016/09/28/fashion/a-look-at-rihannas-fenty-for-puma-collection-paris-fashion-week.html','http://www.nytimes.com/2015/12/20/opinion/sunday/the-one-question-you-should-ask-about-every-new-job.html','http://www.nytimes.com/2016/10/02/movies/heavens-gate-comes-to-bamcinematek.html','http://www.nytimes.com/2016/09/29/business/economy/more-wealth-more-jobs-but-not-for-everyone-what-fuels-the-backlash-on-trade.html?hp&target=comments#commentsContainer','http://www.nytimes.com/2016/09/29/world/middleeast/obama-troops-iraq.html','http://www.nytimes.com/2016/09/29/theater/provincetown-tennessee-william-theater-festival-eugene-oneill.html','http://www.nytimes.com/2016/09/28/opinion/the-deaf-body-in-public-space.html','http://www.nytimes.com/2016/09/28/opinion/hillary-clintons-everywoman-moment.html','http://www.nytimes.com/2016/10/02/arts/music/elvis-costellos-new-york-soul.html?partner=rss&amp;emc=rss','http://www.nytimes.com/roomfordebate/2016/09/28/should-the-us-give-up-oversight-of-internet-addresses','http://www.nytimes.com/2016/09/29/business/dealbook/arbitration-nursing-homes-elder-abuse-harassment-claims.html','http://www.nytimes.com/2016/09/29/us/should-you-intervene-when-a-parent-harshly-disciplines-a-child-in-public.html','http://www.nytimes.com/2016/09/28/t-magazine/fashion/alessandro-michele-gucci-set-design-fashion-week.html','http://www.nytimes.com/2016/09/29/technology/personaltech/virtual-realitys-possibilities-lure-video-game-developers.html','http://www.nytimes.com/2016/09/28/t-magazine/fashion/dries-van-noten-beauty-paris-fashion-week.html','http://www.nytimes.com/2016/09/28/insider/how-i-got-the-shot-times-photographers-on-preparing-for-a-presidential-showdown.html','http://www.nytimes.com/2016/10/02/books/review/iran-wars-jay-solomon.html','http://www.nytimes.com/2016/09/28/movies/herschell-gordon-lewis-a-pioneer-of-gore-cinema-dies-at-90.html','http://www.nytimes.com/2016/09/28/opinion/mr-corbyns-labour-party.html','http://www.nytimes.com/2016/09/29/technology/yahoo-data-breach-hacking.html','http://lens.blogs.nytimes.com/2016/09/28/on-the-prowl-with-a-wildlife-photographer/feed/','http://www.nytimes.com/2016/09/29/business/dealbook/california-wells-fargo-john-stumpf.html','http://www.nytimes.com/2016/09/28/business/economy/what-can-mexico-do-about-trump.html','http://www.nytimes.com/2016/10/02/travel/budget-family-frugal-montana.html','http://www.nytimes.com/2016/09/28/insider/times-insider-photo-challenge-caption-this.html','http://www.nytimes.com/2016/09/28/world/middleeast/shimon-peres-dies-israel.html','http://www.nytimes.com/2016/09/29/nyregion/mr-wolf-sought-to-fix-bridge-scandal-ex-christie-ally-testifies.html?partner=rss&amp;emc=rss','http://www.nytimes.com/2016/10/02/realestate/real-estate-in-costa-rica.html','http://www.nytimes.com/2015/12/20/opinion/sunday/the-one-question-you-should-ask-about-every-new-job.html?partner=rss&amp;emc=rss','http://www.nytimes.com/2016/09/28/crosswords/wheres-the-downside.html','http://www.nytimes.com/2016/10/02/fashion/brian-anderson-skateboarding-gay-coming-out-vice-sports.html','http://www.nytimes.com/2016/09/28/opinion/sympathy-for-the-donald.html','http://www.nytimes.com/2016/09/28/us/joe-browder-dead.html','http://www.nytimes.com/2016/09/28/movies/review-sand-storm-follows-a-bedouin-mother-and-daughter-in-quiet-revolts.html','http://www.nytimes.com/2016/09/29/opinion/shimon-peres-a-dreamer-of-peace-for-israel.html','http://www.nytimes.com/2016/09/29/science/ancient-european-malaria-dna.html','http://www.nytimes.com/2016/09/29/arts/music/review-laura-benanti-tales-from-soprano-isle-cafe-carlyle.html','http://www.nytimes.com/2016/09/29/sports/baseball/tim-tebow-homers-in-first-at-bat-as-a-professional.html','http://www.nytimes.com/2016/09/29/us/townville-school-shooting-south-carolina.html','http://www.nytimes.com/2016/09/29/science/milky-way-stars-3-d-map.html','http://www.nytimes.com/2016/09/28/magazine/donald-trump-sean-hannity-and-a-still-elusive-tape.html','http://www.nytimes.com/2016/09/29/nyregion/2-men-who-found-unexploded-bomb-in-travel-bag-in-chelsea-are-identified.html?partner=rss&amp;emc=rss','http://www.nytimes.com/2016/09/28/opinion/4-1-miles.html','http://www.nytimes.com/2016/09/29/business/dealbook/arbitration-nursing-homes-elder-abuse-harassment-claims.html?hp&target=comments#commentsContainer','http://www.nytimes.com/2016/09/28/us/keith-lamont-scott-charlote-police-shooting.html','http://www.nytimes.com/2016/09/29/us/politics/obama-trump.html?partner=rss&amp;emc=rss','http://www.nytimes.com/2016/09/28/business/economy/charles-l-schultze-91-dies-advised-presidents-on-economic-policy.html','http://www.nytimes.com/2016/09/29/nyregion/mr-wolf-sought-to-fix-bridge-scandal-ex-christie-ally-testifies.html','http://www.nytimes.com/2016/09/29/books/review-the-moth-snowstorm-and-other-natural-bliss-outs.html','http://www.nytimes.com/2016/09/28/sports/golf/michael-phelps-retirement-olympics.html','http://www.nytimes.com/2016/09/28/world/middleeast/behind-the-scenes-travelling-with-shimon-peres.html','http://www.nytimes.com/2016/09/28/t-magazine/fashion/azuma-makoto-dries-van-noten-paris-fashion-week.html','http://www.nytimes.com/2016/10/02/magazine/marilyn-mosby-freddie-gray-baltimore.html','http://www.nytimes.com/2016/09/24/opinion/adventures-on-the-china-golf-tour.html','http://www.nytimes.com/2016/09/28/arts/joan-of-arcs-shaky-pedestal-france-battles-over-its-identity-at-school.html','http://www.nytimes.com/2016/09/29/technology/protecting-humans-and-jobs-from-robots-is-5-tech-giants-goal.html','http://www.nytimes.com/2016/09/29/us/politics/hillary-clinton-democrats.html?partner=rss&amp;emc=rss','http://www.nytimes.com/2016/09/29/sports/baseball/vin-scully-los-angeles-dodgers-retire-broadcasting.html','http://www.nytimes.com/2016/09/28/science/elon-musk-spacex-mars-exploration.html','http://www.nytimes.com/2016/09/29/world/middleeast/israel-shimon-peres.html?partner=rss&amp;emc=rss','http://www.nytimes.com/2016/09/29/us/politics/senate-votes-to-override-obama-veto-on-9-11-victims-bill.html','http://www.nytimes.com/2016/09/28/world/middleeast/behind-the-scenes-travelling-with-shimon-peres.html?partner=rss&amp;emc=rss','http://www.nytimes.com/2016/09/29/world/middleeast/obama-troops-iraq.html?partner=rss&amp;emc=rss','http://www.nytimes.com/2016/09/29/technology/yahoo-data-breach-hacking.html?partner=rss&amp;emc=rss','http://www.nytimes.com/2016/09/29/fashion/dior-the-collection-amazon-prime-television.html','http://www.nytimes.com/2015/12/20/opinion/sunday/the-one-question-you-should-ask-about-every-new-job.html?hp&target=comments#commentsContainer','http://www.nytimes.com/2016/09/29/business/economy/more-wealth-more-jobs-but-not-for-everyone-what-fuels-the-backlash-on-trade.html','http://www.nytimes.com/2016/09/28/sports/soccer/england-manager-sam-allardyce-undone-by-an-undercover-film.html','http://www.nytimes.com/2016/10/02/books/review/blood-at-the-root-patrick-phillips.html','http://www.nytimes.com/2016/10/02/arts/music/elvis-costellos-new-york-soul.html','http://www.nytimes.com/2016/09/27/arts/international/with-oliver-twist-a-french-musical-aims-higher.html','http://www.nytimes.com/2016/09/29/world/kristalina-georgieva-candidate-secretary-general.html','http://www.nytimes.com/2016/09/29/world/middleeast/israel-shimon-peres.html','http://www.nytimes.com/2016/10/02/realestate/compare-homes-in-tucson-arizona-portsmouth-rhode-island-and-tiburon-california.html']

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
