import json
import pandas as pd

with open("kfc_locations.json", 'r', encoding='utf8') as read_file:
    data = json.load(read_file)

df_locations = pd.DataFrame(columns=['Index', 'City', 'Address', 'Lat_coord', 'Long_coord',
                                     'STL', 'ETL', 'TF', 'TT',
                                     'BF', 'WW', 'Wifi', 'DI', 'RtC'])

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

        for feature in point['storePublic']['features']:
            bf = 1 if feature == 'breakfast' else 0
            ww = 1 if feature == 'walkupWindow' else 0
            wifi = 1 if feature == 'wifi' else 0
            di = 1 if feature == 'driveIn' else 0
            rtc = 1 if feature == '24hours' else 0

        data_row.extend([index, city, address, lat_coord, long_coord,
                         stl, etl, tf, tt,
                         bf, ww, wifi, di, rtc])

        df_locations.loc[len(df_locations)] = data_row

df_locations.to_csv('df_location', index=False)
