from worlds.extra import Extra
from worlds.jarilo_vi import Silvermane_Guard
from worlds.penacony.golden_hour import Golden_Hour
from worlds.penacony.dreams_edge import Dreams_Edge
from worlds.penacony.childs_dream import Childs_Dream
from worlds.penacony.the_reverie_dreamscape import The_Reverie_Dreamscape
from worlds.penacony.dewlight_pavilion import Dewlight_Pavilion
from worlds.penacony.clock_studio_theme_park import Clock_Studios_Theme_Park
from worlds.penacony.audition_venue import Audition_Venue
from worlds.penacony.penacony_grand_theater import Penacony_Grand_Theater
from worlds.penacony.the_soaring_clock_hand import The_Soaring_Clock_Hand


class Penacony:
    '''
    Status: 8/9
    '''
    def __init__(self, device, mode='credits'):
        self.mode = mode
        self.extra = Extra(device)
        self.silvermane_guard = Silvermane_Guard(device)
        self.golden_hour = Golden_Hour(device)
        self.dreams_edge = Dreams_Edge(device)
        self.childs_dream = Childs_Dream(device)
        self.the_reverie_dreamscape = The_Reverie_Dreamscape(device)
        self.dewlight_pavilion = Dewlight_Pavilion(device)
        self.clock_studios_theme_park = Clock_Studios_Theme_Park(device)
        self.audition_venue = Audition_Venue(device)
        self.penacony_grand_theater = Penacony_Grand_Theater(device)
        self.the_soaring_clock_hand = The_Soaring_Clock_Hand(device)
    async def farm(self):
        '''
        Status  8/9 (new: theater, audition) /n
        TP      5 -> ???                    /n
        R2/R4   5 / 3                       /n
        XP      ???/???                   /n
        Time    ???
        '''
        await self.extra.restore_tp(tp=4, info='Penacony 1')    # TP:+4->5 Time:???
        await self.dreams_edge.farm()                           # TP:-4->1 XP:7668/9612 Time:431    
        await self.silvermane_guard.restore_tp(tp=4.1)          # TP:+4->5 Time:85
        await self.childs_dream.farm()                          # TP:-3->2 R2:4 XP:5832/5832 Time:???
        await self.extra.restore_tp(tp=4, info='Penacony 2')    # TP:+4->5 Time:???
        await self.clock_studios_theme_park.farm()              # TP:-4->1 XP:7648/7648 Time:???
        await self.silvermane_guard.restore_tp(tp=4.2)          # TP:+4->5 Time:???
        await self.the_reverie_dreamscape.farm()                # TP:-???->1 XP:14580/15552 Time:? R2/4:1/2
        await self.golden_hour.restore_tp(tp=4.1)               # TP:+4->5 Time:???
        await self.dewlight_pavilion.farm()                     # TP:-14->1 XP:11448/11448 Time: R2/4:1/2
        await self.golden_hour.restore_tp(tp=4.2)               # TP:+4->5 Time:80
        await self.penacony_grand_theater.farm()                # XP:?/? Time: TP:1->3 R4:0 R2:0 # unoptimized/unfinished
        await self.audition_venue.farm()
        await self.the_soaring_clock_hand.restore_tp(tp=4)      # TP:+4->5 Time:???
    async def dev(self):
        raise SystemExit()


