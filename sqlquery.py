import sqlite3

db = 'nflpool.sqlite'


def passyds():
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    cur.execute('''SELECT player_id, passyds FROM player_stats, nflplayers
      WHERE Customers.CustomerId = Reservations.CustomerId;''')

    cur.execute('''SELECT Name, Day FROM Customers, Reservations
      WHERE Customers.CustomerId = Reservations.CustomerId;''')


select
laps.lap_id,
laps.laptime,
heats.heat_pos,
tracks.name
from laps

inner
join
heats
on
laps.heat_id = heats.heat_id
inner
join
tracks
on
tracks.track_id = heats.track_id;

SELECT
teams.conference,
player_stats.passyds,
player_stats.player_id,
nflplayers.player_id,
nflplayers.team_id,
teams.team_id,
from nflplayers

inner
join
on
nflplayers.player_id = player_stats.player_id
inner
join
on
teams.team_id = nflplayers.team_id;

near
"from": syntax
error: