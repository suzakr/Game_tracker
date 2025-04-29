import requests

api = requests.get("https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=48322C8A72A39F8B442C8288285F7B68&steamid=76561198090178023&include_appinfo=true&include_played_free_games=true&format=json")

jsn_api = api.json()

def gtime():
    for game in jsn_api['response']['games']:
        print(game['playtime_forever'])

def gname():
    for game in jsn_api['response']['games']:
        x = game['name']
        glist.append(x)

glist = []

# vygeneruje API a udela z nej list, ktery se zobrazi jako moznosti her, ktere vlastnim na Steamu
# dale pak budu API zpracovavat tak, aby mi aplikace zobrazovala i herni cas