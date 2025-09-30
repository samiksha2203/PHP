# 1. Insert()
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['7Y77DB259711']

def insert():
    try:
        name1 = input("Enter the Name:")
        age1 = input("Enter the Age:")
        dept1 = input("Enter the Department:")
        pin1 = input("Enter the Pin No.:")
        
        # db.MyCol.insert_one() is missing a collection name.
        # Assuming the collection name is 'MyCol' based on the update/read functions.
        db.MyCol.insert_one(
            {
                "name": name1,
                "age": age1,
                "dept": dept1,
                "pin": pin1
            }
        )
        print("Inserted data successfully")
    except Exception as e:
        print(str(e))

insert()

# ----------------------------------------------------

# 2. Update()
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['7Y77DB259711']

def update():
    try:
        name1 = input("Enter the Name:")
        age1 = input("Enter the Age to Update:")
        
        # Update the age of the document where name matches name1
        db.MyCol.update_one(
            {"name": name1},
            {"$set": {"age": age1}}
        )
        
        # The print statement seems to have been cut off/misplaced in the image.
        # Based on the image content:
        print("\nRecords updated successfully\n")
    except Exception as e:
        print(str(e))

update()

# ----------------------------------------------------

# 3. Read()
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['7Y77DB259711']

def read():
    try:
        # Fetch all documents from the 'MyCol' collection
        Col = db.MyCol.find() 
        print("\nAll data from database 7Y77DB259711\n")
        
        # Loop through and print each document
        for MyCol in Col:
            print(MyCol)
    except Exception as e:
        print(str(e))
