from bs4 import BeautifulSoup as bs
import requests as r
import sqlite3

conn = sqlite3.connect('./skambot.sqlite')
c = conn.cursor()

# Set up database
c.execute('''CREATE TABLE IF NOT EXISTS bylines
             (date text, heading text)''')
conn.commit()
conn.close()


WEBHOOK_URL = "https://hooks.slack.com/services/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"

'''
payload={"text": "A very important thing has occurred! <https://alert-system.com/alerts/1234|Click here> for details!"}

'''
page = r.get('http://skam.p3.no')
content = page.content
soup = bs(content)
articles = soup.find_all('article')
bylines = [byline.string for byline in soup.select('.byline a')]
dates = [date for date in bylines]
date
c.execute("INSERT INTO bylines VALUES (?,?)", bylines[0])
