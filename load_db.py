import csv
from pymongo import MongoClient
from pprint import pprint

client = MongoClient()

class load_db:

    def __init__(self):
        self.db = client.CrashesDB
        self.crashes = self.db.crashes
        if len( self.db.collection_names() ) == 0:
            self.load_db()

    def load_db(self):
        print ("loading")
        data = []
        with open('NYPD_Motor_Vehicle_Collisions.csv') as cf:
            reader = csv.DictReader(cf)
            for line in reader:
                data.append(line)
        for i in data:
            self.crashes.insert(i)

    def test(self):
        print ("item count: ")
        print(self.crashes.count() )
        #pprint (self.crashes.find_one() )

if __name__ == "__main__":
    obj = load_db()

    obj.test()