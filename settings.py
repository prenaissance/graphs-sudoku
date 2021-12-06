class ScreenSettings:
    def __init__(self):
        self.screen_width = 900
        self.screen_height = 900
        self.square_width = round(self.screen_width / 9)
        self.square_height = round(self.screen_height / 9)
        self.fw = round(self.square_width / 3)
        self.fh = round(self.square_height / 5 * 3)
        # if increase tick it increase visualisation speed
        self.tick = 100

    def changeResolution(self, new_width, new_height):
        self.screen_width = new_width
        self.screen_height = new_height
        self.square_width = round(self.screen_width / 9)
        self.square_height = round(self.screen_height / 9)
        self.fw = round(self.square_width / 3)
        self.fh = round(self.square_height / 5 * 3)

