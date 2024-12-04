from datetime import datetime
from . import db

class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, nullable=True)
    standings = db.Column(db.String(200), nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class TeamStanding(db.Model):
    __tablename__ = 'team_standings'

    id = db.Column(db.Integer, primary_key=True)
    descriptions = db.Column(db.String, nullable=True)
    position = db.Column(db.Integer, nullable=False)
    matches = db.Column(db.Integer, nullable=False)
    wins = db.Column(db.Integer, nullable=False)
    scores_for = db.Column(db.Integer, nullable=False)
    scores_against = db.Column(db.Integer, nullable=False)
    losses = db.Column(db.Integer, nullable=False)
    draws = db.Column(db.Integer, nullable=False)
    points = db.Column(db.Integer, nullable=False)
    team_name = db.Column(db.String, nullable=False)
    team_slug = db.Column(db.String, nullable=False)
    team_short_name = db.Column(db.String, nullable=True)
    team_gender = db.Column(db.String, nullable=False)
    team_sport_name = db.Column(db.String, nullable=False)
    team_sport_slug = db.Column(db.String, nullable=False)
    team_sport_id = db.Column(db.Integer, nullable=False)
    team_user_count = db.Column(db.Integer, nullable=False)
    team_name_code = db.Column(db.String, nullable=True)
    team_disabled = db.Column(db.Boolean, nullable=False)
    team_national = db.Column(db.Boolean, nullable=False)
    team_type = db.Column(db.Integer, nullable=False)
    team_team_colors_primary = db.Column(db.String, nullable=True)
    team_team_colors_secondary = db.Column(db.String, nullable=True)
    team_team_colors_text = db.Column(db.String, nullable=True)
    promotion_text = db.Column(db.String, nullable=True)
    promotion_id = db.Column(db.Integer, nullable=True)
    unique_tournament_id = db.Column(db.Integer, nullable=False)
    season_id = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)


class UniqueTournamentSeason(db.Model):
    __tablename__ = 'unique_tournament_seasons'
    id = db.Column(db.Integer, primary_key=True)
    season_id = db.Column(db.Integer, nullable=False)
    unique_tournament_id = db.Column(db.Integer, nullable=False)
    season_name = db.Column(db.String, nullable=False)
    season_start_date = db.Column(db.String, nullable=False)

    


class CompetitionStanding(db.Model):
    __tablename__ = 'competition_standings'

    id = db.Column(db.Integer, primary_key=True)
    total_teams = db.Column(db.Integer, nullable=False)
    year = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    row_name = db.Column(db.String, nullable=True)
    ranking = db.Column(db.Integer, nullable=False)
    points = db.Column(db.Integer, nullable=False)
    comp_id = db.Column(db.Integer, nullable=False)
    ranking_class = db.Column(db.String, nullable=True)
    unique_tournament_name = db.Column(db.String, nullable=False)
    unique_tournament_slug = db.Column(db.String, nullable=False)
    unique_tournament_primary_color = db.Column(db.String, nullable=True)
    unique_tournament_secondary_color = db.Column(db.String, nullable=True)
    unique_tournament_category_name = db.Column(db.String, nullable=True)
    unique_tournament_category_slug = db.Column(db.String, nullable=True)
    unique_tournament_category_sport_name = db.Column(db.String, nullable=True)
    unique_tournament_category_sport_slug = db.Column(db.String, nullable=True)
    unique_tournament_category_sport_id = db.Column(db.Integer, nullable=True)
    unique_tournament_category_id = db.Column(db.Integer, nullable=True)
    unique_tournament_category_flag = db.Column(db.String, nullable=True)
    unique_tournament_category_alpha2 = db.Column(db.String, nullable=True)
    unique_tournament_user_count = db.Column(db.Integer, nullable=True)
    unique_tournament_id = db.Column(db.Integer, nullable=True)
    country_alpha2 = db.Column(db.String, nullable=False)
    country_name = db.Column(db.String, nullable=False)
    season_id = db.Column(db.Integer, nullable=True)




class CompetitionList(db.Model):
    __tablename__ = 'top_competitions'  # Name of the table

    id = db.Column(db.Integer, primary_key=True)
    total_teams = db.Column(db.Integer, nullable=True)
    year = db.Column(db.String, nullable=True)
    type = db.Column(db.String, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    points = db.Column(db.Integer, nullable=True)
    ranking_class = db.Column(db.String, nullable=True)
    uniquetournament_name = db.Column(db.String, nullable=True)
    uniquetournament_slug = db.Column(db.String, nullable=True)
    uniquetournament_primary_color_hex = db.Column(db.String, nullable=True)
    uniquetournament_secondary_color_hex = db.Column(db.String, nullable=True)
    uniquetournament_category_name = db.Column(db.String, nullable=True)
    uniquetournament_category_slug = db.Column(db.String, nullable=True)
    uniquetournament_category_sport_name = db.Column(db.String, nullable=True)
    uniquetournament_category_sport_slug = db.Column(db.String, nullable=True)
    uniquetournament_category_sport_id = db.Column(db.Integer, nullable=True)
    uniquetournament_category_id = db.Column(db.Integer, nullable=True)
    uniquetournament_category_flag = db.Column(db.String, nullable=True)
    uniquetournament_category_alpha2 = db.Column(db.String, nullable=True)
    uniquetournament_usercount = db.Column(db.Integer, nullable=True)
    uniquetournament_id = db.Column(db.Integer, nullable=True)
    uniquetournament_displayinversehomeawayteams = db.Column(db.Boolean, nullable=True, default=False)
    country_alpha2 = db.Column(db.String, nullable=True)
    country_name = db.Column(db.String, nullable=True)
