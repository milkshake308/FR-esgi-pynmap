import pandas as pa
import sys
USAGE = """
USAGE : report_reader.py <filename_of_scan_report.log>
"""

#  Converti le rapport en dataframe
def parse_report(filename):
    try:
        with open(filename, 'r') as f:
            report_header = [next(f) for line in range(6)]
            report_header = ''.join(report_header)
            report_header = report_header.replace('\n', '\r\n'.replace('\t', '\t'))
            df = pa.read_csv(f, sep='\t')
    except FileNotFoundError as e:
        print("Le fichier n'a pas été trouvé, vérifiez le chemin d'accès du fichier et le contexte d'éxécution du programme", e)
    except Exception as e:
        print("Impossible de lire le fichier",e)

    print("Fichier de rapport chargé :", filename)
    report_footer = df.iloc[-1].to_string(index=False).replace('NaN', '')
    df = df.drop(df.index[-1])
    
    #  Définition des colonnes 
    df = df.drop(df.columns[1], axis=1)
    df.columns = ['Horodatage', 'Protocol', 'Port', 'Etat']
    df['Port'] = df['Port'].astype(int)
    df = df.sort_values('Port', ascending=True)
    return  report_header, df, report_footer

def filter_with_services(service_file ,df_report, skip_closed_ports=True):
    try:
        df_services = pa.read_csv(service_file)
    except pa.errors.ParserError as e:
        print("Erreur de parsing du fichier CSV, vérifiez le format du fichier", e)
    except FileNotFoundError as e:
        print("Le fichier de services.csv n'a pas été trouvé, \n Vérifiez qu'un fichier services.csv avec les colonnes Port, Protocol, Description existe (sensible a la casse)", e)
    except Exception as e:
        print("Impossible de lire le fichier",e)

    # On joint les deux dataframe 
    df_services['Protocol'] = df_services['Protocol'].str.upper()
    df = pa.merge(df_report, df_services, on=['Port', 'Protocol'], how='left')
    df = df.drop_duplicates(subset=['Port', 'Protocol'])

    #  On ignore les ports Fermé
    if skip_closed_ports: df = df[df['Etat'] != 'Fermé']
    
    return df


if len(sys.argv) > 1:
    # Récupérer le premier argument passé
    filename = sys.argv[1]
    report_head, report, report_footer = parse_report(sys.argv[1])

    pa.set_option('display.max_rows', None)
    pa.set_option('display.max_columns', None)

    print(report_head)
    print(filter_with_services(service_file="./services.csv", df_report=report))
    print(report_footer)
else:
    print(USAGE)
