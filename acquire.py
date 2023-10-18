# imports
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import random
import os



    
def acquire_codeup_blog():
    '''webscrapes from codeup blogs'''

    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0",
        "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0"
        ]
    user_agents = random.choice(user_agents)
    headers = {'User-Agent': user_agents[0]}
    base_url = 'https://codeup.edu/blog/'
    base_soup = BeautifulSoup(response.text, 'html.parser')
    blog_links = [element['href'] for element in base_soup.find_all('a', class_='more-link')]
    
    blog_contents = []
    for link in blog_links:
        response = response.get(link, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('h1', class_='entry-title').text
        body = soup.find('div', class_='entry-content').text.strip()

        row = {'title' : title, 'article': body}

        blog_contents.append(row)
    blog_arts = pd.DataFrame(blog_contents)
    return blog_arts




def acquire_news_articles():
    '''webscrapes from '''

    base_url = 'https://inshorts.com/en/read/'
    categories = ['business', 'sports', 'technology', 'entertainment']

    
    all_articles = pd.DataFrame(columns=['title','body','category'])
    for category in categories:

        category_url = base_url + category

        raw_content = requests.get(category_url).text
        soup = BeautifulSoup(raw_content, 'html.parser')

        title = [element.text for element in soup.find_all('span', itemprop='headline')]
        bodies = [element.text for element in soup.find_all('div', itemprop='articleBody')]
        category_df = pd.DataFrame({'title': title, 'body': bodies, 'category': category})

        all_articles = pd.concat([all_articles, category_df], axis=0, ignore_index=True)
    return all_articles