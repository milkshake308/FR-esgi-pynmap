import csv

# Ouvrir le fichier de services
with open("/etc/services") as f:
    # Créer un lecteur pour lire les données dans le fichier
    reader = csv.reader(f, delimiter="\t")
    next(reader)
    next(reader)
    # Créer une liste pour stocker les informations sur les ports
    ports = []
    
    # Parcourir chaque ligne du fichier
    for row in reader:
        # Extraire les informations sur le port
        
        port_info = row[0].split("/")
        if len(port_info) != 2:
            continue
        
        port, proto = port_info
        try:
            desc = row[1].strip()
        except:
            desc = ""
        
        # Ajouter les informations sur le port à la liste
        ports.append((port, proto, desc))

# Écrire la liste des ports dans un fichier CSV
with open("ports.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Port", "Protocol", "Description"])
    writer.writerows(ports)
