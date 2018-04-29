from pymongo import MongoClient
from bson.son import SON

database = 'CrashesDB'
collection = 'crashes'

client = MongoClient()

db = client[database]

db2 = client.Crashes2DB

#collection = db[collection]
collection2 = db2.crashes

def stuff(raw_data):
    #raw_data = "(40.768890000000006, -73.96457000000001),(40.76921, -73.96535),(40.76794, -73.96625),(40.76671, -73.96717000000001),(40.76545, -73.96808),(40.7642, -73.96900000000001),(40.762950000000004, -73.96988),(40.76231000000001, -73.97035000000001),(40.762240000000006, -73.97017000000001),(40.7616, -73.96863),(40.75901, -73.97054),(40.757580000000004, -73.97159),(40.7565, -73.97237000000001),(40.7558, -73.97290000000001),(40.75527, -73.97329),(40.75462, -73.97373),(40.754020000000004, -73.97419000000001),(40.75276, -73.97511),(40.752, -73.97566),(40.75016, -73.97699),(40.74573, -73.98022),(40.74327, -73.98199000000001),(40.7408, -73.98382000000001),(40.740170000000006, -73.98426),(40.740100000000005, -73.98411)"

    #processed_data = raw_data
    processed_data = process(raw_data)

    crashes = []
    for coords in processed_data:
        [crashes.append({"lat": float(i["LATITUDE"]), "lng": float(i["LONGITUDE"])}) for i in collection2.find({ "$and" : [{ "LAT": coords[0] }, {"LONG": coords[1] }] })]
    

    return crashes

    # #for j in range(0, len(processed_data), 5):
    # for index, coords in enumerate(processed_data):
    #     #{"CONTRIBUTING FACTOR VEHICLE 1": "Bicycle",
    #     if index % 5 == 0: 
    #         for index in collection.find( {'$and': [{"LAT": coords[0], "LONG": coords[1]}]} ):
    #             thing.append([index['LATITUDE'], index['LONGITUDE']])
    # print(thing)

def process(raw_data):
    processed_data = []

    for coords in raw_data.split(')'):
        coords = coords.replace(',', '').replace('(', '')
        if coords[:6] != '':
            processed_data.append([
                round(float(coords[:7]), 3),
                round(float(coords[coords.find(' ') + 1: coords.find(' ') + 9]), 3)])
                
    #list(set(coordPairs))
    return processed_data

def fix_points(raw_data):
    results = []
    for coords in raw_data:
        results.append(
            '{lat: ' + '{0}'.format(coords[0]) + ', lng: ' + '{0}'.format(coords[1]))
        
    return results

#takes type float
def rounder(num):
    rounded = round(num, 3)
    return rounded

def fix_database():
    print("querying...")
    for i in collection2.find():
        if i['LATITUDE'] != '':
            i['LAT'] = rounder( float(i['LATITUDE']))
            i['LONG'] = rounder( float(i['LONGITUDE']))
        collection2.save(i)
    print("querying done")

