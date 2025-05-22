"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import pandas as pd

def dividir_claves_con_coma_y_espacio(texto):
    partes = []
    buffer = ''
    for char in texto:
        buffer += char
        if buffer.endswith(', '):
            partes.append(buffer)
            buffer = ''
    if buffer:  
        partes.append(buffer)
    return partes

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    with open("files/input/clusters_report.txt") as data:
        lines = data.readlines()
    
    # Quitar lineas vacias o separadores
    lines = [line.rstrip() for line in lines if line.strip() and not line.startswith("----")]
    
    lines = lines[2:]
    clusters = []
    current_cluster = None

    for line in lines:
        parts = line.split()

        if parts[0].isdigit():
            if current_cluster:
                clusters.append(current_cluster)
            
            cluster = int(parts[0])
            cantidad = int(parts[1])
            porcentaje_str = parts[2].replace(",", ".").replace("%","")
            porcentaje = float(porcentaje_str)

            palabras = " ".join(parts[3:]).replace("%", "")
            current_cluster = {
                'cluster': cluster,
                'cantidad_de_palabras_clave': cantidad,
                'porcentaje_de_palabras_clave': porcentaje,
                'principales_palabras_clave': palabras
            }
        else:
            if current_cluster:
                current_cluster["principales_palabras_clave"] += " " + " ".join(parts)

    if current_cluster:
        clusters.append(current_cluster)

    for c in clusters:
      texto = ' '.join(c['principales_palabras_clave'].split())  # Limpia espacios
      claves = dividir_claves_con_coma_y_espacio(texto)
      claves = [clave.replace(".","") for clave in claves] # Separa por coma, limpia espacios y puntos
      c['principales_palabras_clave'] = "".join(claves)
    
    df = pd.DataFrame(clusters)
    return df




if __name__ == "__main__":
    print(pregunta_01().principales_palabras_clave.to_list()[0])
  