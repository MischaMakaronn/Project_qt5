import sqlite3 as sl

"""
SELECT ('столбцы или * для выбора всех столбцов; обязательно')
FROM ('таблица; обязательно')
WHERE ('условие/фильтрация, например, city = 'Moscow'; необязательно')
GROUP BY ('столбец, по которому хотим сгруппировать данные; необязательно')
HAVING ('условие/фильтрация на уровне сгруппированных данных; необязательно')
ORDER BY ('столбец, по которому хотим отсортировать вывод; необязательно')
"""

con = sl.connect('warehouse.db')

with con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS Clients (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
        name TEXT, 
        phone_number TEXT, 
        address TEXT,
        UNIQUE (phone_number)
        );
    """)

    con.execute("""
        CREATE TABLE IF NOT EXISTS Category (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        description TEXT
        );
    """)

    con.execute("""
        CREATE TABLE IF NOT EXISTS Goods (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        code TEXT,
        name TEXT,
        description TEXT,
        photo TEXT,
        price FLOAT,
        weight FLOAT,
        unit TEXT,
        count INTEGER,
        expiration_date DATETIME,
        sold  INTEGER,
        write_off INTEGER,
        category_id INTEGER,
        stock_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES Category (id),
        FOREIGN KEY (stock_id) REFERENCES Stock (id)
        );
    """)

    con.execute("""
        CREATE TABLE IF NOT EXISTS Orders (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        client_id INTEGER,
        good_id TEXT,
        total_price FLOAT,
        date DATETIME,
        FOREIGN KEY (client_id) REFERENCES Clients (id),
        FOREIGN KEY (good_id) REFERENCES Goods (id)
        );
    """)

    con.execute("""
        CREATE TABLE IF NOT EXISTS Stock (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        address TEXT,
        geo_text TEXT,
        geo_coordinates TEXT
        )
    """)

    con.execute("""
        CREATE TABLE IF NOT EXISTS WriteOff (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        category_id INTEGER,
        stock_id INTEGER,
        good_id INTEGER,
        count INTEGER,
        reason TEXT,
        document TEXT,
        date_off DATETIME,
        FOREIGN KEY (category_id) REFERENCES Category (id),
        FOREIGN KEY (stock_id) REFERENCES Stock (id),
        FOREIGN KEY (good_id) REFERENCES Goods (id)
        )
    """)

    con.execute("""
        CREATE TABLE IF NOT EXISTS Supply (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        good_id INTEGER,
        price FLOAT,
        stock_id INTEGER,
        count_in INTEGER,
        count_current INTEGER,
        supply_date DATETIME,
        expiration_date DATETIME,
        document TEXT,
        FOREIGN KEY (good_id) REFERENCES Goods (id),
        FOREIGN KEY (stock_id) REFERENCES Stock (id)
        )
    """)

con.execute("""
        CREATE TABLE IF NOT EXISTS MovementOfGoods (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        supply_id INTEGER,
        stock_in_id INTEGER,
        stock_out_id INTEGER,
        count_in INTEGER,
        count_current INTEGER,
        movement_date DATETIME,
        movement_status TEXT,
        document TEXT,
        FOREIGN KEY (supply_id) REFERENCES Supply (id),
        FOREIGN KEY (stock_in_id) REFERENCES Stock (id),
        FOREIGN KEY (stock_out_id) REFERENCES Stock (id)
        )
    """)
