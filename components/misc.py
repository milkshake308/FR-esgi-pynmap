def ask_user(query: str , valid_args, default_value=False, allow_empty=False):
    while True:
        x = input(query+" ")

        #  Essaye de convertir en entier si la valeur est un entier
        try:
            x = int(x)
        except:
            #  J'avais utilisé continue pensant que c'était interchangeable, sauf que ça reset la boucle
            pass 

        if x in valid_args:
            return x
        elif allow_empty and x == "":
            return default_value
        else:
            print("Valeur incorrecte !")

def prompt_yes_no(prompt: str):
    while True:
        response = input((prompt+' [y/N]: '))
        if response.lower() in ["y", "yes", "o", "oui"]:
            return True
        elif response.lower() in ["n", "no", "non", ""]:
            return False
        else:
            print("Merci de saisir 'yes' ou 'no'.")