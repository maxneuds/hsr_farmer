from worlds import astral_express


class Astral_Express:
    
    def __init__(self, bot):
        self.parlor_car = astral_express.Parlor_Car(bot)

    async def goto_pompom(self):
        await self.parlor_car.teleport()


