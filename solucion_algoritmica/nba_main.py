# Test challenge nba height players nba
# Dev @jhoninsuasti3
# Date : 22-05-2022


import json
import requests
#import nba_players_data_app.constants   as cons


""" 
    Search information in data returned
"""
def search(valuenumeric):
    response = requests.get("https://mach-eight.uc.r.appspot.com/")
    return_data = json.loads(response.text)
    players = return_data["values"]
    #will keep the height as a key and its index in the list of players as a value -->
    idx_map = {}  
    response_final = []

    for idx, p in enumerate(players):
        h_in = int(p['h_in'])
        if valuenumeric - h_in in idx_map.keys():  
            p1 = players[idx_map[valuenumeric - h_in]]  
            p2 = players[idx]
            response_final.append((p1, p2))  
        idx_map[h_in] = idx  
    return response_final

""" 
    Obtain values data for print
"""
def get_player_data(player):
    return f"{player['first_name']} {player['last_name']} "

"""
    Main program, verification logyc in input and output
"""
def main():
        try:
            valuenumeric = int(input("Insert value numeric: "))
            result = search(valuenumeric)
            players = []
            for pair in result:
                players.append(( f" {get_player_data(pair[0])}   {get_player_data(pair[1])} "))
                print(f" {get_player_data(pair[0])}   {get_player_data(pair[1])} ")
            if len(players) == 0 :
                print("Not match found")
        except ValueError:
            print("Please insert integer value")


if __name__ == "__main__":
    main()