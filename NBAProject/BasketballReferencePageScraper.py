from datetime import datetime
import argparse

from cassandra.cluster import Cluster
import requests

from BasketballReferencePageTextSchema import BasketballReferencePageTextSchema
from BasketballReferenceScrapeStatusSchema import BasketballReferenceScrapeStatusSchema
from CassandraQueryBuilder import CassandraQueryBuilder
from CassandraTables import CassandraTables


__author__ = 'Ryan'

"""
CREATE TABLE nba.basketball_reference_page_text_table (
gameid text,
type text,
page text,
scrapedate text,
PRIMARY KEY (type, gameid)
);

"""


class BasketballReferencePageScraper:
    def __init__(self):
        self.cluster = Cluster()
        self.session = self.cluster.connect(CassandraTables.KEYSPACE_NBA)
        self.scrapeDate = str(datetime.today())


    def process(self, pageType):
        column = self.getColumnFromPageType(pageType)
        gameids = self.selectSource(column)
        links = self.selectLinks(gameids)
        for r in links:
            self.extractPage(r, pageType, column)


    def extractPage(self, row, pageType, column):
        r = requests.get(row.boxscorelink)
        self.writePageToTable(row.gameid, pageType, r.text)
        self.updateSourceTable(row.gameid, column)


    def updateSourceTable(self, gameId, column):
        self.session.execute(
            CassandraQueryBuilder.updateQueryBuilder(CassandraTables.BASKETBALLREFERENCE_SCRAPE_STATUS_TABLE,
                                                     "{0}=$${1}$$".format(column, self.scrapeDate),
                                                     ["gameid=\'{0}\'".format(gameId)]))

    def writePageToTable(self, gameId, pageType, text):
        self.session.execute(
            CassandraQueryBuilder.insertInto(CassandraTables.BASKETBALLREFERENCE_PAGE_TEXT,
                                             BasketballReferencePageTextSchema.toHeader(),
                                             [gameId, pageType, text, self.scrapeDate]
            )
        )

    def selectLinks(self, gameids):
        return self.session.execute(
            CassandraQueryBuilder.selectFrom(CassandraTables.BASKETBALLREFERENCE_GAME_LINKS_TABLE,
                                             ['gameid', 'boxscorelink'],
                                             [CassandraQueryBuilder.inClause('gameid', gameids)]))

    def selectSource(self, column):
        source = self.session.execute(
            CassandraQueryBuilder.selectFrom(CassandraTables.BASKETBALLREFERENCE_SCRAPE_STATUS_TABLE,
                                             ['gameid'],[column + "=''"]))
        return [r.gameid for r in source.current_rows]

    def getColumnFromPageType(self, pageType):
        if pageType == "BoxScore":
            return BasketballReferenceScrapeStatusSchema.boxscore_scrapedate
        elif pageType == "PlayByPlay":
            return BasketballReferenceScrapeStatusSchema.play_by_play_scrapedate
        elif pageType == "ShotChart":
            return BasketballReferenceScrapeStatusSchema.shotchart_scrapedate
        else:
            raise ValueError("The pageType provided is not a valid pageType")


def main(argv):
    BSS = BasketballReferencePageScraper()
    if argv['run_all']:
        argv['playbyplay'] = True
        argv['boxscore'] = True
        argv['shotchart'] = True

    if argv['playbyplay']:
        BSS.process("PlayByPlay")
    if argv['boxscore']:
        BSS.process("BoxScore")
    if argv['shotchart']:
        BSS.process("ShotChart")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-ra', '--run-all', help='Will run all three page extractors (BoxScore, ShotChart, PlayByPlay)',
                        action="store_true", default=False)
    parser.add_argument('-bs', '--boxscore', help='Scrape all new boxscore links', action="store_true", default=False)
    parser.add_argument('-sc', '--shotchart', help='Scrape all new shotchart links', action="store_true", default=False)
    parser.add_argument('-pbp', '--playbyplay', help='Scrape all new playbyplay links', action="store_true",
                        default=False)
    results = vars(parser.parse_args())
    main(results)

