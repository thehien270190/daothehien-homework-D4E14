import pymysql
from pymongo import MongoClient

cakes_connection = MongoClient()
cakes_database = cakes_connection.get_database('cakes')
cakes_collection = cakes_database.get_collection('cakes')

client = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'Thehien2701',
    cursorclass = pymysql.cursors.DictCursor
)
database = client.cursor()

database.execute('DROP DATABASE IF EXISTS cakes')
database.execute('CREATE DATABASE cakes')

database.execute('''
    CREATE TABLE cakes.cakes(
        id VARCHAR(255),
        type VARCHAR(255),
        name VARCHAR(255),
        ppu DECIMAL(10,2),
        PRIMARY KEY (id)
    )
''')

database.execute('''
    CREATE TABLE cakes.batters(
        id INT,
        type VARCHAR(255),
        PRIMARY KEY (id)
    )
''')

database.execute('''
    CREATE TABLE cakes.toppings(
        id INT,
        type VARCHAR(255),
        PRIMARY KEY (id)
    )
''')

database.execute('''
    CREATE TABLE cakes.fillings(
        id INT,
        name VARCHAR(255),
        addcost DECIMAL(10,2),
        PRIMARY KEY (id, addcost)
    )
''')

database.execute('''
    CREATE TABLE cakes.cake_batter(
        cake_id VARCHAR(255),
        batter_id INT,
        PRIMARY KEY (cake_id, batter_id)
    )
''')

database.execute('''
    CREATE TABLE cakes.cake_topping(
        cake_id VARCHAR(255),
        topping_id INT,
        PRIMARY KEY (cake_id, topping_id)
    )
''')

database.execute('''
    CREATE TABLE cakes.cake_filling(
        cake_id VARCHAR(255),
        filling_id INT,
        PRIMARY KEY (cake_id, filling_id)
    )
''')

query = {
    'type': {'$ne': None},
    'name': {'$ne': None},
    'ppu': {'$ne': None}
}
cakes = cakes_collection.find(query)
for cake in cakes:
    database.execute(f'''
        INSERT INTO `cakes`.cakes(`id`, `type`, `name`, `ppu`)
        VALUES("{cake['_id']}", "{cake['type']}", "{cake['name']}", {cake['ppu']})
    ''')

query = [
    {'$unwind': '$batters.batter'},
    {'$group': {'_id': '$batters.batter'}}
]
batters = cakes_collection.aggregate(query)
for batter in batters:
    database.execute(f'''
        INSERT INTO `cakes`.batters(`id`, `type`)
        VALUES({batter['_id']['id']}, "{batter['_id']['type']}")
    ''')

query = [
    {'$unwind': '$topping'},
    {'$group': {'_id': '$topping'}}
]
toppings = cakes_collection.aggregate(query)
for topping in toppings:
    database.execute(f'''
        INSERT INTO `cakes`.toppings(`id`, `type`)
        VALUES({topping['_id']['id']}, "{topping['_id']['type']}")
    ''')

query = [
    {'$unwind': '$fillings.filling'},
    {'$group': {'_id': '$fillings.filling'}}
]
fillings = cakes_collection.aggregate(query)
for filling in fillings:
    database.execute(f'''
        INSERT INTO `cakes`.fillings(`id`, `name`, `addcost`)
        VALUES({filling['_id']['id']}, "{filling['_id']['name']}", {filling['_id']['addcost']})
    ''')

query = [{'$unwind': '$batters.batter'}]
cake_batter_database = cakes_collection.aggregate(query)
for cake_batter in cake_batter_database:
    database.execute(f'''
        INSERT INTO `cakes`.cake_batter(`cake_id`, `batter_id`)
        VALUES("{cake_batter['_id']}", {cake_batter['batters']['batter']['id']})
    ''')

query = [{'$unwind': '$topping'}]
cake_topping_database = cakes_collection.aggregate(query)
for cake_topping in cake_topping_database:
    database.execute(f'''
        INSERT INTO `cakes`.cake_topping(`cake_id`, `topping_id`)
        VALUES("{cake_topping['_id']}", {cake_topping['topping']['id']})
    ''')

query = [{'$unwind': '$fillings.filling'}]   
cake_filling_database = cakes_collection.aggregate(query)
for cake_filling in cake_filling_database:
    database.execute(f'''
        INSERT INTO `cakes`.cake_filling(`cake_id`, `filling_id`)
        VALUES("{cake_filling['_id']}", {cake_filling['fillings']['filling']['id']})
    ''') 



client.commit()