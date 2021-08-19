import pandas as pd
import datetime
import json

df = pd.read_excel('./data/dmg_tento.xlsx')

exhibitions = []

for index, row in df.iterrows():
    identifier = row['ID']
    name = {}

    if not pd.isnull(row['TITEL NL ']):
        name['nl'] = row['TITEL NL ']

    if not pd.isnull(row['TITEL FR']):
        name['fr'] = row['TITEL FR']

    if not pd.isnull(row['TITEL_ENG']):
        name['en'] = row['TITEL_ENG']

    location = {
        "@type": "Place",
        "name": {
            'nl': row['INSTELLING']
        }
    }
    if isinstance(row['BEGINDATUM'], datetime.date):
        startDate = row['BEGINDATUM'].strftime('%Y-%m-%d')
    else:
        startDate = ""

    if isinstance(row['EINDDATUM'], datetime.date):
        endDate = row['EINDDATUM'].strftime('%Y-%m-%d')
    else:
        endDate = ""

    event = {
        "@context": "https://schema.org",
        "@type": "ExhibitionEvent",
        "identifier": identifier,
        "location": location,
        "name": name,
        "startDate": startDate,
        "endDate": endDate
    }

    exhibitions.append(event)

out_file = open("exhibitions.json", "w")
json.dump(exhibitions, out_file, indent=2)
out_file.close()