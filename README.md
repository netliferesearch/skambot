# SKAMBOT

![Linn og Eskild og Isak](img/linn_og_eskild_og_isak.gif)

Skambot er gaffet fort sammen for å kunne gi oss beskjed i kanalen #skam i Slack når det har kommet noe nytt på [skam.p3.no](http://skam.p3.no). Siden NRK tilsynelatende har noen RSS-feed lengre kjører vi et lite webscraping script i Python som titter på nettsiden om det er noe nytt. Om tittelen ikke matcher den siste som er lagt i databasen, poster den en melding i Slack.

## Installere skambot

### 1. Lag en *Incoming Webhook* i Slack

![Slack Incomming Webhook](img/skambot_slack_config.png)

### 2. Deploy denne appen på Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/netliferesearch/skambot/tree/master)

Det kan være en fordel å sette *Runtime Selection* til Europe.

### 3. Legg til URLen i Heroku configen, om du ikke allerede har gjort det.

![Heroku Config](img/heroku_config.png)

eller `heroku config:add WEBHOOK_URL=https://hooks.slack.com/services/xxxxxxxxx/xxxxxxxxx/xxxxxxxxxxxxxxxxxxxxxxxx`

### 4. Sett opp Heroku Scheduler

Du finner Heroku Scheduler under *Resources* -> *Add-ons* i Heroku-dashboardet. Klikk på den for å stille inn.

![Heroku Scheduler](img/heroku_scheduler.png)

### 5. Vent på at det skal skje noe på [skam.p3.no](http://skam.p3.no).

![Skam i Slack](img/skam_i_slack.png)

Laga med :heart: av dine venner i [Netlife Research](http://www.netliferesearch.com).

![Fra Julebordet](img/netlife_julebord_nytt_skamklipp.jpg)
*Når man er på julebord og det kommer et nytt SKAM-klipp*
