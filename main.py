import json
import pandas as pd

with open(r"kfc_locations.json", 'r', encoding='utf8') as read_file:
    data = json.load(read_file)

df_locations = pd.DataFrame(columns=['INDEX', 'CITY', 'ADDRESS', 'COORD', 'STL', 'ETL', 'TF', 'TT', 'F'])
print(df_locations)

features = set()

for point in data.get('searchResults'):
    data_row = []
    if point['storePublic']['localStoreId'] is not None:
        if len(point['storePublic']['contacts']['streetAddress']['ru'].split(', ')) > 1:
            address_list = point['storePublic']['contacts']['streetAddress']['ru'].split(', ')
            # print(address_list)

            index = address_list[0]
            # print('INDEX', index)
            # print('INDEX', point['storePublic']['contacts']['streetAddress']['ru'].split(', ')[0])

            # print('CITY', point['storePublic']['contacts']['streetAddress']['ru'].split(', ')[1])
            city = address_list[1]
            # print('CITY', city)

            # print('ADDRESS', point['storePublic']['contacts']['streetAddress']['ru'].split(', ')[2:])
            temp_addr = address_list[2:]
            address = ", ".join(temp_addr)
            # print('ADDRESS', address)

        # print('COORD', city['storePublic']['contacts']['coordinates']['geometry']['coordinates'])
        # print(type(point['storePublic']['contacts']['coordinates']['geometry']['coordinates']))
        coord = point['storePublic']['contacts']['coordinates']['geometry']['coordinates']
        # print('COORD', coord)
        # print('COORD', city['storePublic']['contacts']['coordinates']['geometry']['coordinates'])

        stl = point['storePublic']['openingHours']['regular']['startTimeLocal']
        # print('STL', stl)
        # print('STL', point['storePublic']['openingHours']['regular']['startTimeLocal'])
        etl = point['storePublic']['openingHours']['regular']['endTimeLocal']
        # print('ETL', etl)
        # print('ETL', point['storePublic']['openingHours']['regular']['endTimeLocal'])

        if point['storePublic']['openingHours']['driveInDaily'] is not None:
            tf = point['storePublic']['openingHours']['driveInDaily'][0]['timeFrom']
            # print('TF', tf)
            # print('TF', point['storePublic']['openingHours']['driveInDaily'][0]['timeFrom'])
            tt = point['storePublic']['openingHours']['driveInDaily'][0]['timeTill']
            # print('TT', tt)
            # print('TT', point['storePublic']['openingHours']['driveInDaily'][0]['timeTill'])
        else:
            tf = None
            tt = None

        f = point['storePublic']['features']
        # print('F', f)

        for feature in point['storePublic']['features']:
            features.add(feature)

        data_row.extend([index, city, address, coord, stl, etl, tf, tt, f])

        df_locations.loc[len(df_locations)] = data_row

        # df_locations = df_locations.append(data_row, ignore_index=False)

        # print(data_row)
    # break

# print(features)

print(df_locations)

# print(type(data.get('searchResults')[3]))
# print(data.get('searchResults')[3])

