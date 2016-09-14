__author__ = 'Ryan'
"""
CREATE TABLE nba.basketball_reference_box_score_inactives (
gameid text,
teamid float,
playerid text,
PRIMARY KEY(gameid, playerid)
);
"""
class BasketballReferenceBoxScoreInactivesSchema(object):

    gameid = "gameid"
    teamid = "teamid"
    playerid = "playerid"


    @staticmethod
    def toHeader():
        return ['gameid',
                "teamid",
                "playerid"]