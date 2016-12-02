# -*- coding: utf8 -*-
from bs4 import BeautifulSoup as bs
from datetime import datetime
import itertools
import json
import requests as r
import re
import os
import psycopg2
import urllib.parse

from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

WEBHOOK_URL = os.environ.get("WEBHOOK_URL")
DATABASE_URL = os.environ.get("DATABASE_URL")

urllib.parse.uses_netloc.append("mysql")
url = urllib.parse.urlparse(DATABASE_URL)

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS updates2(id serial PRIMARY KEY, title VARCHAR (255) UNIQUE NOT NULL);")
conn.commit()

def post_to_slack(tittel, url, r):
    payload = u'Noe nytt har skjedd på SKAM: <' + url + '|'+tittel+'>'
    slack_data = {'text': payload}
    response = r.post(
        WEBHOOK_URL, data=json.dumps(slack_data),
        headers={'Content-Type': 'application/json'}
    )
    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )

page = r.get('http://skam.p3.no')
content = page.content
soup = bs(content, "html.parser")
articles = soup.find_all('article')
bylines = [byline.text.replace('\n','') for byline in soup.select('.byline')]
link = articles[0].find_all('a', href=True)[0]['href']

cursor.execute("SELECT * FROM updates2 ORDER BY ID DESC")
records = cursor.fetchall()

if not records:
    cursor.execute("INSERT INTO updates2 (title) VALUES (%s) ON CONFLICT DO NOTHING", ["Skambot ass."])
    conn.commit()
    print("Måtte lissom legge noe i tabellen a")
if records:
    if records[0][1] != bylines[0]:
        # post_to_slack(bylines[0], link, r)
        cursor.execute("INSERT INTO updates2 (title) VALUES (%s)", [bylines[0]])
        conn.commit()
        print('Awsm! Ny episode :) :) :)')
    else:
        print('Ingenting nytt :(')
conn.close()
