import requests
import pandas as pd
from app import db
from app.models import UniqueTournamentSeason  # Assuming you have a model for this
from app.models import CompetitionStanding,CompetitionList  # Assuming you have a model for this


def fetch_unique_tournaments_seasons_sofaSport(unique_tournament_id_list):
    results = []
    # __tablename__ = 'competition_standings'
    i=0
    # Iterate through each unique tournament ID in the list
    for unique_tournament_id in unique_tournament_id_list:
        print('unique_tournament_id',unique_tournament_id)
        try:
            print(f'Fetching data for unique_tournament_id: {unique_tournament_id}')
            url = "https://sofasport.p.rapidapi.com/v1/unique-tournaments/seasons"
            querystring = {"unique_tournament_id": unique_tournament_id}
            headers = {
                "X-RapidAPI-Key": "01a794702emshc130a98a05a2c7cp1e921fjsnbdba9347fe99",
                "X-RapidAPI-Host": "sofasport.p.rapidapi.com"
            }

            response = requests.get(url, headers=headers, params=querystring)
            print(f'API Response Status Code: {response.status_code}')
            
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                data = response.json()
                normalized_data = pd.json_normalize(data['data'])  # Flatten JSON response
                normalized_data['unique_tournament_id'] = unique_tournament_id  # Add the tournament ID to the data
                
                normalized_data.columns = [col.replace('.', '_') for col in normalized_data.columns]

                integer_columns = normalized_data.select_dtypes(include='int').columns
                print(f'Normalized Data for {unique_tournament_id}:', normalized_data)
                integer_columns = integer_columns.tolist()
            
                for col in integer_columns:   
                    normalized_data[col] = pd.to_numeric(normalized_data[col], errors='coerce').fillna(0).astype(int)  # Ensure wins is numeric
                
                # Create list to hold the database entries
              
                
                # Loop through the normalized data and add each entry to the session
                for record in normalized_data.to_dict(orient='records'):
               
                    new_entry = UniqueTournamentSeason(
                        season_id = record.get('id'),
                        unique_tournament_id=unique_tournament_id,
                        season_name=record.get('name'),
                        season_start_date=record.get('year')
                    )
                  
                
                # Add entries to the session
                    db.session.add(new_entry)
                db.session.commit()
                print(f'Added {new_entry} new entries for unique_tournament_id {unique_tournament_id}')
            else:
                print(f"Error fetching data for unique_tournament_id {unique_tournament_id}, status code: {response.status_code}")
                results.append({"unique_tournament_id": unique_tournament_id, "status": "failed", "error": f"Status code: {response.status_code}"})
        
        except Exception as e:
            print(f"Exception occurred while fetching data for unique_tournament_id {unique_tournament_id}: {e}")
            results.append({"unique_tournament_id": unique_tournament_id, "status": "failed", "error": str(e)})
    
    return results

def fetch_competitions(seasons_id_list, unique_tournament_id_list):
    results = []
    i = 0
    for unique_tournament_id in unique_tournament_id_list:
        try:
            url = "https://sofasport.p.rapidapi.com/v1/seasons/standings"
            querystring = {
                "seasons_id": seasons_id_list[i],
                "standing_type": "total",
                "unique_tournament_id": unique_tournament_id
            }
            headers = {
                "X-RapidAPI-Key": "01a794702emshc130a98a05a2c7cp1e921fjsnbdba9347fe99",
                "X-RapidAPI-Host": "sofasport.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers, params=querystring)
            data = response.json()

            # Process competition standings data
            df = pd.json_normalize(data['data'][0]['rows'])
            df.columns = [col.replace('.', '_') for col in df.columns]  # Replace dot with underscore for valid column names
            print('df.columns',df.columns)
            print('df',df)
            # Ensure numeric values are correctly formatted
            integer_columns = df.select_dtypes(include='int').columns
            integer_columns = integer_columns.tolist()
            for col in integer_columns:
                df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)

            # Handle string columns (if any)
            string_columns = df.select_dtypes(include='object').columns
            for col in string_columns:
                df[col] = df[col].fillna('')  # Replace NaN with empty strings
                df[col] = df[col].astype(str)  # Ensure all entries are strings

            standings = df.to_dict(orient='records')
            
            # Save the competition data to the database
            for record in standings:
             
                new_entry = CompetitionStanding(
                    total_teams=record.get('totalTeams'),
                    year=record.get('year'),
                    type=record.get('type'),
                    row_name=record.get('rowName'),
                    ranking=record.get('ranking'),
                    points=record.get('points'),
                    comp_id=record.get('id'),
                    ranking_class=record.get('rankingClass'),
                    unique_tournament_name=record.get('uniqueTournament_name'),
                    unique_tournament_slug=record.get('uniqueTournament_slug'),
                    unique_tournament_primary_color=record.get('uniqueTournament_primaryColorHex'),
                    unique_tournament_secondary_color=record.get('uniqueTournament_secondaryColorHex'),
                    unique_tournament_category_name=record.get('uniqueTournament_category_name'),
                    unique_tournament_category_slug=record.get('uniqueTournament_category_slug'),
                    unique_tournament_category_sport_name=record.get('uniqueTournament_category_sport_name'),
                    unique_tournament_category_sport_slug=record.get('uniqueTournament_category_sport_slug'),
                    unique_tournament_category_sport_id=record.get('uniqueTournament_category_sport_id'),
                    unique_tournament_category_id=record.get('uniqueTournament_category_id'),
                    unique_tournament_category_flag=record.get('uniqueTournament_category_flag'),
                    unique_tournament_category_alpha2=record.get('uniqueTournament_category_alpha2'),
                    unique_tournament_user_count=record.get('uniqueTournament_userCount'),
                    unique_tournament_id=record.get('uniqueTournament_id'),
                    country_alpha2=record.get('country_alpha2'),
                    country_name=record.get('country_name'),
                    season_id=seasons_id_list[i]
                )
              

                

                db.session.add(new_entry)

            db.session.commit()
            results.append({"unique_tournament_id": unique_tournament_id, "standings": standings})
        except Exception as e:
            print(f"Error fetching data for unique_tournament_id {unique_tournament_id}: {e}")
            results.append({"unique_tournament_id": unique_tournament_id, "error": str(e)})
        i += 1

    return results



def fetch_top_competitions(url_csv):
    df = pd.read_csv(url_csv)
    print('df----Z',df)
    results = []
    i = 0
    
    try:
        # Ensure numeric values are correctly formatted
        top_competitions = df.to_dict(orient='records')
        # Save the competition data to the database
        for record in top_competitions:
        
            new_entry = CompetitionList(
                total_teams = record.get('total_teams'),
                year = record.get('year'),
                type = record.get('type'),
                ranking = record.get('ranking'),
                points = record.get('points'),
                ranking_class = record.get('ranking_class'),
                uniquetournament_name = record.get('uniquetournament_name'),
                uniquetournament_slug = record.get('uniquetournament_slug'),
                uniquetournament_primary_color_hex = record.get('uniquetournament_primary_color_hex'),
                uniquetournament_secondary_color_hex = record.get('uniquetournament_secondary_color_hex'),
                uniquetournament_category_name = record.get('uniquetournament_category_name'),
                uniquetournament_category_slug = record.get('uniquetournament_category_slug'),
                uniquetournament_category_sport_name = record.get('uniquetournament_category_sport_name'),
                uniquetournament_category_sport_slug = record.get('uniquetournament_category_sport_slug'),
                uniquetournament_category_sport_id = record.get('uniquetournament_category_sport_id'),
                uniquetournament_category_id = record.get('uniquetournament_category_id'),
                uniquetournament_category_flag = record.get('uniquetournament_category_flag'),
                uniquetournament_category_alpha2 = record.get('uniquetournament_category_alpha2'),
                uniquetournament_usercount = record.get('uniquetournament_usercount'),
                uniquetournament_id = record.get('uniquetournament_id'),
                country_alpha2 = record.get('country_alpha2'),
                country_name = record.get('country_name'),
            )
            db.session.add(new_entry)
        db.session.commit()
        results.append({"unique_tournament_id": 'csv', "top_competitions": top_competitions})
    except Exception as e:
        print(f"Error fetching data for unique_tournament_id {'csv'}: {e}")
        results.append({"unique_tournament_id": 'csv', "error": str(e)})
    i += 1

    return results
