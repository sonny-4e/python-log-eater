import re
from collections import Counter

def parse_logs(file_path):
    """Funkcja do analizy pliku z logami."""
    
    # Kompilujemy wzorzec (Regex)
    log_pattern = re.compile(r'^(\S+).*?"\s+(\d{3})')
    
    # incjalizuje licznik
    status_counter = Counter()
    
    try:
        #  bloku 'with', aby plik automatycznie zamknął się po zakończeniu czytania
        with open(file_path, 'r') as file:
            for line in file:
                
                match = log_pattern.search(line)
                
                if match:
                    ip_address = match.group(1)
                    status_code = match.group(2)

                    status_counter[status_code] += 1
                    print(f"Znaleziono -> IP: {ip_address} | Status: {status_code}")
                
            print("\n" + "="*30)
            print(" RAPORT: PODSUMOWANIE KODÓW HTTP ")    
            print("="*30)
            
            
            for status, count in status_counter.most_common():
                print(f"Kod {status}: {count} wystąpień")
                        
    except FileNotFoundError:
        print(f"Błąd: Nie znaleziono pliku {file_path}")

if __name__ == "__main__":
    # Punkt wejścia naszego skryptu
    log_file = "logs/access.log"
    print(f"--- Rozpoczynam analizę pliku: {log_file} ---")
    parse_logs(log_file)