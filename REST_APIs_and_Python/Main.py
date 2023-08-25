import requests

# r = requests.get('https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2023-7-23&to=2023-7-24&sortBy=popularity&language=en&apiKey=351d9501b20444329cff8b5847df7282')



def get_news(topic,from_date, to_date, language='en',api_key='351d9501b20444329cff8b5847df7282'):
    url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key}'

    r = requests.get(url)
    #print(r)
    content =  r.json()
    #print(content)
    articles = content['articles']
    result =[]
    for article in articles:
        result.append(f"TITLE\n{article['title']}, '\n Description\n', {article['description']}")
    return result
# print(get_news(topic='space',from_date='2023-8-24',to_date='2023-8-25'))

def get_News_with_CountryName(country='US' , api_key='351d9501b20444329cff8b5847df7282'):
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'
    
    r = requests.get(url)
    content = r.json()
    #print(content)
    articles = content['articles']
    result =[]
    for article in articles:
        result.append(f"TITLE\n{article['title']}, '\n Description\n', {article['description']}")
    return result

found = get_News_with_CountryName()
print(found)
    