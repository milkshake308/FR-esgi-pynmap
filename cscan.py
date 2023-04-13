import argparse
import components.net as net


parser = argparse.ArgumentParser(description='Script de scan réseau sans interaction utilisateur ')

# Définition des arguments obligatoires
parser.add_argument('host', type=str, help='Nom d\'hôte')

parser.add_argument('port_start', type=int, help='Port de début')

# Définition des arguments facultatifs
parser.add_argument('--port_end', type=int, help='Port de fin (facultatif)')

parser.add_argument('--proto','-p', type=str, choices=['TCP', 'UDP'], default='TCP',
                    help='Protocole (TCP ou UDP, facultatif, défaut: TCP)')

parser.add_argument('--parallel_threads', '-P', action='store_true',
                    help='Utiliser l\'exécution parallèle (facultatif)')

# Analyse des arguments de ligne de commande
args = parser.parse_args()

# Passage des arguments à la fonction net.scan_handler()
net.scan_handler(host=args.host,
                 port_start=args.port_start,
                 port_end=args.port_end,
                 proto=args.proto,
                 parallel_threads=args.parallel_threads)
