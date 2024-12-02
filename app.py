from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from apscheduler.schedulers.background import BackgroundScheduler
import requests
import datetime
import pandas as pd
from sqlalchemy import text


app = Flask(__name__)

# Configurations for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://miguelmagalhaes:yourpassword@db:5432/miguelmagalhaes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)
pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.width', None)  # Don't truncate the display width
pd.set_option('display.max_colwidth', None)  # Don't truncate column content

@app. route('/')
def index():
    txt='sdasdasa'
    for i in range(1,5) :
        txt += str(i)
    return render_template("index.html",**locals())

# Existing Data model
class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, nullable=True)
    standings = db.Column(db.String(200), nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)


# New TeamStanding model for the expanded schema
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
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

@app.before_first_request
def create_tables():
    db.create_all()


# Initialize the database and tables
with app.app_context():
    db.create_all()

# Function to get all tables
def get_tables():
    result = db.session.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"))
    tables = result.fetchall()
    return [table[0] for table in tables]

@app.route('/check-data', methods=['GET'])
def check_data():
    # Query the first 10 records from the TeamStanding table
    standings = TeamStanding.query.limit(10).all()

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


@app.route('/test-fetch-standings', methods=['GET'])
def test_fetch_standings():
    seasons_id_list = [37036]  # Example team ID (replace with any valid team ID)
    unique_tournament_id_list = [17]  # Example team ID (replace with any valid team ID)
    return fetch_teams_season_standings(seasons_id_list,unique_tournament_id_list)


@app.route('/tables', methods=['GET'])
def show_tables():
    tables = get_tables()
    return {'tables': tables}

# Function to fetch team season standings from the SofaSport API
def fetch_teams_season_standings(seasons_id_list,unique_tournament_id_list):
    results = []
    __tablename__ = 'team_standings'
    i=0
    # querystring = {"seasons_id":"37036","standing_type":"total","unique_tournament_id":"17"}
    print('seasons_id_list------>',seasons_id_list)
    unique_tournament_id_list
    print('unique_tournament_id_list------>',unique_tournament_id_list)

    for unique_tournament_id in unique_tournament_id_list:
        url =  "https://sofasport.p.rapidapi.com/v1/seasons/standings"
        
        # querystring = {"team_id": team_id}
        querystring = {"seasons_id":seasons_id_list[i],"standing_type":"total","unique_tournament_id":unique_tournament_id}
        
        headers = {
            "X-RapidAPI-Key": "01a794702emshc130a98a05a2c7cp1e921fjsnbdba9347fe99",
            "X-RapidAPI-Host": "sofasport.p.rapidapi.com"
        }
        team_id = 0
        try:
            response = requests.get(url, headers=headers, params=querystring)
            response.raise_for_status()
            data = response.json()

            # Normalize data for easy handling (optional)
            df = pd.json_normalize(data['data'][0]['rows'])

          

            df.columns = [col.replace('.', '_') for col in df.columns]
    
            # Remove the null character (\0) from column names
            # df.columns = df.columns.str.replace('__0', '', regex=False)
            print('________DF_______',df.columns)
            integer_columns = df.select_dtypes(include='int').columns


            # Convert integer_columns to a list if it's an Index
            integer_columns = integer_columns.tolist()


            integer_columns.append('promotion_id')
            # Replace NaN values with 0 in integer columns


            # df[integer_columns] = df[integer_columns].fillna(0)
            
            for col in integer_columns:   
                df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)  # Ensure wins is numeric
            # print('df_team_id',df.team_id)
                
             #Handle string columns
            string_columns = df.select_dtypes(include='object').columns
            string_columns = string_columns.tolist()

            # Debug: Print the list of string columns
            print('string_columns', string_columns)

            # Clean string columns: Ensure non-null strings or replace invalid entries
            for col in string_columns:
                df[col] = df[col].fillna('')  # Replace NaN with empty strings
                df[col] = df[col].astype(str)  # Ensure all entries are strings

            standings = df.to_dict(orient='records')
            # print('standings------>',standings)
            # print('standings',standings)

            # Save the data to the TeamStanding table
            for record in standings:
                # print('raw_record---->',raw_record)
                # print('record in standings ',record)
                # record = {key.replace('__0', ''): value for key, value in raw_record.items()}
             

                team_id = record.get('team_id')  # Adjust this based on your actual data structure
                # print('team_id-->',team_id,'record in standings ',record)
                if team_id is None or team_id == 0:
                    continue  # Skip this record as it has no team_id
                # print('record in standings ',record)
                # df = pd.json_normalize(data['data'][0]['rows'])
                new_entry = TeamStanding(
                    descriptions=record.get('descriptions'),
                    position=record.get('position'),
                    matches=record.get('matches'),
                    wins=record.get('wins'),
                    scores_for=record.get('scoresFor'),
                    scores_against=record.get('scoresAgainst'),
                    losses=record.get('losses'),
                    draws=record.get('draws'),
                    points=record.get('points'),
                    team_name=record.get('team_name'),
                    team_slug=record.get('team_slug'),
                    team_short_name=record.get('team_shortName'),
                    team_gender=record.get('team_gender'),
                    team_sport_name=record.get('team_sport_name'),
                    team_sport_slug=record.get('team_sport_slug'),
                    team_sport_id=record.get('team_sport_id'),
                    team_user_count=record.get('team_userCount'),
                    team_name_code=record.get('team_nameCode'),
                    team_disabled=record.get('team.disabled') == "True",
                    team_national=record.get('team_national') == "True",
                    team_type=record.get('team_type'),
                    team_team_colors_primary=record.get('team_teamColors_primary'),
                    team_team_colors_secondary=record.get('team_teamColors_secondary'),
                    team_team_colors_text=record.get('team_teamColors_text'),
                    promotion_text=record.get('promotion_text'),
                    promotion_id=record.get('promotion_id'),
                    unique_tournament_id=unique_tournament_id,
                    season_id=seasons_id_list[i]
                )
          
                db.session.add(new_entry)
         
            db.session.commit()
            print('oookkk')
            results.append({"team_id": team_id, "standings": standings})
        except Exception as e:
            print(f"Error fetching data for team_id {team_id}: {e}")
            print()
            results.append({"team_id": team_id, "error": str(e)})
        i+=1

    return results


# Scheduler to run the fetch_teams_season_standings function daily
scheduler = BackgroundScheduler()
scheduler.add_job(lambda: fetch_teams_season_standings([37036],[17]), 'interval', days=1)
scheduler.start()


# Route to fetch and display stored standings from the new table
@app.route('/standings', methods=['GET'])
def get_standings():
    all_standings = TeamStanding.query.all()
    return jsonify([
        {
            'id': s.id,
            'position': s.position,
            'matches': s.matches,
            'wins': s.wins,
            'team_name': s.team_name,
            'points': s.points
        }
        for s in all_standings
    ])


# Route to trigger a manual standings fetch
@app.route('/fetch-standings', methods=['POST'])
def manual_fetch_standings():
    unique_tournament_id_list = request.json.get('unique_tournament_id_list', [])
    seasons_id_list = request.json.get('seasons_id_list', [])
    if not unique_tournament_id_list:
        return jsonify({"error": "No unique_tournament_id_list IDs provided"}), 400
    if not seasons_id_list:
        return jsonify({"error": "No team seasons_id_list provided"}), 400

    results = fetch_teams_season_standings(seasons_id_list,unique_tournament_id_list)
    return jsonify({"message": "Manual fetch completed", "results": results})


if __name__ == '__main__':
    app.run(debug=True)
