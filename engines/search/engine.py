import urllib
import json

urlPrefix = "https://help.bingads.microsoft.com/#apex/3/en/"

def __getBingUrl(kwlist):
    kwstring = '+'.join(kwlist)
    urlpattern = "https://help.bingads.microsoft.com/api/apexapi?id=3&language=en&query={0}&nav="
    return urlpattern.format(kwstring)

def __getSolutionUrl(SecretKey, Nav):
    return urlPrefix + SecretKey +'/'+Nav 

def __urlCrawler(url):
    return urllib.urlopen(url).read()


def __search(question):
    kwlist = question.split(' ')
    url = __getBingUrl(kwlist)
    text = __urlCrawler(url)
    
    ent = json.loads(text)
    topics = ent['Topics']
    if topics:
        i = topics[0]
        Title = i['Title'].replace("<span class='highlight'>", "").replace("</span>", "")
        Summary = i['Summary'].replace("<span class='highlight'>", "").replace("</span>", "")
        url = __getSolutionUrl(i['SecretKey'],i['Nav'])
        return [Title, Summary, url]

def Ask(question):
    response = __search(question)
    if response:
        answer = "`Are you asking:` \n\t\t" + "*{0}*".format(response[0]) + '?\n'
        answer += "`I know that...` \n\t" + response[1] + '\n'
        answer += '`Please click this URL:` \n\t' + response[2] + '\n'
    else:
        answer = "Sorry, cannot answer this question."
    return answer