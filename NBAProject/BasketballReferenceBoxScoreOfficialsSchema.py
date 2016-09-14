__author__ = 'Ryan'
"""
CREATE TABLE nba.basketball_reference_box_score_officials (
gameid text,
refid text,
name text,
PRIMARY KEY(gameid, refid)
);
"""
class BasketballReferenceBoxScoreOfficialsSchema(object):

    gameid = "gameid"
    refid = "refid"
    name = "name"


    @staticmethod
    def toHeader():
        return ['gameid',
                "refid",
                "name"]