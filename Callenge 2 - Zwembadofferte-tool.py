length = 8
width = 3
depth = 1.5

volume = round(length * width * depth, 2)

excavation_cost = volume * 25
soil_removal_cost = volume * 32.50

distance = 60

if volume < 20:
    fixed_price = 100
else:
    fixed_price = 250

if distance < 50:
    distance_cost = distance * 1.25
else:
    distance_cost = distance * 2.05

transport_cost = fixed_price + distance_cost

print(f"Offerte voor een zwembad van {length} bij {width} bij {depth} meter (inhoud: {volume} m3)")
print(f"Uitgraven:                         € {excavation_cost:.2f}")
print(f"Afvoeren grond:              € {soil_removal_cost:.2f}")
print(f"Voorrijkosten                    € {transport_cost:.2f}")
print(f"Totaal:                               € {excavation_cost + soil_removal_cost + transport_cost:.2f}")
