from flask import Flask, jsonify, request
from dotenv import load_dotenv
import blocksmc
import os

load_dotenv()

USERNAME = os.getenv('MCUSERNAME')
HASH = os.getenv('HASH')

blocksmc = blocksmc.BlocksMC(USERNAME, HASH)

app = Flask(__name__)

@app.route("/search")
def search():
    username = request.args.get('username')
    
    if (username is None): return {"code": 400, "error": "missing username"}
    try:
        player = blocksmc.getPlayer(username)

        data = {
            "query": username,
            "rank": player.rank,
            "minutes_of_playtime": round(float(player.hours_played) * 60),
            "games": {}
        }
        
        for game in player.games:
            data["games"][game.name] = game.stats

        return jsonify(data)
    except:
        return jsonify({"code": "500"})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8000)