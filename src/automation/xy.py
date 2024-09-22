class OnePlus7T():
    def __init__(self):
        w = 2400
        h = 1080
        self.width = w
        self.height = h
        self.center = (int(w/2), int(h/2))
        self.map = (int(w*240/2400), int(h*190/1080))
        self.star_rail_map = (int(w*2000/2400), int(h*145/1080))
        self.sprint = (int(w*2145/2400), int(h*925/1080))
        self.attack = (int(w*1965/2400), int(h*825/1080))
        self.skill = (int(w*1765/2400), int(h*925/1080))
        self.technique = (int(w*1816/2400), int(h*926/1080))
        self.inventory = (int(w*2033/2400), int(h*58/1080))
        self.phone = (int(w*120/2400), int(h*80/1080))
        self.food_menu = (int(w*155/2400), int(h*721/1080))
        self.food_fav = (int(w*364/2400), int(h*209/1080))
        self.vjoy = {}
        self.vjoy['r'] = 150
        self.vjoy['center'] = (int(w*440/2400), int(h*839/1080))
        self.vjoy['n'] = (self.vjoy['center'][0], self.vjoy['center'][1]-150)
        self.vjoy['s'] = (self.vjoy['center'][0], self.vjoy['center'][1]+150)
        self.vjoy['w'] = (self.vjoy['center'][0]-150, self.vjoy['center'][1])
        self.vjoy['e'] = (self.vjoy['center'][0]+150, self.vjoy['center'][1])
        self.vjoy['ne'] = (self.vjoy['center'][0]+100, self.vjoy['center'][1]-100)
        self.vjoy['se'] = (self.vjoy['center'][0]+100, self.vjoy['center'][1]+100)
        self.vjoy['sw'] = (self.vjoy['center'][0]-100, self.vjoy['center'][1]+100)
        self.vjoy['nw'] = (self.vjoy['center'][0]-100, self.vjoy['center'][1]-100)