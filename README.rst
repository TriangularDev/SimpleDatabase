============
TrianglDB
============

***************
Installation:
***************

Run this command in your project folder::

  curl "https://raw.githubusercontent.com/28klotlucas2/SimpleDatabase/main/src/__init__.py" -O "TrianglDB.py"

***************
Usage:
***************
See example.py for a better example::

  database = TrianglDB.db("DATABASE") #Creates a database.

  database.setkey("key", "value") #Sets a key.

  database.getkey("key") #Gets a key's value. If the key dosen't exist, it will return None instead.

***************
Reasons to use:
***************
1. It's fast. It took 1 second to change 2052 keys on a lower end machine.

2. It's free.

3. It's easy to use. Literally just two commands. No aysnc stuff or whatever.

4. There is a low risk of data corruption. Just storing an entire database in one file makes it easy to be corrupted by just a few bytes. Trust me, fixing broken json and SQLITE files are a pain. Especially large ones.
