import SimpleDatabase

database = SimpleDatabase.db("monke")

database.setkey("key", "value")

print(database.getkey("key"))

print(database.getkey("nonexistantkey"))