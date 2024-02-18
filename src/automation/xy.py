class OnePlus7T():
    def __init__(self):
        w = 2400
        h = 1080
        self.width = 2400
        self.height = 1080
        self.map = (int(w*240/2400), int(h*190/1080))
        self.star_rail_map = (int(w*2000/2400), int(h*145/1080))
        self.sprint = (int(w*2145/2400), int(h*925/1080))
        self.attack = (int(w*1965/2400), int(h*825/1080))
        self.skill = (int(w*1765/2400), int(h*925/1080))
        self.vjoy = {}
        self.vjoy['mid'] = (int(w*440/2400), int(h*839/1080))
        self.vjoy['n'] = (self.vjoy['mid'][0], self.vjoy['mid'][1]-150)
        self.vjoy['s'] = (self.vjoy['mid'][0], self.vjoy['mid'][1]+150)
        self.vjoy['w'] = (self.vjoy['mid'][0]-150, self.vjoy['mid'][1])
        self.vjoy['e'] = (self.vjoy['mid'][0]+150, self.vjoy['mid'][1])
        self.vjoy['ne'] = (self.vjoy['mid'][0]+100, self.vjoy['mid'][1]-100)
        self.vjoy['se'] = (self.vjoy['mid'][0]+100, self.vjoy['mid'][1]+100)
        self.vjoy['sw'] = (self.vjoy['mid'][0]-100, self.vjoy['mid'][1]+100)
        self.vjoy['nw'] = (self.vjoy['mid'][0]-100, self.vjoy['mid'][1]-100)