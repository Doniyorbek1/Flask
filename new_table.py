from tinydb import TinyDB

db = TinyDB("db.json", indent = 4)

table1 = db.table("Samsung")

table1.insert({
    'mdoel':'Samsung M32',
    "price" : 1000
})
print(table1.all())