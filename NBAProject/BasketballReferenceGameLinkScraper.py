import argparse
from bs4 import BeautifulSoup
from cassandra.cluster import Cluster
import requests
from BasketballReferenceScrapeStatusSchema import BasketballReferenceScrapeStatusSchema
from BasketballRefereneceGameLinksSchema import BasketballRefereneceGameLinksSchema

from CassandraQueryBuilder import CassandraQueryBuilder
from CassandraTables import CassandraTables
from Links import Links
from ScraperUtils import *


__author__ = 'ryan'

"""
CREATE TABLE nba.basketball_reference_games_links_table (
gameid text,
date text,
time text,
awayid float,
awayscore float,
homeid float,
homescore float,
boxscorelink text,
year int,
scrapedate text,
PRIMARY KEY ((year), gameid, date, time, awayid, awayscore, homeid, homescore)
);

CREATE TABLE nba.basketball_reference_scrape_status_table (
gameid text,
link_scrapedate text,
boxscore_scrapedate text,
play_by_play_scrapedate text,
shotchart_scrapedate text,
boxscore_parsedate text,
play_by_play_parsedate text,
shotchart_parsedate text,
PRIMARY KEY (gameid)
);
"""


class BasketballReferenceGameLinkScraper:
    """

    :param year:
    """

    def __init__(self):
        self.cluster = Cluster()
        self.session = self.cluster.connect(CassandraTables.KEYSPACE_NBA)
        self.scrapeDate = str(datetime.today())
        self.EMPTY_CELL = ""


    def scrapeYear(self, year):
        """
        Scrapes all links from the current year and adds them to the table

        """
        r = requests.get(Links.getBasketballReferenceLeagueYearGames(year))
        soup = BeautifulSoup(r.content, "html.parser")
        table = soup.find_all('table', id='games')[0]
        rows = table.find_all('tr', class_='')
        self.scrapeTable(rows)


    def scrapeNewLinks(self, year):
        r = requests.get(Links.getBasketballReferenceLeagueYearGames(year))
        soup = BeautifulSoup(r.content, "html.parser")
        table = soup.find_all('table', id='games')[0]
        rows = table.find_all('tr', class_='')
        gameIds = self.selectSource(BasketballReferenceScrapeStatusSchema.link_scrapedate)
        for r in rows:
            data = r.find_all('td')
            if data:
                if data[2].find_all('a', href=True):
                    if data[0]['csk'] in gameIds:
                        dataRow = self.scrapeRow(data, year)
                        if not self.rowInTable(CassandraTables.BASKETBALLREFERENCE_GAME_LINKS_TABLE, dataRow):
                            self.writeToLinkTable(dataRow)
                            self.updateTrackingTable(dataRow[0], self.scrapeDate)
                else:
                    self.updateTrackingTable(data[0]['csk'], "")


    def scrape_page(self, soup):
        table = soup.find_all('table', id='games')[0]
        rows = table.find_all('tr', class_='')
        self.scrapeTable(rows)

    def scrapeRow(self, data, year):
        return [data[0]['csk'],
                dateFormat(data[0].find_all('a', href=True)[0].text),
                data[1].text,
                convertNameToId(data[3]['csk'][:data[3]['csk'].find('.')]),
                int(data[4].text),
                convertNameToId(data[5]['csk'][:data[5]['csk'].find('.')]),
                int(data[6].text),
                Links.BASKETBALL_REFERENCE + data[2].find_all('a', href=True)[0]['href'],
                year,
                self.scrapeDate]


    def scrapeTable(self, rows):
        """
        Converts the current table into a row and adds each row to cassandraCore
        :param rows:
        """
        for r in rows:
            data = r.find_all('td')
            if data:
                if data[2].find_all('a', href=True):
                    dataRow = self.scrapeRow(data)
                    if not self.rowInTable(CassandraTables.BASKETBALLREFERENCE_GAME_LINKS_TABLE, dataRow):
                        self.writeToLinkTable(dataRow)
                        self.updateTrackingTable(dataRow[0], self.scrapeDate)
                else:
                    self.updateTrackingTable(data[0]['csk'], "")





    def rowInTable(self, table, dataRow):
        """
        checks to see if a row is already in the table
        SELECT count(*) FROM TABLE WHERE primary_keys = blah

        :param dataRow:
        """
        return self.session.execute(
            CassandraQueryBuilder.checkRowInTable(table, [(BasketballRefereneceGameLinksSchema.gameid, dataRow[0])]))

    def writeToLinkTable(self, dataRow):
        """
        writes a datarow to the basketball ref links table
        :param dataRow:
        """
        self.session.execute(
            CassandraQueryBuilder.insertInto(CassandraTables.BASKETBALLREFERENCE_GAME_LINKS_TABLE,
                                             BasketballRefereneceGameLinksSchema.toHeader(),
                                             dataRow))

    def updateTrackingTable(self, gameid, date):
        """
        writes a datarow to the basketball ref links table
        :param dataRow:
        """
        self.session.execute(
            CassandraQueryBuilder.insertInto(CassandraTables.BASKETBALLREFERENCE_SCRAPE_STATUS_TABLE,
                                             BasketballReferenceScrapeStatusSchema.toHeader(),
                                             [gameid,
                                              self.EMPTY_CELL,
                                              self.EMPTY_CELL,
                                              date,
                                              self.EMPTY_CELL,
                                              self.EMPTY_CELL,
                                              self.EMPTY_CELL,
                                              self.EMPTY_CELL]))

    def selectSource(self, column):
        source = self.session.execute(
            CassandraQueryBuilder.selectFrom(CassandraTables.BASKETBALLREFERENCE_SCRAPE_STATUS_TABLE,
                                             ['gameid'], [column + "=''"]))
        return [r.gameid for r in source.current_rows]

def main(argv):
    BSS = BasketballReferenceGameLinkScraper()
    if argv['scrape_new']:
        BSS.scrapeNewLinks(currentSeason())

    if len(argv['year'])>0:
        for y in argv['year']:
            BSS.scrapeYear(y)




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--scrape-new', help='Will scrape all new links for the current year',
                        action="store_true", default=False)
    parser.add_argument('-y', '--year', help='years to scrape', nargs='+', type=int)
    results = vars(parser.parse_args())
    main(results)