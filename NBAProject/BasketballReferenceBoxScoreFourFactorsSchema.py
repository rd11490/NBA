__author__ = 'Ryan'
"""
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
"""
class BasketballReferenceBoxScoreFourFactorsSchema(object):

    gameid = "gameid"
    teamid = "teamid"
    pace = "pace"
    effective_field_goal_percent = "effective_field_goal_percent"
    turnover_percent = "turnover_percent"
    offensive_rebound_percent = "offensive_rebound_percent"
    freethrow_per_field_goal_attempt = "freethrow_per_field_goal_attempt"
    offensive_rating = "offensive_rating"
    hometeam = "hometeam"

    @staticmethod
    def toHeader():
        return ['gameid',
                "teamid",
                "pace",
                "effective_field_goal_percent",
                "turnover_percent",
                "offensive_rebound_percent",
                "freethrow_per_field_goal_attempt",
                "offensive_rating",
                "hometeam"]