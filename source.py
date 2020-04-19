from newsapi import NewsApiClient


def supreme(s, test):
    newsapi = NewsApiClient(api_key='bb0f664df41346a38b42d10e3682c915')
    universe = []
    newsl = []
    urls = []
    title = []

    for i in s.split():
        all_news = newsapi.get_everything(q=i)
        temp = all_news.get('articles')
        for j in temp:
            universe.append(j)

    for i in universe:
        if i.get('content'):
            newsl.append(i.get('content'))
            urls.append(i.get('url'))
            title.append(i.get('title'))

    final_urls = []
    for i in s.split():
        for j in urls:
            if i in j:
                final_urls.append(j)

    l1 = []
    l2 = []

    for i in newsl:
        for j in i.split():
            l1.append(j.lower())

    for j in test.split():
        l2.append(j.lower())

    intersection = list(set([value for value in l1 if value in l2 and len(value) > 5]))
    truthfulness = True if len(intersection) > 2 else False
    links = {title[i]: urls[i] for i in range(len(title))}
    d = {"truthfulness": truthfulness, "intersection": intersection, "links":links}
    return d

