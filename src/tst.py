import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel, QMainWindow, QVBoxLayout, QHBoxLayout
from functools import partial
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

p = Player('outside')

# def main():
#     while True:
#         movement = input("In which direction would you like to move:\n\t[N] North\n[W] West\t[E] East\n\t[S] South\n[Q] Quit\n[I]  View Items in Room").lower()

#         try:
#             if not movement.isalpha() or not all(c in "nsewqi" for c in movement):
#                 raise ValueError
#         except ValueError:
#             print('Movement is not allowed.')

#         if movement == 'q':
#             break

#         if movement == 'i':
#             print('i')
#             continue

#         if not hasattr(room[p.current_room], movement + '_to'):
#             print('You just walked in to a wall! Try again!')
#             continue

#         else:
#             d = getattr(room[p.current_room], movement + '_to')
#             print(f'You are now in then {d.name}.')
#             p.current_room = d.name.lower().replace("grand ", "")



        # ("In which direction would you like to move:\n\t[N] North\n[W] West\t[E] East\n\t[S] South\n[Q] Quit\n[I]  View Items in Room").lower()
class GamePlay():
    def __init__(self):
      super().__init__()
    def __init__(self, current_room, name = 'Player'):
        self.name = name
        self.current_room = current_room
      self.name = name
      self.foo('foo')


class GameUi(QMainWindow):
    # print(f"You are located {p.current_room}.\n{room[p.current_room].description}.")
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Adventure Game')
        self.setFixedSize(500, 500)

        # Set the central widget and the general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        # Create the display and the buttons
        self.buttons = {}
        self._createButtons()
        self._createMessage()
        self._createMessage2()
        self.movement = ''
        self.gameplay = GamePlay()

    def _createMessage(self):
        self.msgLayout = QHBoxLayout()
        self.msg = QLabel(f"You are located {p.current_room}.\n{room[p.current_room].description}.")
        self.msgLayout.addWidget( self.msg )
        self.generalLayout.addLayout(self.msgLayout)

    def _createMessage2(self):
        self.msgLayout = QHBoxLayout()
        self.msg2 = QLabel("In which direction would you like to move:\n[N] North\n[W] West\n[E] East\n[S] South\n[Q] Quit\n[I]  View Items in Room")
        self.msgLayout.addWidget( self.msg2 )
        self.generalLayout.addLayout(self.msgLayout)

    def btnClicked(self, btn):
        self.msg.setText(f'You are now in the {btn}.')
        self.movement = btn

    def _createButtons(self):
        buttonsLayout = QGridLayout()
        buttons = { 'N': (0, 1),
                    'W': (1, 0),
                    'E': (1, 3),
                    'S': (2, 1)
                  }
        # Create the buttons and add them to the grid layout
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(40, 40)
            self.buttons[btnText].clicked.connect(partial(self.btnClicked, btnText))
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
            # Add buttonsLayout to the general layout
            self.generalLayout.addLayout(buttonsLayout)
    
    # def main_gameplay(self):
    #     # def loaded():
    #     print('Loaded')
    #     def getFoo(f):
    #         print(f)

def main():
    adventure = QApplication(sys.argv)
    view = GameUi()
    view.show()
    # print(view.msg.text)
    sys.exit(adventure.exec_())

if __name__ == '__main__':
    main()



# def greeting():
#     """Slot function."""
#     if msg.text():
#         msg.setText("")
#     else:
#         msg.setText("Hello World!")



# app = QApplication([])
# window = QWidget()
# layout = QGridLayout()
# btn1 = QPushButton('North')
# btn1.clicked.connect(greeting)

# layout.addWidget(btn1, 0, 1)
# # layout.addWidget(QPushButton('North'), 0, 1)
# layout.addWidget(QPushButton('West'), 1, 0)
# layout.addWidget(QPushButton('East'), 1, 3)
# layout.addWidget(QPushButton('South'), 2, 1)
# msg = QLabel('')
# layout.addWidget(msg, 4, 1)
# window.setLayout(layout)
# window.show()
# app.exec_()