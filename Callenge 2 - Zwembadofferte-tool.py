length = float(input("Enter the length of the pool in meters: "))
width = float(input("Enter the width of the pool in meters: "))
depth = float(input("Enter the depth of the pool in meters: "))
distance = float(input("Enter the distance to the prospect in kilometers: "))

volume = round(length * width * depth, 2)

excavation_cost = volume * 25
soil_removal_cost = volume * 32.50

if volume < 20:
    fixed_price = 100
else:
    fixed_price = 250

if distance < 50:
    distance_cost = distance * 1.25
else:
    distance_cost = distance * 2.05

transport_cost = fixed_price + distance_cost

if volume < 20:
    finishing_cost_per_m2 = 250
    red_color_cost = 25
    color_choice_cost = 100
else:
    finishing_cost_per_m2 = 200
    red_color_cost = 20
    color_choice_cost = 125

wall_area = 2 * (length * depth) + 2 * (width * depth)
floor_area = length * width
total_area = wall_area + floor_area

finishing_cost = total_area * finishing_cost_per_m2
total_finishing_cost = finishing_cost + red_color_cost + color_choice_cost

print(f"Totale oppervlakte voor afwerking: {total_area:.2f} m2")
