import math
# a cable run planner

distance = float(input("Input distance (m): "))
segments = math.ceil(distance / 100)
repeaters = segments - 1
last_segment = distance - (segments - 1) * 100

print(f'\nDistance: {distance} m \nSegments: {segments} \nRepeaters: {repeaters} \nLast segment: {last_segment} m')

expected_cable = float(input("\nEnter expected cable length: "))
measured_cable = float(input("Enter measured cable length: "))

margin_error = 0.02 * expected_cable
difference = abs(measured_cable - expected_cable)
error_percentage = difference / expected_cable * 100

print(f'Error: {error_percentage:.2f}%')
if difference <= margin_error:
    print("PASS")
else:
    print("FAIL")