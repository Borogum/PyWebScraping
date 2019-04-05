# coding=utf-8

# @Author: Darío M. García Carretero
# @Date:   2019-04-01T14:45:40+02:00
# @Email:  dario.aviles@gmail.com
# @Last modified by:   Darío M. García Carretero
# @Last modified time: 2019-04-04T17:37:44+02:00


import os
import re
import csv
import time
import urllib
import requests
from datetime import datetime
from  multiprocessing import Pool
from bs4 import BeautifulSoup


class FifaWorldCupCrawler(object):


    def __init__(self, max_retries=5, retry_wait=1):

        # Target web
        self.base_url = 'https://www.fifa.com/'
        # Headers for requests
        self.headers = { 'User-Agent':'Mozilla/5.0 (Macintosh;'
                         ' Intel Mac OS X 10_10_4) '
                         'AppleWebKit/537.36 (KHTML, like Gecko)'
                         ' Chrome/64.0.3282.186 Safari/537.36',
                         'X-Requested-With':'XMLHttpRequest'}
        # Max retries
        self.max_retries = max_retries
        # Time between retries
        self.retry_wait = retry_wait


    def parse_date(self, text):

         ''' Date parser. Example: 14 Jun 2018 - 18:00 '''

         return datetime.strptime(text.split('\r\n')[1].strip(), '%d %b %Y - %H:%M')


    def parse_int(self, text):

        ''' Remove units in integers. 34% -> 34 '''

        return int(re.findall(r'\d+', text)[0])


    def parse_table(self, table):

        ''' Stats parser '''

        stats = {}
        for row in table.find_all('tr', {'class': 'table__stats-progress-bar__data'}):
            items = [item.text for item in row.find_all('td')]
            label = items[1].lower().replace(' ', '_')
            stats[label + '_home'] = self.parse_int(items[0])
            stats[label + '_away'] = self.parse_int(items[2])

        return stats


    def url_request(self, url):

        ''' Makes get requests '''

        retry = 0
        r = requests.get(url, headers=self.headers)
        while (r.status_code != 200) and (retry < self.max_retries):
            retry += 1
            print('Retrying "%s" (%d/%d)' % (url, retry, self.max_retries))
            r = requests.get(url)
            time.sleep(self.retry_wait)
        if retry == self.max_retries:
            raise Exception('Unable to connect "%s"' % url)

        return r.text


    def clean_text(self, text):

        ''' Remove some problematic characters '''

        for chr in ['\u200b', '\u2028', '\u2122']:
            text = text.replace(chr,'')
        text = text.replace('\u2019',"'")
        text = text.replace('\u00a0',' ')
        text = text.replace('\u2012','-')
        text = text.replace('\u2013','-')
        text = text.replace('\u2014','-')
        text = text.replace('\u2015','-')
        return text


    def process_summary(self, text):

        ''' Split summaries '''

        expressions = [r'budweiser man of the match',
                       r'.*(\btwitter\b|\bfacebook\b)',
                      ]

        text = text.strip()
        text = re.sub(r'(\n)+', r'\n', text)
        lines = text.splitlines()
        markers = []
        for n, line in enumerate(lines):
            for exp in expressions:
                if re.match(exp, line, re.IGNORECASE):
                    markers.append(n)
            if len(markers)==3:
                break

        #Ignore "highlights"
        general = ''.join(lines[3:markers[0]-1])
        home = ''.join(lines[markers[0]+1: markers[1]])
        away = ''.join(lines[markers[1]+1: markers[2]])

        return general, home, away


    def parse_match(self, id):

        ''' Parse match info '''

        match = {'id':id}

        # General info
        url = url = urllib.parse.urljoin(self.base_url,
             '/worldcup/matches/match/{}'.format(id))
        r = self.url_request(url)
        soup = BeautifulSoup(r, 'html.parser')

        # Countries
        countries = soup.find('div', {'class':'fi-mu__m'})
        names = countries.find_all('span', {'class':'fi-t__nText'})
        codes = countries.find_all('span', {'class':'fi-t__nTri'})
        match['name_home'] = names[0].text
        match['name_away'] = names[1].text
        match['code_home'] = codes[0].text
        match['code_away'] = codes[1].text

        # General info
        info = soup.find('div', {'class':'fi-mu__info'})
        for item in ['group', 'stadium', 'venue']:
            match[item] = info.find('span', {'class':'fi__info__{}'\
            .format(item)}).text.replace(',','')

        match['datetime'] = self.parse_date(info.find('div',
         {'class':'fi-mu__info__datetime'}).text)
        match['group'] = match['group'].replace(',', '')

        # Summary
        url = urllib.parse.urljoin(self.base_url,
             '/worldcup/matches/match/{}/_libraries/_summary?qs=1'.format(id))
        r = self.url_request(url)
        soup = BeautifulSoup(r, 'html.parser')
        match['headline'] = soup.find('h1').text.strip()
        texts = soup.find_all('div', {'class':'fi-o-article__body-part--text'})
        texts = self.clean_text(''.join([text.text for text in texts]))
        match['summary'], match['summary_home'], match['summary_away'] = \
         self.process_summary(texts)

        # Stats
        url = urllib.parse.urljoin(self.base_url,
             '/live/17/season/254645/match/{}/_live_statistics?qs=1'.format(id))
        r = self.url_request(url)
        soup = BeautifulSoup(r, 'html.parser')
        for table in soup.find_all('table', {'class':'table__stats-progress-bar'}):
            match = {**match, **self.parse_table(table)}

        # Facts
        url = urllib.parse.urljoin(self.base_url,
            '/worldcup/matches/match/{}/_libraries/_matchfacts?qs=1'.format(id))
        r = self.url_request(url)
        soup = BeautifulSoup(r, 'html.parser')

        # Referee
        officials = soup.find('ul', {'class':'fi-m__officials__list'})
        official = officials.find('li')
        kind = official.find('div', {'class':'fi-m__officials__kind'})\
        .text.strip().lower().replace(':','').replace(' ', '_')
        name = ' '.join([ x.capitalize() for x in official.find('span',
        {'class':'fi-m__officials__name'}).text.strip().lower().split() ])
        country = official.find('span', {'class':'fi-m__officials__country'})\
        .text.strip().upper()
        match[kind + '_name'] = name
        match[kind + '_conrtry'] = country

        # Weather
        weather = soup.find('ul', {'class':'fi-m__weather__list'})
        match['weather_description'] = weather.find('span', {'class':'description'})\
        .text.strip().lower()

        for item in ['temperature', 'windspeed', 'humidity']:
            match['weather_{}'.format(item)] = self.parse_int( \
            weather.select('.fi-m__weather__{} .fi-m__weather__data'.format(item))[0].text)

        return match


    def get_matches_ids(self):

        ''' Returns all matches ids '''

        url = urllib.parse.urljoin(self.base_url, '/worldcup/matches')
        r = self.url_request(url)
        soup = BeautifulSoup(r, 'html.parser')
        return [x['href'].split('/')[-2]  for x in soup.find_all('a', {'class':'fi-mu__link'})]


    def crawl(self, workers=2):

        ''' Crawler process '''

        # Get all ids
        matches_ids = self.get_matches_ids()
        # Parallelize
        pool = Pool(workers)
        results = pool.map_async(self.parse_match, matches_ids)
        pool.close()
        pool.join()
        return results.get()




if __name__ == '__main__':

    crawler = FifaWorldCupCrawler()
    result = crawler.crawl(workers=4)
    # Save data into csv file
    with open('../csv/worldcup.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=result[0].keys())
        writer.writeheader()
        for row in result:
            writer.writerow(row)
