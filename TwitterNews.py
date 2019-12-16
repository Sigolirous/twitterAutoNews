import tweepy as tweepy
import requests
from bs4 import BeautifulSoup as BS
import time as t
auth = tweepy.OAuthHandler("Developer key", "developer secret")
auth.set_access_token("User key","user secret")
api = tweepy.API(auth)
continents = ['America', 'Asia', 'Africa', 'Europe', 'Oceania']


for continent in continents:
    page = requests.get(f"https://www.bbc.co.uk/search?q={continent}&filter=news&suggid=#page=2")
    soup = BS(page.content, 'html.parser')
    h1 = soup.find_all('h1', itemprop ='headline')
    for news in h1:
        print(news.get_text())
        print(news.find('a').get('href'))
        try:
            api.update_status(f"{continent}\n{news.get_text()}\n{news.find('a').get('href')}")
        except:
            print(f"Not able to post \n{continent}\n{news.get_text(news.find('a').get('href'))}")
        t.sleep(30)
