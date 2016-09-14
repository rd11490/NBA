__author__ = 'Ryan'
"""
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
"""
class BasketballReferenceBoxScoreGameScoresSchema(object):

    gameid = "gameid"
    teamid = "teamid"
    q1 = "q1"
    q2 = "q2"
    q3 = "q3"
    q4 = "q4"
    overtime = "overtime"
    total = "total"
    num_overtime = "num_overtime"
    hometeam = "hometeam"
    

    @staticmethod
    def toHeader():
        return ['gameid',
                "teamid",
                "q1",
                "q2",
                "q3",
                "q4",
                "overtime",
                "total",
                "num_overtime",
                "hometeam"]