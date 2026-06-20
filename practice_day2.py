points = [25, 18, 15, 12, 10]
sus=0
for a in points:
    a_ = int(a)
    sus+= a_


driver = {"name": "Lewis Hamilton", "team": "Ferrari", "number": 44}
# print(f"{driver['number']} {driver['name']} ({driver['team']})")

standings = [
    {"name": "Verstappen", "points": 437},
    {"name": "Norris", "points": 374},
    {"name": "Leclerc", "points": 356},
]

for index, a  in enumerate(standings, start=1):
    print(f"{index}. {a["name"]} - {a["points"]} очков")