import components.misc as misc
import components.net as net

while True:

    while True:
        host = input("Nom d'hôte ou adresse IP pour le scan: ")
        if net.ping(host): 
            break
        if misc.prompt_yes_no("L'hôte semble ne pas être joignable, voulez-vous malgré tout poursuivre ?"): 
            break

    port_start = misc.ask_user(
                            query = "Port de début :", 
                            valid_args = range(1,65535),
                            )
    port_end = misc.ask_user(query = "Port de fin (vide si identique) :", 
                            valid_args = range(port_start,65535), 
                            default_value = port_start, 
                            allow_empty = True,
                            )

    is_udp = misc.prompt_yes_no("Voulez-vous faire un scan UDP ?")
    is_parallel = misc.prompt_yes_no("Voulez-vous faire un scan de ports en parallèle ?")
    print()
    net.scan_handler(
        host= host,
        port_start= port_start,
        port_end= port_end,
        proto= "UDP" if is_udp else "TCP",
        parallel_threads= is_parallel,
        verbose=True
    )
    if not misc.prompt_yes_no("Voulez refaire un scan ?"):
        break