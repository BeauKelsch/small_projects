#
#
#
#

from requests_html import HTMLSession
session = HTMLSession()
url = 'https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en'

r = session.get(url)

r.html.render(sleep=5, scrolldown=5)

articles = r.html.find('article')

newslist = []

for i in articles:
    try:
        newsitem = i.find('h3', first=True)
        newsarticle = {
        'title' : newsitem.text,
        #'link' : newsitem.absolute_links
        }
        newslist.append(newsarticle)
    except:
        pass

print ("There are ", len(newslist), " articles I can currently pull from Google News.")
count = 0
for i in newslist:
    print (newslist[count])
    count = count + 1