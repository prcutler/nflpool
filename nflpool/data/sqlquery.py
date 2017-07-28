import sqlite3

db = 'nflpool.sqlite'


def passyds():
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    cur.execute('''SELECT player_id, passyds FROM player_stats, nflplayers
      WHERE Customers.CustomerId = Reservations.CustomerId;''')

    cur.execute('''SELECT Name, Day FROM Customers, Reservations
      WHERE Customers.CustomerId = Reservations.CustomerId;''')

