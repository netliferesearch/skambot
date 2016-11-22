# -*- coding: utf8 -*-
from bs4 import BeautifulSoup as bs
import requests as r
import sqlite3
import re
import itertools
from datetime import datetime
import json
conn = sqlite3.connect('./skambot.sqlite')
c = conn.cursor()

# Set up database
c.execute('''CREATE TABLE IF NOT EXISTS bylines
             (heading text)''')
conn.commit()

def dateifyer(dateString):
    return datetime.strptime(str(dateString), '%d.%m.%y')

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
dateRegex = r".*(\d{2}\.\d{2}\.\d{2}).*"
dates = [re.match(dateRegex, date).group(1) for date in bylines]
if [row for row in c.execute("SELECT * FROM bylines LIMIT 1")]:
    latestDate = [row for row in c.execute("SELECT * FROM bylines LIMIT 1")][0]
    latestDate = dateifyer(latestDate[0])
    latestDate > dateifyer(dates[0])
    if latestDate > dateifyer(dates[0]):
        c.execute("INSERT INTO bylines VALUES (?)", [dates[0]])
        conn.commit()
        payload = u'Noe nytt har skjedd på <http://skam.p3.no|skam.p3.no>: ' + bylines[0]
        slack_data = {'text': payload}
        slack_data
        response = requests.post(
            WEBHOOK_URL, data=json.dumps(slack_data),
            headers={'Content-Type': 'application/json'}
        )
        if response.status_code != 200:
            raise ValueError(
                'Request to slack returned an error %s, the response is:\n%s'
                % (response.status_code, response.text)
            )
