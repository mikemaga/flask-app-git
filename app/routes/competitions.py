from flask import Blueprint, jsonify, request
from app.services.fetch_competitions import fetch_competitions,fetch_unique_tournaments_seasons_sofaSport, fetch_top_competitions  # Assuming you have this function
from app.models import UniqueTournamentSeason, CompetitionList # Assuming you have a Competition model
from app import db

competitions_bp = Blueprint('competitions', __name__)



@competitions_bp.route('/top_competitions', methods=['GET'])
def get_top_competitions():
    # Fetch the first 10 competition standings from the database
    top = CompetitionList.query.limit(10).all()

    # Log the fetched top
    print("Fetched competition top:", top)


    # Return the result as a JSON response
    return jsonify([{
        'id': s.id,
        'total_teams': s.total_teams,
        'year': s.year,
        'type': s.type,
        'ranking': s.ranking,
        'points': s.points,
        'ranking_class': s.ranking_class,
        'uniquetournament_name': s.uniquetournament_name,
        'uniquetournament_slug': s.uniquetournament_slug,
        'uniquetournament_primary_color_hex': s.uniquetournament_primary_color_hex,
        'uniquetournament_secondary_color_hex': s.uniquetournament_secondary_color_hex,
        'uniquetournament_category_name': s.uniquetournament_category_name,
        'uniquetournament_category_slug': s.uniquetournament_category_slug,
        'uniquetournament_category_sport_name': s.uniquetournament_category_sport_name,
        'uniquetournament_category_sport_slug': s.uniquetournament_category_sport_slug,
        'uniquetournament_category_sport_id': s.uniquetournament_category_sport_id,
        'uniquetournament_category_id': s.uniquetournament_category_id,
        'uniquetournament_category_flag': s.uniquetournament_category_flag,
        'uniquetournament_category_alpha2': s.uniquetournament_category_alpha2,
        'uniquetournament_usercount': s.uniquetournament_usercount,
        'uniquetournament_id': s.uniquetournament_id,
        'uniquetournament_displayinversehomeawayteams': s.uniquetournament_displayinversehomeawayteams,
        'country_alpha2': s.country_alpha2,
        'country_name': s.country_name,
    } for s in top])




@competitions_bp.route('/competitions', methods=['GET'])
def get_competitions():
    # Fetch the first 10 competitions from the database
    competitions = UniqueTournamentSeason.query.limit(10).all()
    print("Fetched competitions:", competitions)

    # Return the result as a JSON response
    return jsonify([{
        'id': c.id,
        'season_id': c.season_id,
        'unique_tournament_id':c.unique_tournament_id,
        'competition_name': c.season_name,
        'start_date': c.season_start_date,
    } for c in competitions])

@competitions_bp.route('/fetch-competitions', methods=['POST'])
def manual_fetch_competitions():
    # Get the JSON data from the request
    data = request.get_json()  # Use get_json to parse the incoming JSON
    
    # Check if data is None (i.e., no JSON was sent)
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    unique_tournament_id_list = data.get('unique_tournament_id_list', [])
    seasons_id_list = data.get('seasons_id_list', [])
    
    if not unique_tournament_id_list:
        return jsonify({"error": "Invalid input"}), 400

    # Call your function that fetches competition data (make sure fetch_competitions is defined)
    results = fetch_competitions(seasons_id_list,unique_tournament_id_list)
    
    return jsonify({"message": "Fetch completed", "results": results})




@competitions_bp.route('/fetch-top-competitions', methods=['POST'])
def manual_fetch_top_competitions():
    # Get the JSON data from the request
    data = request.get_json()  # Use get_json to parse the incoming JSON
    
    # Check if data is None (i.e., no JSON was sent)
    if not data:
        return jsonify({"error": "Invalid input"}), 400
    url = '/Users/miguelmagalhaes/Documents/scoreplay/flask_api_server/initaldb/top_competitions.csv'

    # Call your function that fetches competition data (make sure fetch_competitions is defined)
    results = fetch_top_competitions(url)
    
    return jsonify({"message": "Fetch completed", "results": results})




@competitions_bp.route('/fetch-seasons', methods=['POST'])
def manual_fetch_seasons():
    # Get the JSON data from the request
    data = request.get_json()  # Use get_json to parse the incoming JSON
    
    # Check if data is None (i.e., no JSON was sent)
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    unique_tournament_id_list = data.get('unique_tournament_id_list', [])
    if not unique_tournament_id_list:
        return jsonify({"error": "Invalid input"}), 400

    # Call your function that fetches competition data (make sure fetch_competitions is defined)
    results = fetch_unique_tournaments_seasons_sofaSport(unique_tournament_id_list)
    
    return jsonify({"message": "Fetch completed", "results": results})
