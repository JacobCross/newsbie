import newspaper
import datetime
import urllib
import json
import sys

#news_domain = "http://cnn.com"
#news_domain = "http://www.wired.com/"
#news_domain = "https://techcrunch.com/"
news_domain = "http://www.nytimes.com/"
#news_domain = "http://www.sfgate.com/"
#news_domain = "http://www.ap.org/"

cnn_paper = newspaper.build(news_domain)

print("----------------------------------------")
print("Getting recent articles from: " + news_domain)
print("----------------------------------------")

counter = 0
final_url_list = ""
for article in cnn_paper.articles:
    counter += 1
    url = article.url
    final_url_list += "'" + url + "'," #formatting url to be added; adding
print('Fetched' + str(counter) + 'articles from ' + news_domain)

extension = "txt"
filename = input('Please enter name for new file: ')
name = filename+ "." + extension

f = open(name, 'a') #open(name, 'a')
f.write(final_url_list)
