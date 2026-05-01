def parse_logs(file_path):
    """Funkcja do analizy pliku z logami."""
    try:
        # Używamy bloku 'with', aby plik automatycznie zamknął się po zakończeniu czytania
        with open(file_path, 'r') as file:
            for line in file:
                # .strip() usuwa białe znaki z początku i końca (np. znak nowej linii \n)
                print(line.strip()) 
    except FileNotFoundError:
        print(f"Błąd: Nie znaleziono pliku {file_path}")

if __name__ == "__main__":
    # Punkt wejścia naszego skryptu
    log_file = "access.log"
    print(f"--- Rozpoczynam analizę pliku: {log_file} ---")
    parse_logs(log_file)