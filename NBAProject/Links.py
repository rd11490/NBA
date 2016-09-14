__author__ = 'ryan'


class Links(object):

    BASKETBALL_REFERENCE = 'http://www.basketball-reference.com'
    BASKETBALL_REFERENCE_NBA = BASKETBALL_REFERENCE+'/leagues/NBA'

    @staticmethod
    def getBasketballReferenceLeagueYearGames(year):
        return Links.BASKETBALL_REFERENCE_NBA+'_'+str(year)+'_games.html'

    @staticmethod
    def BoxScoreURLtoPBP(url):
        insert_ind = url.rfind('/')
        return url[:insert_ind] + '/pbp' + url[insert_ind:]

    @staticmethod
    def BoxScoreURLtoShotChart(url):
        insert_ind = url.rfind('/')
        return url[:insert_ind] + '/shot-chart' + url[insert_ind:]