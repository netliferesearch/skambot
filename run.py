# -*- coding: utf8 -*-
from bs4 import BeautifulSoup as bs
from datetime import datetime
import itertools
import json
import requests as r
import re

import os
import psycopg2
'''
import urlparse

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)
'''
def dateifyer(dateString):
    return datetime.strptime(str(dateString), '%d.%m.%y')

def post_to_slack(url, r):
    payload = u'Noe nytt har skjedd på SKAM: ' + url
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

WEBHOOK_URL = "https://hooks.slack.com/services/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"

'''
payload={"text": "A very important thing has occurred! <https://alert-system.com/alerts/1234|Click here> for details!"}

'''
page = r.get('http://skam.p3.no')
content = page.content
soup = bs(content, "html.parser")
articles = soup.find_all('article')
articles[0].select('img')[0]
bylines = [byline.string for byline in soup.select('.byline a')]
link = articles[0].find_all('a', href=True)[0]['href']
post_to_slack(link, r)
'''
dateRegex = r".*(\d{2}\.\d{2}\.\d{2}).*"
dates = [re.match(dateRegex, date).group(1) for date in bylines]
if [row for row in c.execute("SELECT * FROM bylines LIMIT 1")]:
    latestDate = [row for row in c.execute("SELECT * FROM bylines LIMIT 1")][0]
    latestDate = dateifyer(latestDate[0])
    latestDate > dateifyer(dates[0])
    if latestDate > dateifyer(dates[0]):
        c.execute("INSERT INTO bylines VALUES (?)", [dates[0]])
        conn.commit()
'''
