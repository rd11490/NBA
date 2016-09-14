import argparse
from datetime import datetime

from cassandra.cluster import Cluster
from bs4 import BeautifulSoup
import pandas as pd
from BasketballReferenceBoxScoreFourFactorsSchema import BasketballReferenceBoxScoreFourFactorsSchema

from BasketballReferenceBoxScoreGameScoresSchema import BasketballReferenceBoxScoreGameScoresSchema
from BasketballReferenceBoxScoreInactivesSchema import BasketballReferenceBoxScoreInactivesSchema
from BasketballReferenceBoxScoreOfficialsSchema import BasketballReferenceBoxScoreOfficialsSchema
from BasketballReferenceBoxScorePlayerDataSchema import BasketballReferenceBoxScorePlayerDataSchema
from BasketballReferenceBoxScoreTeamDataSchema import BasketballReferenceBoxScoreTeamDataSchema
from BasketballReferenceScrapeStatusSchema import BasketballReferenceScrapeStatusSchema
from CassandraQueryBuilder import CassandraQueryBuilder
from CassandraTables import CassandraTables
from ScraperUtils import rowToList, convertNameToId, URLtoID, isNumber, frameToList


__author__ = 'Ryan'

"""
CREATE TABLE nba.basketball_reference_box_score_teams_data (
gameid text,
teamid float,
minutes_played float,
field_goals float,
field_goal_attempts float,
field_goal_percent float,
three_point float,
three_point_attempts float,
three_point_percent float,
free_throws float,
free_throw_attempts float,
free_throw_percent float,
offensive_rebounds float,
defensive_rebounds float,
total_rebounds float,
assists float,
steals float,
blocks float,
turnovers float,
personal_fouls float,
points float,
plus_minus float,
true_shooting_percent float,
effective_field_goal_percent float,
three_point_attempt_rate float,
free_throw_rate float,
offensive_rebound_percent float,
defensive_rebound_percent float,
total_rebound_percent float,
assist_percent float,
steal_percent float,
block_percent float,
turnover_percent float,
usage_percent float,
offensive_rating float,
defensive_rating float,
hometeam boolean,
PRIMARY KEY(gameid, teamid)
);

CREATE TABLE nba.basketball_reference_box_score_player_data (
gameid text,
teamid float,
playerid text,
minutes_played float,
field_goals float,
field_goal_attempts float,
field_goal_percent float,
three_point float,
three_point_attempts float,
three_point_percent float,
free_throws float,
free_throw_attempts float,
free_throw_percent float,
offensive_rebounds float,
defensive_rebounds float,
total_rebounds float,
assists float,
steals float,
blocks float,
turnovers float,
personal_fouls float,
points float,
plus_minus float,
true_shooting_percent float,
effective_field_goal_percent float,
three_point_attempt_rate float,
free_throw_rate float,
offensive_rebound_percent float,
defensive_rebound_percent float,
total_rebound_percent float,
assist_percent float,
steal_percent float,
block_percent float,
turnover_percent float,
usage_percent float,
offensive_rating float,
defensive_rating float,
hometeam boolean,
PRIMARY KEY(gameid, teamid)
);

CREATE TABLE nba.basketball_reference_box_score_four_factors (
gameid text,
teamid float,
pace float,
effective_field_goal_percent float,
turnover_percent float,
offensive_rebound_percent float,
freethrow_per_field_goal_attempt float,
offensive_rating float,
hometeam boolean,
PRIMARY KEY(gameid, teamid)
);

CREATE TABLE nba.basketball_reference_box_score_game_scores (
gameid text,
teamid float,
q1 float,
q2 float,
q3 float,
q4 float,
overtime float,
total float,
num_overtime float,
hometeam boolean,
PRIMARY KEY (gameid, teamid)
);

CREATE TABLE nba.basketball_reference_box_score_inactives (
gameid text,
teamid float,
playerid text,
PRIMARY KEY(gameid, playerid)
);

CREATE TABLE nba.basketball_reference_box_score_officials (
gameid text,
refid text,
name text,
PRIMARY KEY(gameid, refid)
);

"""


class BasketballReferenceBoxScoreParser(object):
    def __init__(self):
        self.cluster = Cluster()
        self.session = self.cluster.connect(CassandraTables.KEYSPACE_NBA)
        self.scrapeDate = str(datetime.today())


    def process(self):
        gameids = self.selectSource(BasketballReferenceScrapeStatusSchema.boxscore_parsedate)
        boxscores = self.selectBoxScores(gameids)
        for bs in boxscores:
            soup = BeautifulSoup(bs.page)
            playerData, teamData = self.extractBoxScoreStats(soup)
            refData = self.extractRef(soup)
            scoreData = self.extractFinalScores(soup)
            fourFactors = self.extractFourFactors(soup)
            inactiveData = self.extractInactives(soup)

            self.writeTable(
                CassandraTables.BASKETBALLREFERENCE_BOXSCORE_TEAMS_DATA,
                BasketballReferenceBoxScoreTeamDataSchema.toHeader(),
                teamData)

            self.writeTable(
                CassandraTables.BASKETBALLREFERENCE_BOXSCORE_PLAYER_DATA,
                BasketballReferenceBoxScorePlayerDataSchema.toHeader(),
                playerData)

            self.writeTable(
                CassandraTables.BASKETBALLREFERENCE_BOXSCORE_OFFICIALS,
                BasketballReferenceBoxScoreOfficialsSchema.toHeader(),
                refData)

            self.writeTable(
                CassandraTables.BASKETBALLREFERENCE_BOXSCORE_GAME_SCORES,
                BasketballReferenceBoxScoreGameScoresSchema.toHeader(),
                scoreData)

            self.writeTable(
                CassandraTables.BASKETBALLREFERENCE_BOXSCORE_FOUR_FACTORS,
                BasketballReferenceBoxScoreFourFactorsSchema.toHeader(),
                fourFactors)

            self.writeTable(
                CassandraTables.BASKETBALLREFERENCE_BOXSCORE_INACTIVES,
                BasketballReferenceBoxScoreInactivesSchema.toHeader(),
                inactiveData)

            self.updateSourceTable(bs.gameid, BasketballReferenceScrapeStatusSchema.boxscore_parsedate)




    def extractBoxScoreStats(self, soup):
        tables = soup.find_all('table', class_="sortable  stats_table")
        Home = convertNameToId(tables[2]['id'][:tables[2]['id'].find('_')])
        Home_basic = self.getPlayerBoxScore_fromTable(tables[2])
        Home_advanced = self.getPlayerBoxScore_fromTable(tables[3])
        Home_basic = Home_basic.drop('H/A', 1)
        Home_advanced = Home_advanced.drop(['GameID', 'MP'], 1)
        Home_bscore = Home_basic.merge(Home_advanced, on='PlayerID')
        Home_bscore.loc[:, 'H/A'] = 1

        Home_team_bscore = Home_bscore[Home_bscore.PlayerID == 'Team Totals']  # pulls out team totals
        Home_bscore = Home_bscore[Home_bscore.PlayerID != 'Team Totals']  # removes team totals
        Home_team_bscore = Home_team_bscore.rename(columns={'PlayerID': 'TeamID'})
        Home_team_bscore['TeamID'] = Home
        Home_bscore.insert(1, 'TeamID', Home)

        Away = convertNameToId(tables[0]['id'][:tables[0]['id'].find('_')])
        Away_basic = self.getPlayerBoxScore_fromTable(tables[0])
        Away_advanced = self.getPlayerBoxScore_fromTable(tables[1])
        Away_basic = Away_basic.drop('H/A', 1)
        Away_advanced = Away_advanced.drop(['GameID', 'MP'], 1)
        Away_bscore = Away_basic.merge(Away_advanced, on='PlayerID')
        Away_bscore.loc[:, 'H/A'] = 0

        Away_team_bscore = Away_bscore[Away_bscore.PlayerID == 'Team Totals']  # pulls out team totals
        Away_bscore = Away_bscore[Away_bscore.PlayerID != 'Team Totals']  # removes team totals
        Away_team_bscore = Away_team_bscore.rename(columns={'PlayerID': 'TeamID'})
        Away_team_bscore['TeamID'] = Away
        Away_bscore.insert(1, 'TeamID', Away)

        Team_bscore = Home_team_bscore.append(Away_team_bscore, ignore_index=True)
        Player_bscore = Home_bscore.append(Away_bscore, ignore_index=True)

        return Player_bscore, Team_bscore

    def extractRef(self, soup):
        frame = pd.DataFrame()
        table = soup.find_all('table', class_='margin_top small_text')[0]
        row = table.find_all('tr')[0]
        row_data = row.find_all('a')
        for d in row_data:
            frame = frame.append(pd.Series([None, URLtoID(d['href']), d.text]), ignore_index=True)
        frame.columns = ['GameID', 'RefID', 'Name']
        return frame

    def extractFinalScores(self, soup):
        frame = pd.DataFrame()
        total_scores = soup.find_all('table', class_="nav_table stats_table")[0]
        header = total_scores.find_all('th', class_="align_right")
        num_OT = len(header) - 5
        header_lst = []
        for h in header:
            header_lst.append(h.text)
        header_lst_tmp = [header_lst[x] for x in [0, 1, 2, 3, -1]]
        header_lst = header_lst_tmp
        header_lst.insert(4, 'OT')
        header_lst.insert(6, '#OT')
        header_lst.insert(0, 'TeamID')
        header_lst.insert(0, 'GameID')  # gameID is added at the next level
        header_lst.append('H/A')

        rows = total_scores.find_all('tr')
        for i, r in enumerate(rows):
            data_row = rowToList(r)
            if data_row:
                if len(data_row) > 6:  # if there are multiple OTs, add up the points in OT need to add
                    OT_Points = sum(data_row[5:5 + num_OT])
                    while len(data_row) > 7:
                        data_row.pop(6)
                    data_row[5] = OT_Points
                    data_row[0] = convertNameToId(data_row[0])
                else:
                    data_row[0] = convertNameToId(data_row[0])
                    data_row.insert(5, 0)
                data_row.insert(0, None)
                data_row.append(num_OT)
                if i == 2:
                    data_row.append(0)
                elif i == 3:
                    data_row.append(1)
                frame = frame.append(pd.Series(data_row), ignore_index=True)
        frame.columns = header_lst
        return frame


    def extractFourFactors(self, soup):
        frame = pd.DataFrame()
        four_factors = soup.find_all('table', id="four_factors")[0]

        header = four_factors.find_all('th')
        header_lst = []
        for h in header:
            if h.has_attr('tip'):
                header_lst.append(h.text)
        header_lst[0] = 'TeamID'
        header_lst.insert(0, 'GameID')
        header_lst.append('H/A')

        rows = four_factors.find_all('tr')
        for i, r in enumerate(rows):
            data_row = rowToList(r)
            if data_row:
                data_row[0] = convertNameToId(data_row[0])
                data_row.insert(0, None)
                if i == 2:
                    data_row.append(0)
                elif i == 3:
                    data_row.append(1)
                frame = frame.append(pd.Series(data_row), ignore_index=True)
        frame.columns = header_lst
        return frame

    def extractInactives(self, soup):
        frame = pd.DataFrame()
        inactives = soup.find_all("table", _class="margin_top small_text")


    def getPlayerBoxScore_fromTable(self, table):
        frame = pd.DataFrame()
        header = table.find_all('th', class_="tooltip")
        header_lst = []
        for h in header:
            header_lst.append(h.text)

        header_lst[0] = 'PlayerID'
        header_lst.insert(0, 'GameID')
        header_lst.append('H/A')
        rows = table.find_all('tr')

        for i, r in enumerate(rows):
            data_row = self.playerRowToList(r)
            if data_row:
                data_row.insert(0, None)
                data_row.append(None)
                frame = frame.append(pd.Series(data_row), ignore_index=True)
        frame.columns = header_lst
        return frame

    def playerRowToList(self, row):
        data_row = []
        data = row.find_all('td')
        for d in data:
            link = d.find_all('a')
            if link:
                text = URLtoID(link[0].get('href'))
            else:
                text = d.text
            if isNumber(text):
                text = float(text)
            elif text == '':
                text = 0.0
            else:
                text = text.format('ascii')  # for pickling
            data_row.append(text)
        return data_row


    def writeTable(self, table, columns, data):
        self.session.execute(
            CassandraQueryBuilder.insertBatch(
                table,
                columns,
                frameToList(data)
            )
        )

    def updateSourceTable(self, gameId, column):
        self.session.execute(
            CassandraQueryBuilder.updateQueryBuilder(CassandraTables.BASKETBALLREFERENCE_SCRAPE_STATUS_TABLE,
                                                     "{0}=$${1}$$".format(column, self.scrapeDate),
                                                     ["gameid=\'{0}\'".format(gameId)]))

    def selectBoxScores(self, gameids):
        return self.session.execute(
            CassandraQueryBuilder.selectFrom(CassandraTables.BASKETBALLREFERENCE_PAGE_TEXT,
                                             ['gameid', 'page'],
                                             [CassandraQueryBuilder.inClause('gameid', gameids)]))

    def selectSource(self, column):
        source = self.session.execute(
            CassandraQueryBuilder.selectFrom(CassandraTables.BASKETBALLREFERENCE_SCRAPE_STATUS_TABLE,
                                             ['gameid'], [column + "=''"]))
        return [r.gameid for r in source.current_rows]


def main(argv):
    BSS = BasketballReferenceBoxScoreParser()
    BSS.process()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    results = vars(parser.parse_args())
    main(results)