from pygame import mixer

class Keyboard:
    def __init__(self, config):
        self.buttons = {}
        mixer.init()
        for key in config.keys():
            path = "sounds/" + config[key]
            self.buttons[key] = mixer.Sound(path)

    def play(self, char):
        if(char in self.buttons.keys()):
            self.buttons[char].play()
            
