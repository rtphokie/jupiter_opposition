import unittest
from skyfield import almanac
from skyfield.api import Angle, load
import numpy as np

# from datetime import datetime, timedelta, date
from skyfield.api import Loader, Topos
load = Loader('/var/data')
ts = load.timescale()

# import numpy as np
# from scipy.signal import argrelextrema
planets = load('de421.bsp')
earth, jupiter, venus, moon = planets['earth'], planets['jupiter barycenter'], planets['venus'], planets['moon']
from pytz import timezone

eastern = timezone('US/Eastern')

t0 = ts.utc(1950, 1, 1)
t1 = ts.utc(2050, 1, 1)
f = almanac.oppositions_conjunctions(planets, jupiter)
t, y = almanac.find_discrete(t0, t1, f)

oppositions = t[1::2]

print('Jupiter oppositions')
print(f"{'distance (mi)':>15} {'date':>30} {'ang dia':>11}")
results = {}
last_closest_distance= float("inf")  # maxint
last_closest_date = None
for ti in oppositions:
    position = earth.at(ti).observe(jupiter)
    ra, dec, distance = position.radec()
    radius_km = 69911
    parent_diameter = Angle(radians=np.arcsin(radius_km / distance.km) * 2.0)
    datestr = ti.astimezone(eastern).strftime('%c')
    datestr_short = ti.astimezone(eastern).strftime('%x')
    results[datestr]={'distance_mi': round(distance.km * 0.621371),
                     'angular_diameter': round(parent_diameter.arcseconds(),2),
                     'superlative': ''}

    if distance.km < last_closest_distance:
        if last_closest_date is not None:
            results[datestr]['superlative']+=f' closest since {last_closest_date}'
        last_closest_distance=distance.km
        last_closest_date=datestr_short


for datestr, data in results.items():
    # print(datestr)
    print(f"{data['distance_mi']:>15,} {datestr:>30} {data['angular_diameter']:>11.2f} {data['superlative'].strip()}")
