#Prueba tecnica para mach
# Desarrollado por @jhoninsuasti


# Import libraries
import requests, json


def import_data():
    url = requests.get("https://mach-eight.uc.r.appspot.com/")
    text = url.text
    #print(type(text))
    data = json.loads(text)
    return data

def search(valuenumeric):
    response = requests.get("https://mach-eight.uc.r.appspot.com/")
    return_data = json.loads(response.text)
    players = return_data["values"]
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


def search_player():
    pass 

def obtain_inputs():
    valor = int(input("Digite el valor"))

def test_values():
    tst = import_data()
    print(tst)

def main():
    print("Main principal")
    import_data()
    #test_values()

if __name__ == "__main__":
    main()