import flet as ft
import flet_audio as fta


class AudioController:
    def __init__(self, page: ft.Page):
        self.page = page
        self.audio_player = fta.Audio(
            src="C:\\Users\\Jay\\Music\\Local Music\\Lift Yr. Skinny Fists Like Antennas to Heaven!\\01. Storm.flac",   # temporary
            volume=1,
            balance=0,
            autoplay=False
        )


    # basic controls for now
    # async def play(self, e):
    #     await self.audio_player.play()


    async def pause(self):
        await self.audio_player.pause()


    async def resume(self):
        await self.audio_player.resume()