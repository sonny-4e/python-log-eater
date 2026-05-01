import re

def parse_logs(file_path):
    """Funkcja do analizy pliku z logami."""
    
    # Kompilujemy wzorzec (Regex)
    log_pattern = re.compile(r'^(\S+).*?"\s+(\d{3})')
    
    try:
        #  bloku 'with', aby plik automatycznie zamknął się po zakończeniu czytania
        with open(file_path, 'r') as file:
            for line in file:
                
                match = log_pattern.search(line)
                
                if match:
                    ip_address = match.group(1)
                    status_code = match.group(2)

                    print(f"Znaleziono -> IP: {ip_address} | Status: {status_code}")
                
                              
    except FileNotFoundError:
        print(f"Błąd: Nie znaleziono pliku {file_path}")

if __name__ == "__main__":
    # Punkt wejścia naszego skryptu
    log_file = "access.log"
    print(f"--- Rozpoczynam analizę pliku: {log_file} ---")
    parse_logs(log_file)