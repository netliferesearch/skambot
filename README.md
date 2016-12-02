# SKAMBOT

![Linn og Eskild og Isak](linn_og_eskild_og_isak.gif)
Skambot er gaffet fort sammen for å kunne gi oss beskjed i kanalen #skam i Slack når det har kommet noe nytt på [skam.p3.no](http://skam.p3.no). Siden NRK tilsynelatende har noen RSS-feed lengre kjører vi et lite webscraping script i Python som titter på nettsiden om det er noe nytt. Om tittelen ikke matcher den siste som er lagt i databasen, poster den en melding i Slack.

## Installere skambot

### 1. Deploy denne appen på Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

### 2. Lag en *Incoming Webhook* i Slack

![Slack Incomming Webhook](skambot_slack_config.png)

### 3. Legg til URLen i Heroku configen.

![Heroku Config](heroku_config.png)

eller `heroku config:add WEBHOOK_URL=https://hooks.slack.com/services/xxxxxxxxx/xxxxxxxxx/xxxxxxxxxxxxxxxxxxxxxxxx`

### 4. Sett opp Heroku Scheduler

![Heroku Scheduler](heroku_scheduler.png)

### 5. Vent på at det skal skje noe på [skam.p3.no](http://skam.p3.no).

![Skam i Slack](skam_i_slack.png)

Laga med :heart: av dine venner i [Netlife Research](http://www.netliferesearch.com)
