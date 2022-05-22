import json
import requests


def search(target_sum):
    response = requests.get("https://mach-eight.uc.r.appspot.com/")
    data = json.loads(response.text)
    players = data["values"]

    idx_map = {}  # will hold the height as key and it's index in the player list as value
    answer_list = []

    for idx, p in enumerate(players):
        h_in = int(p['h_in'])
        if target_sum - h_in in idx_map.keys():  # the complementary value is in the idx_map!
            p1 = players[idx_map[target_sum - h_in]]  # the according player is resolved
            p2 = players[idx]
            answer_list.append((p1, p2))  # save 'em as a fine tuple

        idx_map[h_in] = idx  # save the idx of the player at the

    return answer_list


def get_person_string(player):
    return f"{player['first_name']} {player['first_name']} ({player['h_in']})"


def main():
    while 1:
        try:
            target_sum = int(input("Insert target sum: "))
            result = search(target_sum)
            for pair in result:
                print(f"Player {get_person_string(pair[0])} and Player {get_person_string(pair[1])} "
                      f"together are {target_sum} inches tall.")
        except ValueError:
            break


if __name__ == "__main__":
    main()