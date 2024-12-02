from flask import Blueprint, jsonify, request
from app.services.fetch_standings import fetch_standings
from app.models import TeamStanding
from app.services.fetch_standings import fetch_standings,fetch_teams_season_standings
from app import db
import logging

standings_bp = Blueprint('standings', __name__)

@standings_bp.route('/standings', methods=['GET'])
def get_standings():
    standings = TeamStanding.query.limit(10).all()
    print("fetch_standings module loaded",standings)
    if not standings:
        return jsonify({"message": "No standings available"}), 404
    
    logging.info(f"Fetched {len(standings)} standings records")

    # Return the result as a JSON response
    return jsonify([{
        'id': s.id,
        'position': s.position,
        'matches': s.matches,
        'wins': s.wins,
        'team_name': s.team_name,
        'points': s.points,
        'descriptions': s.descriptions,
        'scores_for': s.scores_for,
        'scores_against': s.scores_against,
        'losses': s.losses,
        'draws': s.draws,
        'team_slug': s.team_slug,
        'team_short_name': s.team_short_name,
        'team_gender': s.team_gender,
        'team_sport_name': s.team_sport_name,
        'team_sport_slug': s.team_sport_slug,
        'team_sport_id': s.team_sport_id,
        'team_user_count': s.team_user_count,
        'team_name_code': s.team_name_code,
        'team_disabled': s.team_disabled,
        'team_national': s.team_national,
        'team_type': s.team_type,
        'team_team_colors_primary': s.team_team_colors_primary,
        'team_team_colors_secondary': s.team_team_colors_secondary,
        'team_team_colors_text': s.team_team_colors_text,
        'promotion_text': s.promotion_text,
        'promotion_id': s.promotion_id,
        'unique_tournament_id': s.unique_tournament_id,
        'season_id': s.season_id
    } for s in standings])

@standings_bp.route('/fetch-standings', methods=['POST'])
def manual_fetch_standings():
    # Get the JSON data from the request
    data = request.get_json()  # Use get_json to parse the incoming JSON
    
    # Check if data is None (i.e., no JSON was sent)
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    seasons_id_list = data.get('seasons_id_list', [])
    unique_tournament_id_list = data.get('unique_tournament_id_list', [])
    
    if not seasons_id_list or not unique_tournament_id_list:
        return jsonify({"error": "Invalid input"}), 400

    # Call your function that fetches standings (make sure fetch_standings is defined)
    results = fetch_teams_season_standings(seasons_id_list, unique_tournament_id_list)
    
    return jsonify({"message": "Fetch completed", "results": results})
