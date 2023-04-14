import socket

# Définir le numéro de port UDP cible et l'adresse IP de la machine
udp_port = 1199
udp_host = "82.64.241.145"

# Créer un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Définir une valeur de timeout en secondes
sock.settimeout(5)

# Essayer de se connecter au port UDP cible
try:
    sock.sendto(b"ping", (udp_host, udp_port))
    data, addr = sock.recvfrom(1024)
    print("Le port UDP {} est ouvert et en écoute".format(udp_port))
except socket.timeout:
    print("Le port UDP {} n'est pas ouvert ou n'est pas en écoute".format(udp_port))
except ConnectionRefusedError:
    print("La connexion a été refusée sur le port UDP {}".format(udp_port))

# Fermer le socket
sock.close()
