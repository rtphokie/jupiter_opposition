import unittest
from skyfield import almanac
from skyfield.api import Angle, load
import numpy as np

# from datetime import datetime, timedelta, date
from skyfield.api import Loader, Topos

load = Loader('/var/data')
ts = load.timescale()

planets = load('de421.bsp')
earth, jupiter = planets['earth'], planets['jupiter barycenter']
from pytz import timezone

eastern = timezone('US/Eastern')

t0 = ts.utc(1950, 1, 1)
t1 = ts.utc(2050, 1, 1)
f = almanac.oppositions_conjunctions(planets, jupiter)
t, y = almanac.find_discrete(t0, t1, f)

oppositions = t[1::2]

print('Jupiter oppositions')
print(" "*90, "closest")
print(f"{'distance (mi)':>15} {'date':>30} {'ang dia':>11} {'since':>30} {'until':>30}")
results = {}
last_closest_distance = float("inf")  # maxint
last_closest_date = None
dates = []
distances = []
x=0
for ti in oppositions:
    position = earth.at(ti).observe(jupiter)
    ra, dec, distance = position.radec()
    radius_km = 69911
    parent_diameter = Angle(radians=np.arcsin(radius_km / distance.km) * 2.0)
    datestr = ti.astimezone(eastern).strftime('%c')
    datestr_short = ti.astimezone(eastern).strftime('%x')
    dates.append(datestr)
    distances.append(distance.km)
    results[datestr] = {'distance_mi': round(distance.km * 0.621371),
                        'angular_diameter': round(parent_diameter.arcseconds(), 2),
                        'since': '', 'until': ''}
    x+=1

for x, date in enumerate(dates):
    this = results[date]
    for n1 in range(x-1, 0, -1):
        that = results[dates[n1]]
        if that['distance_mi'] < this['distance_mi'] and  results[date]['since'] == '':
            results[date]['since'] = dates[n1]
            continue
    for n1 in range(x + 1, len(dates), 1):
        that = results[dates[n1]]
        if that['distance_mi'] < this['distance_mi'] and results[date]['until'] == '':
            results[date]['until'] = dates[n1]
            continue

for datestr, data in results.items():
    # print(datestr)
    print(f"{data['distance_mi']:>15,} {datestr:>30} {data['angular_diameter']:>11.2f} {data['since']:>30} {data['until']:>30}")
