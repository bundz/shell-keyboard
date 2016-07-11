import json

from lib.keyboard import Keyboard
from lib.ui import UserInterface

board_config = json.loads(open("config/config.json").read())

keyboard = Keyboard(board_config)

ui = UserInterface()

while True:
    char = ui.get_char()
    keyboard.play(char)