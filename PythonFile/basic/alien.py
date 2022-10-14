alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

print("Adding new keys to the aliens")
alien_0['difficulty'] = 'easy'
alien_0['power'] = 'fire'
alien_0['level'] = 1

# print(alien_0)

alien_1 = {'color': 'yellow', 'points': 10, 'difficulty': 'medium', 'power': 'fire and water', 'level': 2}
# empty dictionary
alien_2 = {}
alien_2['color'] = 'red'
alien_2['points'] = 15
alien_2['difficulty'] = 'hard'
alien_2['power'] = 'fire, water and wind'
alien_2['level'] = 3


print(alien_0)
print(alien_1)
print(alien_2)

alien_2['color'] = 'blue'
print(alien_2)

power_increment = 0
# increase power points
if alien_2['level'] == 1:
    power_increment = 2
elif alien_2['level'] == 2:
    power_increment = 5
elif alien_2['level'] == 3:
    power_increment = 10

alien_2['points'] = alien_2['points'] + power_increment
print(f"After increment the power point of alien is {alien_2['points']}")

print(alien_2)
# removing key values from the dictionary
del alien_2['color']
del alien_2['power']
print(alien_2)

#color = alien_2['color'].title()
#print(color)

color = alien_2.get('color', "The required field is not present")
print(color)