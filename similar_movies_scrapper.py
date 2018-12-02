#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 17:53:19 2018

@author: omer farooq ahmed
"""
import numpy as np
from bs4 import BeautifulSoup as soup
import requests
from urllib.parse import urlparse
import json
import random

def main():
    similar_movies_json = []
    # read json data from budgets file
    with open('movie_budget.json') as movie_data:
        data = json.load(movie_data)
    html = ''
    # scrape data of similar movies from each movie
    for i in range(0, len(data)):
        imdb_url = data[i]['imdb_url']
        if (imdb_url == '' or imdb_url is None):
            break
        movie_name = data[i]['movie_name']
        movie_data = {}
        movie_data['movie_name'] = movie_name
        movie_data['imdb_url'] = imdb_url
        print(imdb_url)
        useragent = gen_user_agent()
        try:
            headers = {'User-Agent' : useragent}
            response = requests.get(imdb_url, headers = headers)
            html = response.text
        except:
            print('Connection Failed')
            break
        html_soup = soup(html, 'html.parser')
        similar_movies = html_soup.find_all('div', {'class' : 'rec_overview'})
        similar_movies_data = []
        for movie in similar_movies:
            similar_movie_title = movie.find('div', {'class' : 'rec-title'})
            print(similar_movie_title.a.b.text)
            value = {}
            value['title'] = similar_movie_title.a.b.text
            similar_movie_rating = movie.find('span', {'class' : 'rating-rating'})
            similar_movie_rating_value = similar_movie_rating.find('span', {'class' : 'value'})
            print(similar_movie_rating_value.text)
            value['rating'] = similar_movie_rating_value.text
            similar_movies_data.append(value)
        # end for
        movie_data['similar_movies'] = similar_movies_data
        print(json.loads(json.dumps(movie_data)))
        similar_movies_json.append(movie_data)
    with open('similar_movies_data.json', 'w') as outfile:
        json.dump(similar_movies_json, outfile)

        
        
# end main
        
# return a random user agent
def gen_user_agent():
    return random.choice(USER_AGENT_LIST)
# end gen_user_agent
    

USER_AGENT_LIST = [
    #Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    #Firefox
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
]

main()