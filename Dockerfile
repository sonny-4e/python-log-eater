# 1. Baza: Używamy oficjalnego, lekkiego obrazu z językiem Python
FROM python:3.11-slim

# 2. Ustawiamy katalog roboczy wewnątrz kontenera (jak komenda 'cd /app')
WORKDIR /app

# 3. Kopiujemy nasze pliki z Twojego komputera do wnętrza kontenera
COPY main.py .

# 4. Definiujemy komendę, która ma się wykonać, gdy kontener wystartuje
CMD ["python", "main.py"]