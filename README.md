# Suite d'outils d'analyse de port réseau

Ce projet est une suite d'outils d'analyse de port réseau développée en Python. Les principales fonctionnalités de cette suite sont :

1. **Scan par assistant** : 

    Vous pouvez lancer l'assistant de scan en exécutant le fichier `scan.py`. L'assistant vous guidera dans la saisie des paramètres du scan et générera ensuite un rapport dans le répertoire d'exécution.

2. **Scan sans interaction utilisateur** : 

    Vous pouvez également effectuer un scan sans interaction utilisateur en exécutant le script `cscan.py` en passant en arguments vos choix. 
    
    Exemple d'utilisation : `python cscan.py boobagump.fr 22 --port_end 1200 -P`. Le programme générera ensuite un rapport dans le répertoire d'exécution.

3. **Rapports et Lecteur de rapport** : 
    
    Les rapports générés sont délimités par tabulation, ce qui les rend exploitables dans n'importe quel logiciel tableur. 
    
    Un fichier `services.csv` est également mis à disposition, contenant la liste des ports connus, leur protocole (TCP/UDP) ainsi que leur description, pour faciliter l'analyse. Vous pouvez éditer ce fichier pour ajouter des entrées personnalisées et l'utiliser dans le lecteur de rapport. Vous pouvez exécuter le programme `report_reader.py` en passant en argument un rapport généré par l'un des scripts de scan. Le programme lira le fichier de rapport et vous retournera les éléments exploitables. 

    Exemple d'utilisation : `python report_reader.py ./Rapport_de_scan_du_2023-04-10_18:59.log`. Notez que vous devrez installer les prérequis via `pip install -r requirements.txt`, car ce script utilise le module `pandas`.

4. **Module components.net** : 
    
    Le module `components.net` peut être intégré dans n'importe lequel de vos projets Python 3 pour réutiliser la fonction `scan_handler()`, qui permet d'effectuer un scan en fonction de divers paramètres et de générer un rapport.

N'hésitez pas à explorer et à utiliser cette suite d'outils d'analyse de port réseau pour faciliter vos tâches d'analyse de sécurité et de gestion des ports réseau.
