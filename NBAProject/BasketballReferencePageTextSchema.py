__author__ = 'Ryan'

class BasketballReferencePageTextSchema(object):
    gameid = "gameid"
    type = "type"
    page = "page"
    scrapedate = "scrapedate"

    @staticmethod
    def toHeader():
        return ['gameid', 'type', 'page', 'scrapedate']
