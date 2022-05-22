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