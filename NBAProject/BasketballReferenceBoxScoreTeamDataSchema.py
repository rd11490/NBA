__author__ = 'Ryan'
"""
CREATE TABLE nba.basketball_reference_box_score_player_data (
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
"""
class BasketballReferenceBoxScoreTeamDataSchema(object):

    gameid = "gameid"
    teamid = "teamid"
    minutes_played = "minutes_played"
    field_goals = "field_goals"
    field_goal_attempts = "field_goal_attempts"
    field_goal_percent = "field_goal_percent"
    three_point = "three_point"
    three_point_attempts = "three_point_attempts"
    three_point_percent = "three_point_percent"
    free_throws = "free_throws"
    free_throw_attempts = "free_throw_attempts"
    free_throw_percent = "free_throw_percent"
    offensive_rebounds = "offensive_rebounds"
    defensive_rebounds = "defensive_rebounds"
    total_rebounds = "total_rebounds"
    assists = "assists"
    steals = "steals"
    blocks = "blocks"
    turnovers = "turnovers"
    personal_fouls = "personal_fouls"
    points = "points"
    plus_minus = "plus_minus"
    true_shooting_percent = "true_shooting_percent"
    effective_field_goal_percent = "effective_field_goal_percent"
    three_point_attempt_rate = "three_point_attempt_rate"
    free_throw_rate = "free_throw_rate"
    offensive_rebound_percent = "offensive_rebound_percent"
    defensive_rebound_percent = "defensive_rebound_percent"
    total_rebound_percent = "total_rebound_percent"
    assist_percent = "assist_percent"
    steal_percent = "steal_percent"
    block_percent = "block_percent"
    turnover_percent = "turnover_percent"
    usage_percent = "usage_percent"
    offensive_rating = "offensive_rating"
    defensive_rating = "defensive_rating"
    hometeam = "hometeam"
    

    @staticmethod
    def toHeader():
        return ['gameid',
                "teamid",
                "minutes_played",
                "field_goals",
                "field_goal_attempts",
                "field_goal_percent",
                "three_point",
                "three_point_attempts",
                "three_point_percent",
                "free_throws",
                "free_throw_attempts",
                "free_throw_percent",
                "offensive_rebounds",
                "defensive_rebounds",
                "total_rebounds",
                "assists",
                "steals",
                "blocks",
                "turnovers",
                "personal_fouls",
                "points",
                "plus_minus",
                "true_shooting_percent",
                "effective_field_goal_percent",
                "three_point_attempt_rate",
                "free_throw_rate",
                "offensive_rebound_percent",
                "defensive_rebound_percent",
                "total_rebound_percent",
                "assist_percent",
                "steal_percent",
                "block_percent",
                "turnover_percent",
                "usage_percent",
                "offensive_rating",
                "defensive_rating",
                "hometeam"]