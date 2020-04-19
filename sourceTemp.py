from newsapi import NewsApiClient
from pytrends.request import TrendReq


def getTrends():
    pytrends = TrendReq(hl='en-US', tz=360)
    d = pytrends.trending_searches(pn='india').to_dict()
    d = d[0]
    ret_dic = {}
    for i in d:
        if i < 10:
            ret_dic[i + 1] = d[i]
    return list(ret_dic.values())


def supreme(test):
    newsapi = NewsApiClient(api_key='bb0f664df41346a38b42d10e3682c915')
    universe = []
    newsl = []
    urls = []
    title=[]
    s = [i for i in test.split() if len(i) > 4]

    for i in s:  # s = string with all tags
        all_news = newsapi.get_everything(q=i)  # API provides us the news for every query
        temp = all_news.get('articles')
        for j in temp:
            universe.append(j)  # universe contains all these news

    for i in universe:
        if i.get('content'):
            newsl.append(i.get('content'))
            urls.append(i.get('url'))
            title.append(i.get('title'))

    final_urls = []
    for i in s:
        for j in urls:
            if i in j:
                final_urls.append(j)

    l1 = []  # l1 contains all the words from the news where each elemet is a single word
    l2 = []  # l2 contains individual words of the news provided us by the user

    for i in newsl:
        for j in i.split():
            l1.append(j.lower())

    for j in test.split():
        l2.append(j.lower())

    intersection = list(set([value for value in l1 if value in l2 and len(value) > 3]))
    top_headlines = newsapi.get_top_headlines(q='corona', language='en', country='in')
    links = {title[i]: urls[i] for i in range(len(title))}
    latest_news =[]
    latest_urls = []
    for i in top_headlines['articles']:
        latest_news.append(i.get('title'))
        latest_urls.append(i.get('url'))
    latest_links = {latest_news[i]: latest_urls[i] for i in range(len(latest_news))}
    print(latest_news)
    if len(intersection) > 3:
        d = {"truthfulness": True, "intersection": intersection, "links": links,"trending_topics": getTrends(),"latest_links": latest_links}
    else:
        d = {"truthfulness": False, "intersection": intersection, "links": "", "trending_topics": getTrends(),"latest_links": latest_links}
    return d


"""
Input: Maharashtra lockdown extend till 30 april

news = "Maharashtra lockdown extend till 30 april"

supreme(news)
"""
