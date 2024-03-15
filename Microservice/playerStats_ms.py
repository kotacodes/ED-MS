import os
import csv
import io
from flask import Flask, request, Response, make_response
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:8000"}})  # only accept requests from nba-stat cliet
db_uri = os.getenv("MONGO_URI")
client = MongoClient(db_uri)
nba_db = client["nba_db"]
game_stats = nba_db.game_stats

def generate_stats_file(json_player_stats):
    """
    Generates the player_stats csv file.
    """
    
    file_name = "player_stats.csv"

    # write stats from json to csv
    with open(file_name, 'w', newline='') as csv_file:
        column_names = list(json_player_stats[0].keys())
        csv_writer = csv.DictWriter(csv_file, fieldnames=column_names)
        csv_writer.writeheader()
        csv_writer.writerows(json_player_stats)

    return file_name

@app.route('/download-game-stats', methods=['GET'])
def download_game_stats():
    """
    Handles the request to download player stats. Calls generate_stats_file() and
    return the generated csv file in the response.
    """
    
    player_id = request.args.get('player-id')
    final_output = []

    # get game stats for player
    for game in game_stats.find({'player_id': player_id}, {'_id': False}):
        final_output.append(game)

    file_name = generate_stats_file(final_output)

    # open stats file and return it in response
    with open(file_name, 'rb') as csv_file:
        response = make_response(csv_file.read())
        response.headers['Content-Disposition'] = f'attachment; filename={file_name}'
        response.mimetype = 'text/csv'

    return response

if __name__ == '__main__':
    app.run(debug=True, port=5000)