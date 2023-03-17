import json
import pandas as pd

with open(r"kfc_locations.json", 'r', encoding='utf8') as read_file:
    data = json.load(read_file)

df_locations = pd.DataFrame(columns=['INDEX', 'CITY', 'ADDRESS', 'COORD', 'STL', 'ETL', 'TF', 'TT', 'F'])
# print(df_locations)

for city in data.get('searchResults'):
    if city['storePublic']['localStoreId'] is not None:
        if len(city['storePublic']['contacts']['streetAddress']['ru'].split(', ')) > 1:
            print('INDEX', city['storePublic']['contacts']['streetAddress']['ru'].split(', ')[0])
            print('CITY', city['storePublic']['contacts']['streetAddress']['ru'].split(', ')[1])
            address = city['storePublic']['contacts']['streetAddress']['ru'].split(', ')[2:]
            print('ADDRESS', ", ".join(address))

        print('COORD', city['storePublic']['contacts']['coordinates']['geometry']['coordinates'])

        print('STL', city['storePublic']['openingHours']['regular']['startTimeLocal'])
        print('ETL', city['storePublic']['openingHours']['regular']['endTimeLocal'])

        if city['storePublic']['openingHours']['driveInDaily'] is not None:
            print('TF', city['storePublic']['openingHours']['driveInDaily'][0]['timeFrom'])
            print('TT', city['storePublic']['openingHours']['driveInDaily'][0]['timeTill'])

        print('F', city['storePublic']['features'])


# print(type(data.get('searchResults')[3]))
# print(data.get('searchResults')[3])

