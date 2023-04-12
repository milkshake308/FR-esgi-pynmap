import sys

USAGE = """
USAGE : 
    main.py <arg1> <arg2> .... <premier port>-<dernier port (optionnel)> 

ARGUMENTS :

    -p  --proto          : scan en spécifiant le protocole TCP ou UDP, par défaut TCP (ex : main.py -p UDP 80-443)
    -P  --parallel       : scan en mode parallèle  (ex : main.py -P 80-443)

EXEMPLES :
    main.py 80
    main.py -p UDP 1194
    main.py --parallel --port UDP 80-10000
"""

if len(sys.argv) > 1:
    args = sys.argv[1:]
    print("Les arguments passé sont ")
    for arg in args: print(arg)
else:
    print(USAGE)