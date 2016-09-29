from newsbie_config import *

print(API_KEY)

base_url = "http://gateway-a.watsonplatform.net/calls/url/URLGetCombinedData?extract=page-image,concepts,entity,keyword,taxonomy&apikey="+API_KEY+"&showSourceText=0&sentiment=1&quotations=1&outputMode=json&url="

print(base_url)
