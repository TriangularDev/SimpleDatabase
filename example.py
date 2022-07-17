import TriangleDB

database = TriangleDB.db("monke")

counter = 1


database.setkey("key", "value")

print(database.getkey("key"))
print(database.getkey("nonexistantkey"))