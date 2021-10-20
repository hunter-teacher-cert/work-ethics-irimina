#assign tickets draft 

import math
import random

from airplane import Aircraft


aircraft = Aircraft(20, 5, 4)  # 20 rows, 5 columns, first 4 rows are premium economy

premium_factor = random.randint(4, 10) / 10
premium_passengers = math.floor(aircraft.vacant_premium_seats * premium_factor)

economy_factor = random.randint(7, 10) / 10
economy_passengers = math.floor(aircraft.vacant_economy_seats * economy_factor)

for i in range(premium_passengers):
    aircraft.assign_seat(*aircraft.get_random_premium_seat(), i)


for i in range(economy_passengers):
    aircraft.assign_seat(*aircraft.get_random_economy_seat(), i)

print(aircraft)
