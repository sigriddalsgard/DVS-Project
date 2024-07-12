
import pandas as pd

# Læs CSV-filen, angiv separatoren som ';'
newFile = pd.read_csv('air-pollution.csv')

# Fjern kolonner, hvor alle felter er tomme
newFile = newFile.dropna(axis=1, how='all')

# Kolonner, der skal konverteres
columns_to_convert = [
    'Avoidable deaths [WHO 2005 levels] [PM2.5]',
    'Avoidable deaths [WHO 2021 levels] [PM2.5]',
    'Avoidable deaths [lowest levels] [PM2.5]',
    'Avoidable deaths [WHO 2005 levels] [NO2]',
    'Avoidable deaths [WHO 2021 levels] [NO2]',
    'Avoidable deaths [lowest levels] [NO2]'
]

# Konverter hver kolonne fra streng med komma til float med punktum
for column in columns_to_convert:
    newFile[column] = newFile[column].replace(',', '').astype(int)

# Gem det rensede DataFrame i en ny CSV-fil med ',' som separator
newFile.to_csv('cleaned-air-pollution.csv', sep=',', index=False)

