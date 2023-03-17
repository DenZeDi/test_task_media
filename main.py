import json
import pandas as pd

with open(r"kfc_locations.json", 'r', encoding='utf8') as read_file:
    data = json.load(read_file)

df_locations = pd.DataFrame(columns=['INDEX', 'CITY', 'ADDRESS', 'COORD', 'STL', 'ETL', 'TF', 'TT', 'F'])

features = set()

for point in data.get('searchResults'):
    data_row = []
    if point['storePublic']['localStoreId'] is not None:
        if len(point['storePublic']['contacts']['streetAddress']['ru'].split(', ')) > 1:
            address_list = point['storePublic']['contacts']['streetAddress']['ru'].split(', ')

            index = address_list[0]
            city = address_list[1]
            temp_addr = address_list[2:]
            address = ", ".join(temp_addr)

        coord = point['storePublic']['contacts']['coordinates']['geometry']['coordinates']

        stl = point['storePublic']['openingHours']['regular']['startTimeLocal']
        etl = point['storePublic']['openingHours']['regular']['endTimeLocal']

        if point['storePublic']['openingHours']['driveInDaily'] is not None:
            tf = point['storePublic']['openingHours']['driveInDaily'][0]['timeFrom']
            tt = point['storePublic']['openingHours']['driveInDaily'][0]['timeTill']
        else:
            tf = None
            tt = None

        f = point['storePublic']['features']

        for feature in point['storePublic']['features']:
            features.add(feature)

        data_row.extend([index, city, address, coord, stl, etl, tf, tt, f])

        df_locations.loc[len(df_locations)] = data_row

print(df_locations)
