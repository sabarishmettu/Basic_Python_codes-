# Text-Based Adventure game
# Create a map
map = {
    'room1': {
        'description': 'You are in a dark room.',
        'items': ['key'],
        'exits': {'north': 'room2'}
    },
    'room2': {
        'description': 'You are in a bright room.',
        'items': ['sword'],
        'exits': {'south': 'room1', 'east': 'room3'}
    },
    'room3': {
        'description': 'You are in a cave.',
        'items': ['treasure'],
        'exits': {'west': 'room2'}
    }
}

# Set the current room
current_room = 'room1'

# Set the player's inventory
inventory = []

# Start the game loop
while True:
    # Print the description of the current room
    print(map[current_room]['description'])

    # Print the items in the current room
    for item in map[current_room]['items']:
        print(f'You see a {item}.')

    # Print the valid exits
    print('You can go:')
    for direction, room in map[current_room]['exits'].items():
        print(f'{direction} to {room}')

    # Get the user's input
    command = input('What would you like to do?: ').lower().split()

    # Check if the user wants to go in a direction
    if command[0] == 'go':
        if command[1] in map[current_room]['exits']:
            current_room = map[current_room]['exits'][command[1]]
            print(f'You go {command[1]} to {current_room}.')
        else:
            print('You cannot go that way.')

    # Check if the user wants to take an item
    if command[0] == 'take':
        if command[1] in map[current_room]['items']:
            inventory.append(command[1])
            map[current_room]['items'].remove(command[1])
            print(f'You take the {command[1]}.')
        else:
            print('You cannot take that.')

    # Check if the user wants to quit
    if command[0] == 'quit':
        break

print('Thanks for playing!')