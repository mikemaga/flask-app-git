import requests
import pandas as pd
from app import db
from app.models import TeamStanding

def fetch_standings(seasons_id_list, unique_tournament_id_list):
    results = []
    i=0
    for unique_tournament_id in unique_tournament_id_list:
        try:
            url = "https://sofasport.p.rapidapi.com/v1/seasons/standings"
            querystring = {
                "seasons_id": seasons_id_list[0],
                "standing_type": "total",
                "unique_tournament_id": unique_tournament_id
            }
            headers = {
                "X-RapidAPI-Key": "01a794702emshc130a98a05a2c7cp1e921fjsnbdba9347fe99",
                "X-RapidAPI-Host": "sofasport.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers, params=querystring)
            data = response.json()

            # Process standings data
            df = pd.json_normalize(data['data'][0]['rows'])
            standings = df.to_dict(orient='records')

            # Save to database
            for record in standings:
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
        except Exception as e:
            results.append({"error": str(e)})
    i +=1
    return results



# Function to fetch team season standings from the SofaSport API
def fetch_teams_season_standings(seasons_id_list,unique_tournament_id_list):
    results = []
    __tablename__ = 'team_standings'
    i=0
    unique_tournament_id_list

    for unique_tournament_id in unique_tournament_id_list:
        url =  "https://sofasport.p.rapidapi.com/v1/seasons/standings"
        
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

            integer_columns = df.select_dtypes(include='int').columns
            integer_columns = integer_columns.tolist()
            integer_columns.append('promotion_id')
            
            for col in integer_columns:   
                df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)  # Ensure wins is numeric
                
             #Handle string columns
            string_columns = df.select_dtypes(include='object').columns
            string_columns = string_columns.tolist()

            # Debug: Print the list of string columns
            # print('string_columns', string_columns)

            # Clean string columns: Ensure non-null strings or replace invalid entries
            for col in string_columns:
                df[col] = df[col].fillna('')  # Replace NaN with empty strings
                df[col] = df[col].astype(str)  # Ensure all entries are strings

            standings = df.to_dict(orient='records')

            # Save the data to the TeamStanding table
            for record in standings:

                team_id = record.get('team_id')  # Adjust this based on your actual data structure
                if team_id is None or team_id == 0:
                    continue  # Skip this record as it has no team_id
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