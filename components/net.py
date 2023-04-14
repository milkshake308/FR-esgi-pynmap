import socket, subprocess, threading, platform
from datetime import datetime

def check_port(host: str, port: int, proto: str, timeout: int):
    

    try:
        ip = socket.gethostbyname(host)
        sock = socket.socket(
                            socket.AF_INET, 
                            socket.SOCK_DGRAM if proto.upper()=='UDP' else socket.SOCK_STREAM
                            )
        sock.settimeout(timeout)
        if sock.connect_ex((ip, port)) == 0:
            sock.close()
            return True
        else:
            sock.close()
            return False


    
    except socket.error:
        pass

def timestamp_line(*args):
    log_line = '\t'.join(str(x) for x in args)
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+'\t'+log_line

def save_file(lines: list, filename: str):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(f"{line}\n")

def ping(host :str):
    print("Ping en cours...", end=' ', flush=True)
    try:
        subprocess.check_output(
            ['ping','-n' if platform.system().lower()=='windows' else '-c', 
            '1',
            host]
            )
        print("OK !")
        return True
    except subprocess.CalledProcessError:
        print()
        return False

def progressbar(current, total):
    bar_width = 50
    fill_width = int(round(bar_width * current / float(total)))
    percent = round(100.0 * current / float(total), 1)
    bar = '=' * fill_width + '-' * (bar_width - fill_width)
    print(f'[{bar}] {percent}%\r', end='')
    
def scan_handler(host: str, port_start: int, port_end: int, report_name="Rapport_de_scan_de_", proto="TCP", parallel_threads=False, socket_timeout=2, verbose=False):
    no_progressbar = False
    if port_end is None :
        parallel_threads = False
        no_progressbar = True
        port_end = port_start

    total_ports = port_end - port_start + 1
    start_time = datetime.now()
    logs = []

    # Pour un resultat sous forme textuelle
    def open_or_closed(port):
        cnst =  "Ouvert" if check_port(host, port, proto, socket_timeout) else "Fermé"
        return f"Port\t{proto}\t{port}\t"+cnst

    # Woker pour traitement parallèle
    def scanner_worker(port_start, port_end):
        for port in range(port_start, port_end+1):
            logs.append(timestamp_line(open_or_closed(port)))
            if verbose and not no_progressbar: progressbar(len(logs)-1, total_ports)

    logs.append(f"""Scan de ports avec comme paramètres :  \n
Protocole : {proto}\t\t Nom d'hôte : {host}
Port de début : {port_start}\t\t Timeout Max. socket : {socket_timeout}
Port de fin : {port_end}\t\t Execution parallèle : {"Désactivé" if not parallel_threads else str(int(total_ports/10))+" threads"}
""")
    if verbose:
        print(logs[0])
    

    if port_start==port_end:
        stat = timestamp_line(open_or_closed(port_start))
        logs.append(stat)
    elif parallel_threads :
        threads = []
        step = 10
        for i in range(0, total_ports, step):
            t = threading.Thread(target=scanner_worker, args=(port_start+i, port_start+i+step-1))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        if verbose and not no_progressbar: progressbar(len(logs)-1, total_ports)
        print()
    else:
        for port in range(port_start, port_end+1):
            logs.append(timestamp_line(open_or_closed(port)))
            if verbose and not no_progressbar : 
                progressbar(len(logs)-1, total_ports)
        if verbose and not no_progressbar : print()
        

    logs.append(timestamp_line(f"Temps total d'éxécution du scan : {datetime.now().replace(microsecond=0) - start_time.replace(microsecond=0)}"))
    report_filename = report_name+host+datetime.now().strftime('%Y-%m-%d_%H-%M')+".log"
    save_file(logs, report_filename)
    if verbose:
        print(f"Rapport généré : {report_filename}")
