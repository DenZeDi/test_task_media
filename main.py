import json
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///df_location.db', echo=False)

with open(r"kfc_locations.json", 'r', encoding='utf8') as read_file:
    data = json.load(read_file)

df_locations = pd.DataFrame(columns=['INDEX', 'CITY', 'ADDRESS', 'LAT_COORD', 'LONG_COORD', 'STL', 'ETL', 'TF', 'TT'])

features = set()

for point in data.get('searchResults'):
    data_row = []
    if point['storePublic']['localStoreId'] is not None:
        if len(point['storePublic']['contacts']['streetAddress']['ru'].split(', ')) > 1:
            address_list = point['storePublic']['contacts']['streetAddress']['ru'].split(', ')

            if address_list[0].isdigit():
                index = address_list[0]
                city = address_list[1]
                address = ", ".join(address_list[2:]).replace('\n', '')
            else:
                index = None
                city = address_list[0]
                address = ", ".join(address_list[1:]).replace('\n', '')

        coord = point['storePublic']['contacts']['coordinates']['geometry']['coordinates']
        lat_coord = coord[0]
        long_coord = coord[1]

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

        data_row.extend([index, city, address, lat_coord, long_coord, stl, etl, tf, tt])

        df_locations.loc[len(df_locations)] = data_row

df_locations.to_csv('df_location', index=False)

# df_locations.to_sql(name='df_location', con=engine, index=False, if_exists='replace')

print(df_locations)



