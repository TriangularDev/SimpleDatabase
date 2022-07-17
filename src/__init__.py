import os
import json
import time

databasedir = os.getcwd() + "/Databases/"

class db:
  def __init__(self, dbname):
    self.dir = databasedir + dbname + "/"
    
    try:
      os.mkdir(databasedir)
    except:
      pass
    try:
      os.mkdir(self.dir)
    except:
      pass


  def setkey(self, key, value):
    
    if not os.path.exists(self.dir + key + "/"):
      os.mkdir(self.dir + key + "/")
    
    with open(self.dir + key + "/key.json", "w") as f:

      f.write(value)
      
      f.close()

  def getkey(self, key):
    if os.path.exists(self.dir + key + "/"):
      with open(self.dir + key + "/key.json", "r") as f:

        returnthis = f.read()
      
        f.close()
      return returnthis
    
    