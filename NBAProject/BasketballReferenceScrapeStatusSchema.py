__author__ = 'Ryan'

class BasketballReferenceScrapeStatusSchema(object):

    gameid = "gameid"
    link_scrapedate = "link_scrapedate"
    boxscore_scrapedate = "boxscore_scrapedate"
    play_by_play_scrapedate = "play_by_play_scrapedate"
    shotchart_scrapedate = "shotchart_scrapedate"
    boxscore_parsedate = "boxscore_parsedate"
    play_by_play_parsedate = "play_by_play_parsedate"
    shotchart_parsedate = "shotchart_parsedate"


    @staticmethod
    def toHeader():
        return ['gameid',
                "link_scrapedate",
                "boxscore_scrapedate",
                "play_by_play_scrapedate",
                "shotchart_scrapedate",
                "boxscore_parsedate",
                "play_by_play_parsedate",
                "shotchart_parsedate"]
