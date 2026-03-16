import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
from datetime import date

# Schritt 1: Schema laden (aus einer Datei oder einem String)
schema_json = '''
{
    "type": "record",
    "namespace": "com.lehrbuch.daten",
    "name": "Kunde",
    "fields": [
        { "name": "Kunden_ID", "type": "int" },
        { "name": "Name", "type": "string" },
        { "name": "Wohnort", "type": "string" },
        { "name": "Registriert_seit", "type": { "type": "int", "logicalType": "date" } }
    ]
}
'''
schema = avro.schema.parse(schema_json)

# Unsere Kundendaten, die dem Schema entsprechen
kunden_daten = [
    {'Kunden_ID': 101, 'Name': 'Meier', 'Wohnort': 'Berlin',
     'Registriert_seit': date(2022, 3, 15)},
    {'Kunden_ID': 102, 'Name': 'Huber', 'Wohnort': 'München',
     'Registriert_seit': date(2021, 11, 20)},
    {'Kunden_ID': 103, 'Name': 'Schmidt', 'Wohnort': 'Hamburg',
     'Registriert_seit': date(2023, 1, 5)}
]

# Schritt 2: Daten in eine Avro-Datei schreiben
with open('kunden.avro', 'wb') as f:
    writer = DataFileWriter(f, DatumWriter(), schema)
    for kunde in kunden_daten:
        writer.append(kunde)
    writer.close()

# Schritt 3: Daten aus der Avro-Datei lesen
with open('kunden.avro', 'rb') as f:
    reader = DataFileReader(f, DatumReader())
    for kunde in reader:
        registrierungsdatum = kunde['Registriert_seit']
        print(f"ID: {kunde['Kunden_ID']}, Name: {kunde['Name']}, "
              f"Datum: {registrierungsdatum.isoformat()}")
    reader.close()