from room import Room
from player import Player
from item import Item
from textwrap import dedent

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


item = {
    'keys':    Item("Keys", "Car keys."),
}
room['foyer'].add_item = item['keys']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
p = Player('outside')

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def main():
    print(f"You are located {p.current_room}.\n{room[p.current_room].description}.")
        
    while True:
        movement = input("In which direction would you like to move:\n\t[N] North\n[W] West\t[E] East\n\t[S] South\n[Q] Quit\n[I]  View Items in Room").lower()

        try:
            if not movement.isalpha() or not all(c in "nsewqi" for c in movement):
                raise ValueError
        except ValueError:
            print('Movement is not allowed.')

        if movement == 'q':
            break

        if movement == 'i':
            print('i')
            continue

        if not hasattr(room[p.current_room], movement + '_to'):
            print('You just walked in to a wall! Try again!')
            continue

        else:
            d = getattr(room[p.current_room], movement + '_to')
            print(f'You are now in then {d.name}.')
            p.current_room = d.name.lower().replace("grand ", "")

        

if __name__== "__main__":
    main()


# Add the ability to add items to rooms.

# The Room class should be extended with a list that holds the Items
# that are currently in that room.

# Add functionality to the main loop that prints out all the items that are
# visible to the player when they are in that room.

# Add capability to add Items to the player's inventory. The inventory can
# also be a list of items "in" the player, similar to how Items can be in a
# Room.