import unittest

import pandas as pd

from BasketballReferenceBoxScoreFourFactorsSchema import BasketballReferenceBoxScoreFourFactorsSchema
from CassandraQueryBuilder import *
from ScraperUtils import frameToList
from CassandraTables import *

__author__ = 'Ryan'


class testCassandraQueryBuilder(unittest.TestCase):
    def testInsertQueryBuilder(self):
        cols = ['home', 'away', 'date']
        testRes = CassandraQueryBuilder.insertQueryBuilder(
            CassandraTables.BASKETBALLREFERENCE_GAME_LINKS_TABLE, cols, [5, 6.5, "Test data"])
        self.assertEquals(
            "INSERT INTO basketball_reference_games_links_table (home, away, date) VALUES (5, 6.5, $$Test data$$)",
            testRes)

    def testSelectQueryBuilder(self):
        cols = None
        cond = None
        testRes = CassandraQueryBuilder.selectQueryBuilder(
            CassandraTables.BASKETBALLREFERENCE_GAME_LINKS_TABLE, cols, cond)
        self.assertEquals(
            "SELECT * FROM basketball_reference_games_links_table ALLOW FILTERING",
            testRes)

    def testCheckRowInTable(self):
        testRes = CassandraQueryBuilder.checkRowInTable(
            CassandraTables.BASKETBALLREFERENCE_GAME_LINKS_TABLE, [("gameid", "201605190BOS")])
        self.assertEquals(
            'SELECT COUNT(*) FROM basketball_reference_games_links_table WHERE gameid=\'201605190BOS\' ALLOW FILTERING',
            testRes)

    def testInClause(self):
        testRes = CassandraQueryBuilder.inClause("gameid", ["a", "b"])
        self.assertEquals(
            "gameid in ('a','b')",
            testRes)

    def testUpdateClause(self):
        testRes = CassandraQueryBuilder.updateQueryBuilder(CassandraTables.BASKETBALLREFERENCE_SCRAPE_STATUS_TABLE,
                                                           "scrapedate=today",
                                                           ["gameid=5"])
        self.assertEquals(
            "UPDATE basketball_reference_scrape_status_table SET scrapedate=today WHERE gameid=5",
            testRes)

    def testBatchClause(self):
        frame = pd.DataFrame()
        frame = frame.append(pd.Series(['gameid',
                                        "teamid",
                                        "pace",
                                        "effective_field_goal_percent",
                                        "turnover_percent",
                                        "offensive_rebound_percent",
                                        "freethrow_per_field_goal_attempt",
                                        "offensive_rating",
                                        "hometeam"]), ignore_index=True)
        frame = frame.append(pd.Series(['gameid2',
                                        "teamid2",
                                        "pace2",
                                        "effective_field_goal_percent2",
                                        "turnover_percent2",
                                        "offensive_rebound_percent2",
                                        "freethrow_per_field_goal_attempt2",
                                        "offensive_rating2",
                                        "hometeam2"]), ignore_index=True)

        testRes = CassandraQueryBuilder.insertBatch(CassandraTables.BASKETBALLREFERENCE_BOXSCORE_FOUR_FACTORS,
                                                    BasketballReferenceBoxScoreFourFactorsSchema.toHeader(),
                                                    frameToList(frame))

        self.assertEqual(testRes,
                         "BEGIN BATCH INSERT INTO basketball_reference_box_score_four_factors (gameid, teamid, pace, effective_field_goal_percent, turnover_percent, offensive_rebound_percent, freethrow_per_field_goal_attempt, offensive_rating, hometeam) VALUES ($$gameid$$, $$teamid$$, $$pace$$, $$effective_field_goal_percent$$, $$turnover_percent$$, $$offensive_rebound_percent$$, $$freethrow_per_field_goal_attempt$$, $$offensive_rating$$, $$hometeam$$) INSERT INTO basketball_reference_box_score_four_factors (gameid, teamid, pace, effective_field_goal_percent, turnover_percent, offensive_rebound_percent, freethrow_per_field_goal_attempt, offensive_rating, hometeam) VALUES ($$gameid2$$, $$teamid2$$, $$pace2$$, $$effective_field_goal_percent2$$, $$turnover_percent2$$, $$offensive_rebound_percent2$$, $$freethrow_per_field_goal_attempt2$$, $$offensive_rating2$$, $$hometeam2$$) APPLY BATCH")


if __name__ == '__main__':
    unittest.main()
