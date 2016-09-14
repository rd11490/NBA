__author__ = 'Ryan'

class BasketballRefereneceGameLinksSchema(object):

    gameid = "gameid"
    date = "date"
    time = "time"
    awayid = "awayid"
    awayscore = "awayscore"
    homeid = "homeid"
    homescore = "homescore"
    boxscorelink = "boxscorelink"
    year = "year"
    scrapedate = "scrapedate"

    @staticmethod
    def toHeader():
        return ['gameid',
               'date',
               'time',
               'awayid',
               'awayscore',
               'homeid',
               'homescore',
               'boxscorelink',
               'year',
               'scrapedate']
