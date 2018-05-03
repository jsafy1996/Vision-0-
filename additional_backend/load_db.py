import csv
from pymongo import MongoClient
from pprint import pprint

client = MongoClient()

class load_db:

    def __init__(self):
        #database name: CrashesDB
        self.db = client.CrashesDB
        #collection name: crashes
        self.crashes = self.db.crashes

        #populate database if not populated
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

    #test function
    #outputs item count and a sample object
    def test(self):
        print ("item count: ")
        print(self.crashes.count() )
        print ("item sample: ")
        pprint (self.crashes.find_one() )

    # number of accidents in borough (percent--like a pie chart)
    def accident_count(self):
        dummy = 0

   

#main function
if __name__ == "__main__":
    obj = load_db()

    obj.test()